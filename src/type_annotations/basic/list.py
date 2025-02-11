"""
TODO:

foo should accept a list argument, whose elements are string.
"""


def foo(x: list[str]):
    pass


if __name__ == "__main__":
    foo(["foo", "bar"])
    foo(["foo", 1])  # type: ignore[list-item]
