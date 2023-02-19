import time
from common.sql_queries import create_table_users, get_users

create_table_users()

if __name__ == '__main__':
    while True:
        users = get_users()
        print("-------------------- >>")
        for user in users:
            print(user)
        print("-------------------- <<")
        time.sleep(5)
