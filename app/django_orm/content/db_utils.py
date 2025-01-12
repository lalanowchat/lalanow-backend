import logging

import django.db
import django.db.models
from django.db.utils import OperationalError, ConnectionHandler

logger = logging.getLogger(__name__)


def ensure_connection(connection_name: str = "default") -> None:
    """Verify database connection

    See implementation: https://github.com/django/django/blob/stable/4.2.x/django/db/backends/base/base.py#L285

    Args:
        connection_name (str, optional): Name of Django database connection to ensure. Defaults to "default".

    Raises:
        ValueError: If the connection cannot be ensured.
    """
    db_connection: ConnectionHandler = django.db.connections[connection_name]
    if db_connection is None:
        raise ValueError("Database connection not available.")
    if db_connection.connection is not None and not db_connection.is_usable():
        logger.info("Database connection not usable; attempting restart.")
        db_connection.close()
        try:
            db_connection.ensure_connection()
            logger.info("Database connection had to be restarted.")
        except OperationalError:
            logger.error("Failed to restart database connection.")
            raise ValueError("Failed to re-establish database connection.")


def execute_custom_query(query: str) -> list[dict]:
    """
    Execute custom query through the Django PostgreSQL connection
    :param query: the query to execute
    :return: the results of the query as a list of dictionaries
    """
    db_connection = django.db.connections["default"]

    with db_connection.cursor() as cursor:
        cursor.execute(query)
        # returns column names
        if not cursor.description:
            return []

        columns = [col[0] for col in cursor.description]

        return [
            # returns column name and the value as dict
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
