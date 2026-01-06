#
# import sqlite3
#
# from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
#
# import os
#
# class DatabaseClients:
#     def __init__(self, db_name="clients.db"):
#         self.conn = sqlite3.connect(db_name, check_same_thread=False)
#         self.cursor = self.conn.cursor()
#         self.create_table()
#
# # Создаём базу, если её нет
# if not os.path.exists(DB_FILE):
#     conn = sqlite3.connect(DB_FILE)
#     c = conn.cursor()
#     c.execute(
#     conn.commit()
#     conn.close()


class Backend(QObject):
    clients_updated = pyqtSignal(list)


