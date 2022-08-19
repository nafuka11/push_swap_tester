from pathlib import Path


class PushSwapError(Exception):
    pass


class CommandNotFoundError(PushSwapError):
    """push_swap, checkerが見つからなかった時のエラー"""

    def __init__(self, path: Path) -> None:
        self.path = path

    def __str__(self) -> str:
        return f"Command not found: {self.path}"


class ExecutePermissionError(PushSwapError):
    """push_swap, checkerに実行権限がない時のエラー"""

    def __init__(self, path: Path) -> None:
        self.path = path

    def __str__(self) -> str:
        return f"File is not executable: {self.path}"


class ArgRangeError(PushSwapError):
    """引数生成時のエラー"""

    def __init__(self, min: int, max: int) -> None:
        self.min = min
        self.max = max

    def __str__(self) -> str:
        return f"Range generate error: range({self.min}, {self.max})"
