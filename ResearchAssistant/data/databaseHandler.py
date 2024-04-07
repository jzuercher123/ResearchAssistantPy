import sqlite3

class DBHandler:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        columns_str = ', '.join([f'{name} {type}' for name, type in columns.items()])
        self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})')

    def insert_data(self, table_name, data):
        placeholders = ', '.join(['?' for _ in data[0]])
        self.cursor.executemany(f'INSERT INTO {table_name} VALUES ({placeholders})', data)
        self.conn.commit()

    def query_data(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()


