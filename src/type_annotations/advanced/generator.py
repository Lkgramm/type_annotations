"""
TODO:

`gen` is a generator that yields a integer, and can accept a string sent to it.
It does not return anything.
"""


from typing import Generator, assert_type


def gen() -> Generator[int, str, None]:
    """You don't need to implement it"""
    ...


if __name__ == "__main__":
    generator = gen()
    assert_type(next(generator), int)
    generator.send("sss")
    generator.send(3)  # type: ignore
