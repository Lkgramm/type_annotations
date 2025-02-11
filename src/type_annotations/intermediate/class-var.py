"""
TODO:

Class `Foo` has a class variable `bar`, which is an integer.
"""


from typing import ClassVar


class Foo:
    """Hint: No need to write __init__"""
    bar: ClassVar[int]


if __name__ == "__main__":
    Foo.bar = 1
    Foo.bar = "1"  # type: ignore[assignment]
    Foo().bar = 1  # type: ignore[misc]
