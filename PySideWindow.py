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
        #Scenes
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
        self.addPlaylistBtn.clicked.connect(self.create_playlist)
        self.deletePlaylistBtn.clicked.connect(self.delete_playlist)
        self.loadPlaylistBtn.clicked.connect(self.load_playlist)
        #Variables
        self.playlistIds = []
        self.currentPlaylistRow = 0
        self.currentAnimeRow = 0
        #Events
        self.userPlaylistsList0.itemClicked.connect(self.on_playlist_row_changed)
        self.animeListWidget.itemClicked.connect(self.on_anime_row_changed)

    def open_HTML(self):
        fname, str = QFileDialog.getOpenFileName(self, 'Open file', '/home/Desktop', "Files (*.html)")
        if fname != '':
            animeNames = AnimeProvider.get_anime_from_file(fname)
            for anime in animeNames:
                self.animeListWidget.addItem(anime)
            self.statusBar().showMessage('File successfully loaded from HTML')

    def list_playlists(self):

        self.userPlaylistsList0.clear()
        self.userPlaylistsList1.clear()

        titles, self.playlistIds = YouTubeProvider.get_user_playlists()

        for title in titles:
            self.userPlaylistsList0.addItem(title)
            self.userPlaylistsList1.addItem(title)

    def load_playlist(self):
        YouTubeProvider.load_playlist(self.playlistIds[self.currentPlaylistRow])

    def create_playlist(self):
        
        name, ok = QInputDialog.getText(self, 'Add playlist', 'Enter playlist name: ')

        if ok:
            YouTubeProvider.create_playlist(name)
            self.userPlaylistsList0.addItem(name)
            self.userPlaylistsList1.addItem(name)

    def delete_playlist(self):

        YouTubeProvider.delete_playlist(self.playlistIds[self.currentPlaylistRow])
        self.userPlaylistsList0.takeItem(self.currentPlaylistRow)
        self.userPlaylistsList1.takeItem(self.currentPlaylistRow)

    def log_in(self):
        json, str = QFileDialog.getOpenFileName(self, 'Open JSON file', '/home/Desktop', "Files (*.JSON)")
        if json != '':
            GoogleLogin.json_log_in(json)
            self.list_playlists()

    def delete_anime(self):
        self.animeListWidget.takeItem(self.animeListWidget.currentRow())

    def add_anime(self):
        title, ok = QInputDialog.getText(self, 'Add anime', 'Enter anime title:')

        if ok:
            self.animeListWidget.addItem(title)

    def search(self):
        YouTubeProvider.youtube_search(self.animeListWidget.item(self.currentAnimeRow).text(), 6)

    def show_about(self):
        QMessageBox.about(self, "About AnimeSTProvider",
                          """<p>Copyright &copy; 2015 Jan Kominczyk.
                          <p>Python {} - PySide version {} - Qt version {}""".format(platform.python_version(),
                                                                                     PySide.__version__,
                                                                                     PySide.QtCore.__version__, )
                          )

    def on_playlist_row_changed(self, item):
        currentPlaylistRow = self.userPlaylistsList0.row(item)

    def on_anime_row_changed(self, item):
        currentAnimeRow = self.animeListWidget.row(item)