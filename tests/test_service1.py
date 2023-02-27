from sqlalchemy import create_engine

from common.sql_queries import insert_user, create_table_users, get_users
from models.User import User

import datetime


def test_service1_insert_users(postgres_url: str):
    engine = create_engine(postgres_url)
    conn = engine.connect()

    # create_table_users(conn)

    insert_user(
        conn,
        User(
            first_name="islambek",
            last_name="islamkz",
            email="islamkz@gmail.com",
            created="2021-01-01",
            status="new",
        ),
    )
    engine.dispose(postgres_url)


def test_service1_get_users(postgres_url_with_data: str):
    engine = create_engine(postgres_url_with_data)
    conn = engine.connect()

    users = get_users(conn)

    assert len(users) == 2
    assert users[0].id == 1
    assert users[0].first_name == "islam"
    assert users[0].last_name == "islamkz"
    assert users[0].email == "islamkz@gmail.com"
    assert users[0].created == datetime.date(2021, 1, 1)
    assert users[0].status == "completed"

    engine.dispose(postgres_url_with_data)
