from PyQt5.QtWidgets import (QMainWindow, QAction,
                             QFileDialog, QApplication,
                             QDesktopWidget, QLineEdit,
                             QInputDialog, QPushButton,
                             QHBoxLayout, QVBoxLayout, QWidget)
from PyQt5.QtGui import QIcon
import AnimeProvider


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        
        self.DrawMenuBar()
        
        foo = QLineEdit(self)
        
        emailField = QLineEdit(self)
        email = emailField.text()

        passwordField = QLineEdit(self)
        passwordField.setEchoMode(2)
        password = passwordField.text()

        loginBtn = QPushButton('Login')

        vBox1 = QVBoxLayout()
        vBox1.addStretch(1)
        vBox1.addWidget(emailField)
        vBox1.addWidget(passwordField)
        vBox1.addWidget(loginBtn)
        vBox2 = QVBoxLayout()
        vBox2.addStretch(1)
        vBox2.addWidget(foo)
        hBox = QHBoxLayout()
        hBox.addLayout(vBox1)
        hBox.addSpacing(50)
        hBox.addLayout(vBox2, 1)
        
        widget = QWidget(self)
        widget.setLayout(hBox)
        self.setCentralWidget(widget)

        self.setFixedSize(800, 450)
        self.center()
        self.setWindowTitle('AnimeSTProvider')
        self.show()

    def show_file_dialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/')
        if (fname != ('', '')):
            animeNames = AnimeProvider.GetAnimeFromFile(fname[0])
            self.statusBar().showMessage('File loaded')
            print(animeNames)
    
    def draw_menu_bar(self):
        openFile = QAction(QIcon('open.png'), 'Open file', self)
        openFile.setStatusTip('Open HTML with AnimeList')
        openFile.triggered.connect(self.ShowFileDialog)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
    
    def center(self):
        frame = self.frameGeometry()
        screenSize = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(screenSize)
        self.move(frame.topLeft())
