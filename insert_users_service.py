import time
import random
from common.sql_queries import create_table_users, insert_user
from models.User import User

create_table_users()

if __name__ == '__main__':
    while True:
        insert_user(
            User(
                first_name=random.choice(["islambek", "islam", "islamkz"]),
                last_name=random.choice(["islambek", "islam", "islamkz"]),
                email=random.choice(["islambek", "islam", "islamkz"]) + "@gmail.com",
                created="2021-01-01",
                status="new"
            )
        )
        print("Inserted")
        # time.sleep(10)
