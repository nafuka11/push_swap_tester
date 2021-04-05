import pytest

from src.exception import ArgRangeError
from src.gen_int import generate_args


@pytest.mark.parametrize(
    "min, max",
    [
        (0, 9223372036854775807),
    ],
)
def test_generate_randint(min: int, max: int) -> None:
    with pytest.raises(ArgRangeError):
        generate_args(5, min, max, 1)
