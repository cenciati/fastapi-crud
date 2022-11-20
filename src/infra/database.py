from typing import Union

import psycopg2
from psycopg2.extras import RealDictCursor


def create_database_connection(
    host: str, database: str, user: str, password: str
) -> Union[psycopg2.extensions.connection, psycopg2.extensions.cursor]:
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            cursor_factory=RealDictCursor,
        )
        cursor = connection.cursor()
        print("Database connection succeed!")

        return connection, cursor
    except Exception as error:
        raise error
