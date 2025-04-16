"""
TODO:

foo should return an integer argument.
"""


from typing import assert_type


def foo() -> int:
    return 1


if __name__ == "__main__":
    assert_type(foo(), int)
    assert_type(foo(), str)  # type: ignore[assert-type]
