import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://flowersearch.weebly.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Google', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        
        home_btn = QAction('DuckDuckGo', self)
        home_btn.triggered.connect(self.navigate_DuckDuckGo)
        navbar.addAction(home_btn)

        home_btn = QAction('Bing', self)
        home_btn.triggered.connect(self.navigate_Bing)
        navbar.addAction(home_btn)

        home_btn = QAction('Kiddle', self)
        home_btn.triggered.connect(self.navigate_Kiddle)
        navbar.addAction(home_btn)
        
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com'))

    def navigate_DuckDuckGo(self):
        self.browser.setUrl(QUrl('https://duckduckgo.com/'))
    
    def navigate_Bing(self):
        self.browser.setUrl(QUrl('https://www.bing.com/?FORM=Z9FD1'))

    def navigate_Kiddle(self):
        self.browser.setUrl(QUrl('https://www.kiddle.co/'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Flame')
window = MainWindow()
app.exec_()