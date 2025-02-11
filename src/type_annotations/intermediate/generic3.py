"""
TODO:

The function `add` accepts one argument and returns a value, they all have the same type.
The type can only be int or subclasses of int.
"""


from typing import TypeVar, assert_type


T = TypeVar("T", bound=int)


def add(a: T) -> T:
    ...


if __name__ == "__main__":
    class MyInt(int):
        pass


    assert_type(add(1), int)
    assert_type(add(MyInt(1)), MyInt)
    assert_type(add("1"), str)  # type: ignore[type-var]
    add(["1"], ["2"])  # type: ignore[type-var, call-arg]
    add("1", 2)  # type: ignore[type-var, call-arg]
