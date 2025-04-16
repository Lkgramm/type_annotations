"""
TODO:

Define a decorator that wraps a function and returns a function with the same signature.
The decorator takes an argument `message` of type string
"""


from typing import Callable


def decorator(message: str) -> Callable: # type: ignore[empty-body]
    ...


if __name__ == "__main__":
    @decorator(message="x")
    def foo(a: int, *, b: str) -> None:
        ...


    @decorator  # type: ignore
    def bar(a: int, *, b: str) -> None:
        ...


    foo(1, b="2")
    foo(1, "2")  # type: ignore
    foo(a=1, e="2")  # type: ignore
    decorator(1)  # type: ignore
