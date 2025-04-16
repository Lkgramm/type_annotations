"""
TODO:

`return_self` should return an instance of the same type as the current enclosed class.
"""

from typing import TypeVar, Self


class Foo:
    def return_self(self) -> Self: # type: ignore[empty-body]
        ...

class SubclassOfFoo(Foo):
    pass


if __name__ == "__main__":
    f: Foo = Foo().return_self()
    sf: SubclassOfFoo = SubclassOfFoo().return_self()

    sf: SubclassOfFoo = Foo().return_self()  # type: ignore[assignment, no-redef]
