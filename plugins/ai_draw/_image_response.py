import base64
import json
from dataclasses import dataclass
from typing import Any


class ImageResponseParseError(RuntimeError):
    pass


@dataclass(frozen=True)
class ImageReference:
    b64_json: str | None = None
    url: str | None = None


_IMAGE_MAGIC_BYTES = (
    b"\x89PNG\r\n\x1a\n",
    b"\xff\xd8\xff",
    b"GIF87a",
    b"GIF89a",
    b"RIFF",
)


def parse_image_response_body(body: bytes, content_type: str = "") -> dict[str, Any] | bytes:
    content_type = (content_type or "").split(";", 1)[0].strip().lower()
    if _looks_like_image(body, content_type):
        return body

    if not body:
        raise ImageResponseParseError(f"empty response body; content_type={content_type or 'unknown'}")

    try:
        text = body.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ImageResponseParseError(
            f"response is neither JSON nor image bytes; content_type={content_type or 'unknown'}"
        ) from exc

    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ImageResponseParseError(
            "response is neither JSON nor image bytes; "
            f"content_type={content_type or 'unknown'}; "
            f"body_preview={_body_preview(text)}"
        ) from exc

    if not isinstance(data, dict):
        raise ImageResponseParseError(f"expected JSON object, got {type(data).__name__}")
    return data


def extract_image_reference(data: dict[str, Any]) -> ImageReference:
    relay_error = data.get("RelayError") or data.get("error")
    if relay_error:
        if isinstance(relay_error, str):
            message = relay_error
        elif isinstance(relay_error, dict):
            message = relay_error.get("message") or str(relay_error)
        else:
            message = str(relay_error)
        raise RuntimeError(f"GPT-Image-2 API returned error: {message}")

    for item in _candidate_items(data):
        url = _first_string(item, "url", "image_url")
        if url:
            return ImageReference(url=url)

        b64_json = _first_string(item, "b64_json", "b64", "base64")
        if b64_json:
            return ImageReference(b64_json=b64_json)

    raise ImageResponseParseError("no image field found")


def decode_base64_image(value: str) -> bytes:
    if value.startswith("data:"):
        _, sep, value = value.partition(",")
        if not sep:
            raise ImageResponseParseError("invalid data URL image payload")
    value = "".join(value.split())

    try:
        return base64.b64decode(value, validate=True)
    except Exception as exc:
        raise ImageResponseParseError("image base64 decode failed") from exc


def summarize_response_json(data: dict[str, Any]) -> str:
    return json.dumps(_scrub_large_strings(data), ensure_ascii=False)[:500]


def format_response_body_dump(body: bytes, content_type: str = "") -> str:
    content_type = (content_type or "").strip() or "unknown"
    header = f"content_type={content_type}\nbody_bytes={len(body)}"
    if not body:
        return f"{header}\nbody=<empty>"

    try:
        text = body.decode("utf-8-sig")
    except UnicodeDecodeError:
        text = body.hex()
        header += "\nbody_encoding=hex"
    else:
        header += "\nbody_encoding=utf-8"
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            pass
        else:
            return f"{header}\nbody_json={format_response_json_dump(data)}"

    return f"{header}\nbody={text}"


def format_response_json_dump(data: Any) -> str:
    return json.dumps(_shorten_base64_fields(data), ensure_ascii=False, indent=2)


def _candidate_items(data: dict[str, Any]):
    yield data

    image_data = data.get("data")
    if isinstance(image_data, list):
        for item in image_data:
            if isinstance(item, dict):
                yield item

    output = data.get("output")
    if isinstance(output, list):
        for item in output:
            if not isinstance(item, dict):
                continue
            if item.get("type") == "image_generation_call" and isinstance(item.get("result"), str):
                yield {"b64_json": item["result"]}
            yield item


def _looks_like_image(body: bytes, content_type: str) -> bool:
    if not body:
        return False
    if content_type.startswith("image/"):
        return True
    if body.startswith(b"RIFF") and body[8:12] == b"WEBP":
        return True
    return any(body.startswith(prefix) for prefix in _IMAGE_MAGIC_BYTES if prefix != b"RIFF")


def _first_string(data: dict[str, Any], *keys: str) -> str | None:
    for key in keys:
        value = data.get(key)
        if isinstance(value, str) and value:
            return value
    return None


def _body_preview(text: str, limit: int = 200) -> str:
    return " ".join(text[:limit].split())


def _scrub_large_strings(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: _scrub_large_strings(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_scrub_large_strings(item) for item in value]
    if isinstance(value, str) and len(value) > 120:
        return f"<string {len(value)} chars>"
    return value


def _shorten_base64_fields(value: Any, parent: dict[str, Any] | None = None) -> Any:
    if isinstance(value, dict):
        return {
            key: _shorten_base64_value(key, item, value)
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [_shorten_base64_fields(item, parent) for item in value]
    return value


def _shorten_base64_value(key: str, value: Any, parent: dict[str, Any]) -> Any:
    if isinstance(value, str) and _is_base64_field(key, parent):
        return _shorten_base64_string(value)
    return _shorten_base64_fields(value, parent)


def _is_base64_field(key: str, parent: dict[str, Any]) -> bool:
    normalized = key.lower()
    if "b64" in normalized or "base64" in normalized:
        return True
    return normalized == "result" and parent.get("type") == "image_generation_call"


def _shorten_base64_string(value: str) -> str:
    if value.startswith("data:") and "," in value:
        prefix, b64_value = value.split(",", 1)
        if len(b64_value) > 10:
            return f"{prefix},{b64_value[:10]}..."
        return value
    if len(value) > 10:
        return f"{value[:10]}..."
    return value
