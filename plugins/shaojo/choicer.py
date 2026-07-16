"""Random text chooser used by the shaojo plugin."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any
import random
import re
import time


class Choicer:
    _placeholder_re = re.compile(r"{(.*?)}")

    def __init__(self, config: Mapping[str, Any]):
        self.rand = random.Random()
        self.date = bool(config["date"])
        self.map: dict[str, Any] = {}
        self.vals: dict[str, str] = {}
        self.used: dict[str, set[str]] = {}

        parts = config["parts"]
        for name, value in parts.items():
            self.map[name] = self._compile(value)

        self.result = [self._compile(item) for item in config["result"]]

    def _compile(self, data: Any) -> Any:
        if isinstance(data, list):
            return self._compile_choices(data)

        if isinstance(data, str):
            return data

        if isinstance(data, dict):
            return self._compile_mapping(data)

        return []

    def _compile_choices(self, data: list[Any]) -> list:
        choices = []
        for item in data:
            if (
                isinstance(item, str)
                and item.startswith("{")
                and item.endswith("}")
            ):
                choices.extend(
                    compiled_item[0]
                    for compiled_item in self.map[item[1:-1]]
                )
            else:
                choices.append(item)
        probability = 1.0 / len(choices)
        return [(self._compile(item), probability) for item in choices]

    def _compile_mapping(self, data: dict) -> list:
        if "start" in data:
            return [(self._compile(data["d"]), data["p"], data["start"])]
        if "p" in data:
            return [(self._compile(data["d"]), data["p"])]
        return [
            (self._compile(value), probability)
            for value, probability in data.items()
        ]

    def _set_seed(self, user_id: int | str) -> None:
        date_factor = int((time.time() + 28800) // 86400) if self.date else 1
        try:
            seed = int(user_id) * date_factor
        except (TypeError, ValueError):
            seed = f"{user_id}:{date_factor}"
        self.rand.seed(seed)

    def _run_template(self, template: str, vals: Mapping[str, str] | None = None) -> str:
        if vals:
            for key, value in vals.items():
                template = template.replace(f"{{{key}}}", str(value))

        for key, value in self.vals.items():
            template = template.replace(f"{{{key}}}", str(value))

        def replace(match: re.Match[str]) -> str:
            key = match.group(1)
            map_key = key.split(":", 1)[0]
            if key not in self.used:
                self.used[key] = set()

            for _ in range(100):
                result = self._run(self.map[map_key])
                if result not in self.used[key]:
                    self.used[key].add(result)
                    return result

            return result

        return self._placeholder_re.sub(replace, template)

    def _run(self, data: Any) -> str:
        if isinstance(data, str):
            return self._run_template(data)

        if not isinstance(data, list):
            return ""
        if len(data) == 1 and len(data[0]) == 3:
            return self._run_repeating(data[0])
        return self._run_weighted(data)

    def _run_repeating(self, data: tuple) -> str:
        compiled_template, probability, index = data
        fragments = []
        while True:
            fragments.append(
                self._run_template(compiled_template, {"i": str(index)})
            )
            index += 1
            if self.rand.random() >= probability:
                return "".join(fragments)

    def _run_weighted(self, data: list) -> str:
        roll = self.rand.random()
        for compiled_item, probability in data:
            if probability > roll:
                return self._run(compiled_item)
            roll -= probability
        return ""

    def format_msg(self, user_id: int | str, name: str) -> str:
        self.vals = {"name": name}
        self.used = {}
        self._set_seed(user_id)
        return "".join(self._run(item) for item in self.result)
