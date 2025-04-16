"""
TODO:

The function `add` accepts two arguments and returns a value, they all have the same type.
"""


from typing import TypeVar, List, assert_type


T = TypeVar("T")


def add(a: T, b: T) -> T: # type: ignore[empty-body]
    ... 


if __name__ == "__main__":
    assert_type(add(1, 2), int)
    assert_type(add("1", "2"), str)
    assert_type(add(["1"], ["2"]), List[str])
    assert_type(add(1, "2"), int)  # type: ignore[assert-type]
