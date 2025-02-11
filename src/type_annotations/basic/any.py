"""
TODO:

Modify `foo` so it takes an argument of arbitrary type.
"""


from typing import Any, Optional


def foo(a: Any, b: Optional[str] = None):
    """⬆️ Change me. No need to implement the function."""


if __name__ == "__main__":
    foo(1)
    foo("10")
    foo(1, 2)  # type: ignore[arg-type]
