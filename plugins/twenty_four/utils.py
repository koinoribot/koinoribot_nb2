replace_dict = {
    " ": "",
    "＋": "+",  # noqa: RUF001
    "－": "-",  # noqa: RUF001
    "＊": "*",  # noqa: RUF001
    "×": "*",  # noqa: RUF001
    "x": "*",
    "／": "/",  # noqa: RUF001
    "÷": "/",
    "[": "(",
    "]": ")",
    "{": "(",
    "}": ")",
    "（": "(",
    "）": ")",
    "【": "(",
    "】": ")",
}

def format_expression(string: str) -> str:
    """
    将表达式格式化
    """
    for k, v in replace_dict.items():
        string = string.replace(k, v)
    return string

