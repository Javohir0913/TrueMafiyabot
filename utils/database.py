import sqlite3


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_user(self, f_name, tg_id):
        try:
            self.cursor.execute("INSERT INTO users (f_name, tg_id) VALUES (?, ?);", (f_name, tg_id))
            self.conn.commit()
            return True
        except:
            return False

    def get_user(self, tg_id):
        users = self.cursor.execute('SELECT * FROM users WHERE tg_id=?', (tg_id,))
        return users.fetchone()

    def all_users(self):
        users = self.cursor.execute('SELECT * FROM users', )
        return users.fetchall()

    # ---------------------------------- O'yin uchun ----------------------------
    def create_table(self, table_name):
        try:
            self.cursor.execute(
                f'CREATE TABLE {table_name} (id INTEGER PRIMARY KEY, name TEXT NOT NULL, holat BOOL NOT NULL);')
            self.conn.commit()
            return True
        except:
            return False

    def add_users_game(self, tg_id, name, table_name):
        try:
            query = f"INSERT INTO {table_name} (id, name, holat) VALUES (?, ?, True)"
            self.cursor.execute(query, (tg_id, name))
            self.conn.commit()
        except Exception as e:
            print(f"Error adding user game: {e}")
            return False
        return True

    def get_users_game(self, table_name):
        try:
            query = f"SELECT * FROM {table_name}"
            self.cursor.execute(query)
            users = self.cursor.fetchall()
            return users if users else False
        except Exception as e:
            print(f"Error getting user game: {e}")
            return False

    def get_user_game(self, tg_id, table_name):
        try:
            query = f"SELECT * FROM {table_name} WHERE id = ?"
            self.cursor.execute(query, (tg_id,))
            user = self.cursor.fetchone()
            return user if user else False
        except Exception as e:
            print(f"Error getting user game: {e}")
            return False

    def delete_table(self, table_name):
        self.cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        self.conn.commit()

#  ------------------------------------------ end ------------------------------------
