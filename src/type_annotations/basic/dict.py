"""
TODO:

foo should accept a dict argument, both keys and values are string.
"""


def foo(x: dict[str, str]):
    pass


if __name__ == "__main__":
    foo({"foo": "bar"})
    foo({"foo": 1})  # type: ignore[dict-item]
