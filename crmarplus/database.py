import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name="clients.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            car TEXT,
            plate TEXT,
            comment TEXT,
            created TEXT
        )
        """)
        self.conn.commit()

    def load_clients(self):
        self.cursor.execute("SELECT id, name, phone, car, plate, comment, created FROM clients ORDER BY id DESC")
        clients = self.cursor.fetchall()  # получаем данные
        return clients

    def add_client(self, name, phone, car, plate, comment):
        created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute(
            "INSERT INTO clients (name, phone, car, plate, comment, created) VALUES (?, ?, ?, ?, ?, ?)",
            (name, phone, car, plate, comment, created)
        )
        self.conn.commit()
        self.load_clients()

    def edit_client(self, client_id, name, phone, car, plate, comment):
        self.cursor.execute(
            "UPDATE clients SET name=?, phone=?, car=?, plate=?, comment=? WHERE id=?",
            (name, phone, car, plate, comment, client_id)
        )
        self.conn.commit()
        self.load_clients()

    def delete_client(self, client_id):
        self.cursor.execute("DELETE FROM clients WHERE id=?", (client_id,))
        self.conn.commit()
        self.load_clients()
