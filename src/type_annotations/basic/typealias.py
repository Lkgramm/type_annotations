"""
TODO:

Create a new type called Vector, which is a list of float.
"""


Vector = list[float]


def foo(v: Vector):
    pass


if __name__ == "__main__":
    foo([1.1, 2])
    foo(1)  # type: ignore[arg-type]
    foo(["1"])  # type: ignore[list-item]
