from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TesterResult:
    args: list[str]
    op_count: int
    is_correct: bool

    def __str__(self) -> str:
        text = ""
        if self.is_correct:
            text += "[OK]"
        else:
            text += "[KO]"
        text += f"{' '.join(self.args)}: {self.op_count}"
        return text
