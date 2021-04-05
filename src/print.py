from typing import Any


def print_colored(text: str, code: int, **kwargs: Any) -> None:
    print(f"\033[{code}m{text}\033[0m", **kwargs)
