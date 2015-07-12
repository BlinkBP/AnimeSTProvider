import PySide
from PySide.QtGui import *
from PySide.QtCore import *
from AnimeSTProviderUI import Ui_MainWindow
import platform
import GoogleLogin
import AnimeProvider
import YouTubeProvider

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Scenes
        self.scenes = [QGraphicsScene(), QGraphicsScene(), QGraphicsScene(),
		               QGraphicsScene(), QGraphicsScene(), QGraphicsScene()]
        # Menu
        self.actionOpen_HTML.triggered.connect(self.open_HTML)
        self.actionAbout.triggered.connect(self.show_about)
        self.actionLoad_JSON_auth_file.triggered.connect(self.log_in)
        # Buttons
        self.deleteAnimeBtn.clicked.connect(self.delete_anime)
        self.addAnimeBtn.clicked.connect(self.add_anime)
        self.searchYTBtn.clicked.connect(self.search)

    def open_HTML(self):
        fname, str = QFileDialog.getOpenFileName(self, 'Open file', '/home/Desktop', "Files (*.html)")
        if fname != '':
            animeNames = AnimeProvider.get_anime_from_file(fname)
            for anime in animeNames:
                self.animeListWidget.addItem(anime)
            self.statusBar().showMessage('File successfully loaded from HTML')

    def log_in(self):
        json, str = QFileDialog.getOpenFileName(self, 'Open JSON file', '/home/Desktop', "Files (*.JSON)")
        if json != '':
            GoogleLogin.json_log_in(json)

    def delete_anime(self):
        self.animeListWidget.takeItem(self.animeListWidget.currentRow())

    def add_anime(self):
        title, ok = QInputDialog.getText(self, 'Add anime', 'Enter anime title:')

        if ok:
            self.animeListWidget.addItem(title)

    def search(self):
        YouTubeProvider.youtube_search(self.animeListWidget.selectedItems()[0].text(), 6)
        
    def show_about(self):
        QMessageBox.about(self, "About AnimeSTProvider",
                          """<p>Copyright &copy; 2015 Jan Kominczyk.
                          <p>Python {} - PySide version {} - Qt version {}""".format(platform.python_version(),
                                                                                     PySide.__version__,
                                                                                     PySide.QtCore.__version__, )
                          )