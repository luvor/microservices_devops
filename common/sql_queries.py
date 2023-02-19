
from models.User import User
from common.db import conn


def create_table_users():
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

    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def insert_user(user: User):
    query = """
    INSERT INTO islambek_users (first_name, last_name, email, created, status)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor = conn.cursor()
    cursor.execute(query, (user.first_name, user.last_name, user.email, user.created, user.status))
    conn.commit()


def update_user():
    query = "UPDATE islambek_users SET status='calculated' WHERE status='new';"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def complete_user():
    query = "UPDATE islambek_users SET status='completed' WHERE status='calculated';"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def get_users() -> list[User]:
    query = "SELECT * FROM islambek_users;"
    cursor = conn.cursor()
    cursor.execute(query)
    return [User(
        id=user[0],
        first_name=user[1],
        last_name=user[2],
        email=user[3],
        created=user[4],
        status=user[5],
    ) for user in cursor.fetchall()]
