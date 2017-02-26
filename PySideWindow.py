import PySide
import platform
import GoogleLogin
import AnimeProvider
from YouTubeProvider import YTProvider

from PySide.QtGui import *
from PySide.QtWebKit import QWebView, QWebSettings
from AnimeSTProviderUI import Ui_MainWindow
import AnimeSTProviderUI as Ui

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect_buttons()
        self.connect_menus()
        self.connect_events()
        self.setWindowIcon(QIcon("assets/icon.png"))
        self.loggedIn = False
        self.currentPlaylistRow = 0
        self.currentAnimeRow = 0

    def connect_buttons(self):
        self.closeBtn = QPushButton()
        self.tab1DeleteAnimeBtn.clicked.connect(self.delete_anime)
        self.tab1AddAnimeBtn.clicked.connect(self.add_anime)
        self.tab1SearchYTBtn.clicked.connect(self.search)
        self.tab0AddPlaylistBtn.clicked.connect(self.create_playlist)
        self.tab1AddPlaylistBtn.clicked.connect(self.create_playlist)
        self.tab0DeletePlaylistBtn.clicked.connect(self.delete_playlist)
        self.tab0LoadPlaylistBtn.clicked.connect(self.load_playlist)
        self.closeBtn.clicked.connect(self.destroy_preview)

    def connect_menus(self):
        self.actionOpen_HTML.triggered.connect(self.open_HTML)
        self.actionAbout.triggered.connect(self.show_about)
        self.actionLog_In.triggered.connect(self.log_in)

    def connect_events(self):
        self.tab0UserPlaylistsList.itemClicked.connect(
            self.on_playlist_row_changed)
        self.tab1UserPlaylistsList.itemClicked.connect(
            self.on_playlist_row_changed)
        self.tab1AnimesList.itemClicked.connect(
            self.on_anime_row_changed)

    def load_playlist(self):
        self.videos = self.ytProvider.load_playlist(
            self.playlists[self.currentPlaylistRow].id)
        self.list_video_items()
        self.statusBar().showMessage('Playlist loaded!')

    def list_video_items(self):
        container = self.tab0RightContainerWidget.layout()
        self.clear_layout(container)
        for video in self.videos:
            container.addWidget(Ui.VideoItem(video=video))

    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):
            widget = layout.itemAt( i ).widget()
            layout.removeWidget(widget)
            widget.setParent(None)

    def initialize_preview(self):
        #TODO
        self.previewWindow.setWindowFlags(Qt.FramelessWindowHint)
        self.previewWindow.setWindowTitle("Preview")
        self.layout = QVBoxLayout()
        self.previewWindow.setLayout(self.layout)
        self.webView.settings().setAttribute(QWebSettings.PluginsEnabled, True)
        self.closeBtn.setText("Close")
        self.layout.addWidget(self.webView)
        self.layout.addWidget(self.closeBtn)

    def open_HTML(self):
        fname, str = QFileDialog.getOpenFileName(self, 'Open file', '/home/Desktop', "Files (*.html)")
        if fname != '':
            animeNames = AnimeProvider.get_anime_from_file(fname)
            for anime in animeNames:
                self.tab1AnimesList.addItem(anime)
            self.statusBar().showMessage('File successfully loaded from HTML!')

    def list_playlists(self):
        self.tab0UserPlaylistsList.clear()
        self.tab1UserPlaylistsList.clear()

        self.playlists = self.ytProvider.get_user_playlists()

        for i in range(0, len(self.playlists)):
            title = self.playlists[i].title
            self.tab0UserPlaylistsList.addItem(title)
            self.tab1UserPlaylistsList.addItem(title)

    def create_playlist(self):
        name, ok = QInputDialog.getText(self, 'Add playlist', 'Enter playlist name: ')
        if ok:
            self.ytProvider.create_playlist(name)
            self.tab0UserPlaylistsList.addItem(name)
            self.tab1UserPlaylistsList.addItem(name)

    def delete_playlist(self):
        if self.tab0UserPlaylistsList.item(self.currentPlaylistRow) is not None:
            reply = QMessageBox.question(self, 'Are you sure?', "Are you sure?",
                QMessageBox.Yes,
                QMessageBox.No,
                QMessageBox.No
                )
            if reply == QMessageBox.Yes:
                self.ytProvider.delete_playlist(self.playlists[self.currentPlaylistRow].id)
                self.tab0UserPlaylistsList.takeItem(self.currentPlaylistRow)
                self.tab1UserPlaylistsList.takeItem(self.currentPlaylistRow)
        else:
            self.show_error("You must log in first or you have no playlists.")

    def add_video_to_playlist(self):
        #TODO
        if len(self.videoIds) > 0:
            # buttons' names end in a number from 0 to 5 then we can use that number as an index for array
            senderId = self.sender().objectName()[-1:]
            videoId = self.videos[int(senderId)]
            playlistId = self.playlistIds[self.currentPlaylistRow]
            self.ytProvider.add_to_playlist(videoId, playlistId)

    def delete_video_from_playlist(self):
        #TODO
        if len(self.playlistVideoIds) > 0:
            # buttons' names end in a number from 0 to 5 then we can use that number as an index for array
            senderId = self.sender().objectName()[-1:]
            self.ytProvider.delete_from_playlist(self.playlistVideoIds[int(senderId)])
            self.load_playlist()

    def log_in(self):
        login = GoogleLogin.log_in()
        self.ytProvider = YTProvider(login)
        self.statusBar().showMessage('Logged in!')
        self.list_playlists()

    def delete_anime(self):
        self.tab1AnimesList.takeItem(self.currentAnimeRow)

    def add_anime(self):
        title, ok = QInputDialog.getText(self, 'Add anime', 'Enter anime title:')
        if ok:
            self.tab1AnimesList.addItem(title)

    def search(self):
        #TODO
        if self.tab1AnimesList.item(self.currentAnimeRow) is not None:
            self.videoTitles, self.videoThumbnails, self.videoIds, self.videoUrlIds = self.ytProvider.youtube_search(
                self.tab1AnimesList.item(self.currentAnimeRow).text(),
                self.addTextLabel.text())
            self.statusBar().showMessage('Search done!')
        else:
            self.show_error("You must choose an anime first!")

    def preview(self):
        #TODO
        sender = self.sender().objectName()
        # If sender object's name starts with "video" we know that it comes from YT tab, not playlist
        if sender[:5] == "video":
            if len(self.videoUrlIds) > 0:
                # We can use number at the end of sender object's name as an index for arrays but we must take page number into account
                index = int(sender[-1:]) + self.currentVideoPage * 6
                id = self.videoUrlIds[index]
            else:
                return
        else:
            if len(self.playlistVideoUrlIds) > 0:
                index = int(sender[-1:]) + self.currentPlaylistPage * 6
                id = self.playlistVideoUrlIds[index]
            else:
                return

        self.url = "http://www.youtube.com/embed/{}".format(id)
        s = """<!DOCTYPE html>
                <html>
                <body>
                <iframe id="ytplayer" type="text/html" width="640" height="390" src="{}" frameborder="0"/>
                </body>
                </html>""".format(self.url)
        self.webView.setHtml(s)
        self.previewWindow.show()

    def destroy_preview(self):
        self.webView.load("")
        self.previewWindow.hide()

    def show_about(self):
        QMessageBox.about(self, "About AnimeSTProvider",
            """<p>Developed by Jan Kominczyk (BlinkBP).
            <p>Python {} - PySide version {} - Qt version {}"""
            .format(platform.python_version(),
                PySide.__version__,
                PySide.QtCore.__version__,
                )
            )

    def show_error(self, text):
        self.message = QMessageBox()
        self.message.setWindowTitle("Error")
        self.message.setText(text)
        self.message.setDefaultButton(QMessageBox.Ok)
        self.message.open()

    def on_playlist_row_changed(self, item):
        self.currentPlaylistRow = self.sender().row(item)

    def on_anime_row_changed(self, item):
        self.currentAnimeRow = self.sender().row(item)
