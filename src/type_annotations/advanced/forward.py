from typing import assert_type


class MyClass:
    def __init__(self, x: int) -> None:
        self.x = x

    # TODO: Fix the type hints of `copy` to make it type check
    def copy(self) -> 'MyClass':
        copied_object = MyClass(x=self.x)
        return copied_object


if __name__ == "__main__":
    inst = MyClass(x=1)
    assert_type(inst.copy(), MyClass)
