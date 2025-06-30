import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class YouTubeBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Viewer")
        self.setGeometry(100, 100, 1200, 800)

        self.web_view = QWebEngineView()
        self.web_view.setUrl(QUrl("https://www.youtube.com"))

        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.web_view)
        container.setLayout(layout)
        self.setCentralWidget(container)


def main():
    app = QApplication(sys.argv)
    browser = YouTubeBrowser()
    browser.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
