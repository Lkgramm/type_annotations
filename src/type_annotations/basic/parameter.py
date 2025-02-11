"""
TODO:

foo should accept an integer argument.
"""


def foo(x: int):
    pass


if __name__ == "__main__":
    foo(10)
    foo("10")  # type: ignore[arg-type]
