"""
TODO:

Class `Foo` has an instance variable `bar`, which is an integer.
"""


class Foo:
    """Hint: you don't need to write __init__"""
    bar: int


if __name__ == "__main__":
    foo = Foo()
    foo.bar = 1
    foo.bar = "1"  # type: ignore[assignment]
