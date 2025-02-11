"""
TODO:

Define a callable type that accepts a string parameter called `name` and returns None.
"""


from typing import Protocol, Any


class SingleStringInput(Protocol):
    def __call__(self, name: Any) -> None:
        ...


if __name__ == "__main__":
    def accept_single_string_input(func: SingleStringInput) -> None:
        func(name="name")


    def string_name(name: str) -> None:
        ...


    def string_value(value: str) -> None:
        ...


    def return_string(name: str) -> str:
        return name


    accept_single_string_input(string_name)
    accept_single_string_input(string_value)  # type: ignore[arg-type]
    accept_single_string_input(return_string)  # type: ignore[arg-type]
