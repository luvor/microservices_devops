import time
from common.sql_queries import create_table_users, complete_user

create_table_users()

if __name__ == '__main__':
    while True:
        complete_user()
        print("completed")
        time.sleep(1)
