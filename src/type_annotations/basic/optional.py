"""
TODO:

foo can accept an integer argument, None or no argument at all.
"""


from typing import Optional


def foo(x: Optional[int] = None):
    pass


if __name__ == "__main__":
    foo(10)
    foo(None)
    foo()
    foo("10")  # type: ignore[arg-type]
