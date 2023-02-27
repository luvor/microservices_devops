import time
from common.sql_queries import create_table_users, get_users
from common.db import conn

create_table_users(conn)


def send_push_notification(title: str, link: str, user_id: int):
    print("Sended push notification to {} with title {}".format(user_id, title))


if __name__ == "__main__":
    while True:
        users = get_users(conn)
        for user in users:
            send_push_notification("Hi", "google.com", user.id)
        time.sleep(1440)
