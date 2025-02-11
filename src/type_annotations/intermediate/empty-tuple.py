"""
TODO:

foo should accept a empty tuple argument.
"""


def foo(x: tuple[()]):
    pass


if __name__ == "__main__":
    foo(())
    foo((1))  # type: ignore[arg-type]
