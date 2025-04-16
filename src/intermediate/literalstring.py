"""
TODO:

You're writing a web backend.
Annotate a function `execute_query` which runs SQL, but also can prevent SQL injection attacks.

NOTE: You don't need to implement `execute_query`
"""

from typing import Iterable, LiteralString


def execute_query(sql: LiteralString, parameters: Iterable[str] = ...):
    ...


if __name__ == "__main__":
    def query_user(user_id: str):
        query = f"SELECT * FROM data WHERE user_id = {user_id}"
        # LiteralString is unsupported by mypy
        execute_query(query)  # type: ignore


    def query_data(user_id: str, limit: bool) -> None:
        query = """
            SELECT
                user.name,
                user.age
            FROM data
            WHERE user_id = ?
        """

        if limit:
            query += " LIMIT 1"

        execute_query(query, (user_id,))
