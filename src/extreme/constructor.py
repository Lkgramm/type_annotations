"""
TODO:

Define a decorator `constructor_parameter` that accepts the type of Foo.
and return a wrapper function with the same signature as the constructor of Foo,
and function decorated by `constructor_parameter` can be called with an instance of Foo.
"""
from typing import Callable, ParamSpec, TypeVar

def constructor_parameter[**P, T, R](     # type: ignore[empty-body]
    cls: Callable[P, T],
) -> Callable[[Callable[[T], R]], Callable[P, R]]: 
    """
    Декоратор, который принимает тип класса и возвращает обёртку функции,
    принимающую аргументы конструктора класса и возвращающую список экземпляров.
    """
    ...


# Определение класса Foo
class Foo:
    a: int
    b: str

    def __init__(self, a: int, b: str) -> None:
        self.a = a
        self.b = b


# Пример использования декоратора
@constructor_parameter(Foo)
def func_pass(foo: Foo) -> list[Foo]:
    """
    Функция, которая принимает экземпляр Foo и возвращает список из одного элемента.
    """
    return [foo]


# Корректный вызов
res = func_pass(1, "2")
res[0].a.bit_length()  # Проверка, что res[0].a является int
res[0].b.upper()       # Проверка, что res[0].b является str


@constructor_parameter(Foo)
def func_fail(foo: Foo) -> list[Foo]:
    """
    Функция, аналогичная func_pass, но используется для проверки ошибок типов.
    """
    return [foo]


# Некорректные вызовы
func_fail("1", "2")  # type: ignore[arg-type]
func_fail([1, 2, 3])  # type: ignore[arg-type, call-arg]