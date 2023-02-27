import time
from common.sql_queries import create_table_users, complete_user
from common.db import conn

create_table_users(conn)

if __name__ == "__main__":
    while True:
        complete_user(conn)
        print("completed")
        time.sleep(1)
