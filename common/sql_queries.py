from models.User import User

from sqlalchemy.engine import Connection
from sqlalchemy import text


def create_table_users(conn: Connection):
    query = """
    CREATE TABLE IF NOT EXISTS islambek_users (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        created DATE DEFAULT NOW(),
        status VARCHAR(255) DEFAULT 'new'
        )
    """

    conn.execute(text(query))
    conn.commit()


def insert_user(conn: Connection, user: User):
    query = """
    INSERT INTO islambek_users (first_name, last_name, email, created, status)
    VALUES (:first_name, :last_name, :email, :created, :status)
    """

    conn.execute(
        text(query),
        parameters={
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "created": user.created,
            "status": user.status,
        },
    )
    conn.commit()


def update_user(conn: Connection):
    query = "UPDATE islambek_users SET status='calculated' WHERE status='new';"
    conn.execute(text(query))
    conn.commit()


def complete_user(conn: Connection):
    query = "UPDATE islambek_users SET status='completed';"
    conn.execute(text(query))
    conn.commit()


def get_users(conn: Connection) -> list[User]:
    query = "SELECT * FROM islambek_users;"
    users = conn.execute(text(query)).fetchall()
    return [
        User(
            id=user[0],
            first_name=user[1],
            last_name=user[2],
            email=user[3],
            created=user[4],
            status=user[5],
        )
        for user in users
    ]
