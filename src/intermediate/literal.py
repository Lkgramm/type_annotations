"""
TODO:

foo only accepts literal 'left' and 'right' as its argument.
"""


from typing import Literal


def foo(direction: Literal["left", "right"]):
    ...


if __name__ == "__main__":
    foo("left")
    foo("right")

    a = "".join(["l", "e", "f", "t"])
    foo(a)  # type: ignore[arg-type]
