import pytest
from testcontainers.postgres import PostgresContainer
from sqlalchemy import create_engine

from common.sql_queries import create_table_users, insert_user

from models.User import User


@pytest.fixture()
def fetch_users():
    # User(id=1, first_name='islam', last_name='islamkz', email='islamkz@gmail.com', created=datetime.date(2021, 1, 1), status='completed')

    return [
        {
            "id": 1,
            "first_name": "islam",
            "last_name": "islamkz",
            "email": "islamkz@gmail.com",
            "created": "2021-01-01",
            "status": "completed",
        },
        {
            "id": 2,
            "first_name": "islam",
            "last_name": "islamkz",
            "email": "islam@gmail.com",
            "created": "2021-01-01",
            "status": "completed",
        },
    ]


@pytest.fixture()
def postgres_container() -> PostgresContainer:
    container = PostgresContainer()
    container.start()
    return container


@pytest.fixture()
def postgres_url(postgres_container: PostgresContainer) -> str:
    engine = create_engine(postgres_container.get_connection_url())
    conn = engine.connect()

    create_table_users(conn)
    return postgres_container.get_connection_url()


@pytest.fixture()
def postgres_url_with_data(postgres_container: PostgresContainer, fetch_users) -> str:
    engine = create_engine(postgres_container.get_connection_url())
    conn = engine.connect()

    create_table_users(conn)

    for user in fetch_users:
        insert_user(
            conn,
            User(
                first_name=user["first_name"],
                last_name=user["last_name"],
                email=user["email"],
                created=user["created"],
                status=user["status"],
            ),
        )

    return postgres_container.get_connection_url()
