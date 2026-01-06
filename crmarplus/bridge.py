from database import Database
import json
import os

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, QUrl

class Bridge(QObject):
    clients_updated = pyqtSignal(list)
    def __init__(self, view):
        super().__init__()
        self.view = view
        self.database = Database


    @pyqtSlot()
    def load_clients(self):
        clients = self.database.load_clients()
        # Отправляем в JS через сигнал
        self.clients_updated.emit(clients)

    @pyqtSlot(str, str, str, str, str)
    def add_client(self, name, phone, car, plate, comment):
        self.database.add_client(name, phone, car, plate, comment)
        self.load_clients()

    @pyqtSlot(int, str, str, str, str, str)
    def edit_client(self, client_id, name, phone, car, plate, comment):
        self.database.edit_client(client_id, name, phone, car, plate, comment)
        self.load_clients()

    @pyqtSlot(int)
    def delete_client(self, client_id):
        self.database.delete_client(client_id)
        self.load_clients()




    @pyqtSlot(str)
    def open_page(self, page):
        pages = {
            "main": "ui_main.html",
            "clients": "ui.html",
            "missing": "ui_clients.html"
        }

        if page in pages:
            path = os.path.abspath(pages[page])
            self.view.load(QUrl.fromLocalFile(path))

    # @pyqtSlot(str,str,str,str,str)
    # def add_client(self, name,phone,car,plate,comment):
    #     self.database.add_client(name,phone,car,plate,comment)
    #     self.load_clients()
    #
    # @pyqtSlot(int,str,str,str,str,str)
    # def edit_client(self, id,name,phone,car,plate,comment):
    #     self.database.edit_client(id,name,phone,car,plate,comment)
    #     self.load_clients()
    #
    # @pyqtSlot(int)
    # def delete_client(self, id):
    #     self.database.delete_client(id)
    #     self.load_clients()
    #
    # def load_clients(self):
    #     clients = self.database.get_clients()
    #     # Преобразуем в JSON строку
    #     clients_json = json.dumps(clients)
    #     self.view.page().runJavaScript(f"updateTable({json.dumps(clients)})")







