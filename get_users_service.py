import time
from common.sql_queries import create_table_users, get_users

from common.db import conn

create_table_users(conn)

if __name__ == "__main__":
    while True:
        users = get_users(conn)
        print("-------------------- >>")
        for user in users:
            print(user)
        print("-------------------- <<")
        time.sleep(5)
