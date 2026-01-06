# import sqlite3
#
# class Database:
#     def __init__(self, db_name="crm.db"):
#         self.conn = sqlite3.connect(db_name, check_same_thread=False)
#         self.cursor = self.conn.cursor()
#         self.create_table()
#
#     def create_table(self):
#         self.cursor.execute("""
#         CREATE TABLE IF NOT EXISTS clients (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             email TEXT,
#             phone TEXT
#         )
#         """)
#         self.conn.commit()
#
#     def add_client(self, name, email, phone):
#         self.cursor.execute("INSERT INTO clients (name,email,phone) VALUES (?,?,?)", (name,email,phone))
#         self.conn.commit()
#
#     def edit_client(self, cid, name, email, phone):
#         self.cursor.execute("UPDATE clients SET name=?, email=?, phone=? WHERE id=?", (name,email,phone,cid))
#         self.conn.commit()
#
#     def delete_client(self, cid):
#         self.cursor.execute("DELETE FROM clients WHERE id=?", (cid,))
#         self.conn.commit()
#
#     def get_clients(self):
#         self.cursor.execute("SELECT * FROM clients")
#         return self.cursor.fetchall()
#
#
#
#
#
