"""
TODO:

Make sure `my_list` cannot be re-assigned to.
"""


from typing import Final


my_list: Final[list[int]] = []  # noqa


if __name__ == "__main__":
    my_list.append(1)
    my_list = []  # type: ignore[misc]
    my_list = "something else"  # type: ignore[misc, assignment]
