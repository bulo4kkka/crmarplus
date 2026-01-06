import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel
from bridge import Bridge
from PyQt5.QtCore import QUrl

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Профессиональная CRM")
    window.setGeometry(100, 100, 800, 500)

    layout = QVBoxLayout()
    window.setLayout(layout)

    view = QWebEngineView()

    # Читаем HTML
    html_file = "ui_main.html"

    # Абсолютный путь к папке с HTML
    base_path = os.path.dirname(os.path.abspath(html_file))
    base_url = QUrl.fromLocalFile(base_path + "/")  # базовый URL для относительных путей

    main_html = os.path.abspath("ui_main.html")
    view.load(QUrl.fromLocalFile(main_html))


    layout.addWidget(view)

    # Настраиваем WebChannel
    bridge = Bridge(view)
    channel = QWebChannel()
    channel.registerObject("pywebchannel", bridge)
    view.page().setWebChannel(channel)

    window.show()
    sys.exit(app.exec_())
