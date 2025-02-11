"""
TODO:

Create a descriptor and annotate the __get__ method.
"""

from typing import TypeVar, Type, overload


O = TypeVar("O", bound="TestClass")


class Descriptor:
    @overload
    def __get__(self, instance: None, owner: Type[O]) -> 'Descriptor':
        ...

    @overload
    def __get__(self, instance: O, owner: Type[O]) -> str:
        ...

    def __get__(self, instance: O | None, owner: Type[O]) -> 'Descriptor | str':
        """you don't need to implement this"""
        ...


class TestClass:
    a = Descriptor()


if __name__ == "__main__":
    def descriptor_self(x: Descriptor) -> None:
        ...


    def string_value(x: str) -> None:
        ...


    descriptor_self(TestClass.a)
    string_value(TestClass().a)
    descriptor_self(TestClass().a)  # type: ignore
    string_value(TestClass.a)  # type: ignore
