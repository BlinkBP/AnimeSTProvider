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
        self.connectButtons()
        self.connectMenus()
        self.connectEvents()
        self.setWindowIcon(QIcon("assets/icon.png"))
        self.loggedIn = False
        self.currentPlaylistRow = 0
        self.currentAnimeRow = 0
        self.ytProvider = YTProvider()

    def connectButtons(self):
        self.closeBtn = QPushButton()
        self.tab1DeleteAnimeBtn.clicked.connect(self.delete_anime)
        self.tab1AddAnimeBtn.clicked.connect(self.add_anime)
        self.tab1SearchYTBtn.clicked.connect(self.search)
        self.tab0AddPlaylistBtn.clicked.connect(self.create_playlist)
        self.tab1AddPlaylistBtn.clicked.connect(self.create_playlist)
        self.tab0DeletePlaylistBtn.clicked.connect(self.delete_playlist)
        self.tab0LoadPlaylistBtn.clicked.connect(self.load_playlist)
        self.closeBtn.clicked.connect(self.destroy_preview)

    def connectMenus(self):
        self.actionOpen_HTML.triggered.connect(self.open_HTML)
        self.actionAbout.triggered.connect(self.show_about)
        self.actionLoad_JSON_auth_file.triggered.connect(self.log_in)

    def connectEvents(self):
        self.tab0UserPlaylistsList.itemClicked.connect(
            self.on_playlist_row_changed)
        self.tab1UserPlaylistsList.itemClicked.connect(
            self.on_playlist_row_changed)
        self.tab1AnimesList.itemClicked.connect(
            self.on_anime_row_changed)

    def load_playlist(self):
        if (self.loggedIn):
            #videos entry is [title, thumb_url, id, url]
            self.videos = self.ytProvider.load_playlist(
                self.playlistIds[self.currentPlaylistRow])
            self.loadVideosList()
            self.statusBar().showMessage('Playlist loaded!')
        else:
            self.showError("You must log in first!")

    def loadVideosList(self):
        if (self.tab.currentIndex() == 0):
            container = self.tab0RightContainerWidget.layout()
            for video in videos:
                container.addWidget(Ui.VideoItem(video))

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
        self.tab0userPlaylistsList.clear()
        self.tab1userPlaylistsList.clear()

        titles, self.playlistIds = self.ytProvider.get_user_playlists()

        for title in titles:
            self.userPlaylistsList0.addItem(title)
            self.userPlaylistsList1.addItem(title)

    def create_playlist(self):
        if self.ytProvider.login is not None:
            name, ok = QInputDialog.getText(self, 'Add playlist', 'Enter playlist name: ')

            if ok:
                self.ytProvider.create_playlist(name)
                self.userPlaylistsList0.addItem(name)
                self.userPlaylistsList1.addItem(name)
        else:
            self.showError("You must log in first!")

    def delete_playlist(self):
        if self.userPlaylistsList0.item(self.currentPlaylistRow) is not None:
            reply = QMessageBox.question(self, 'Are you sure?', "Are you sure?",
                QMessageBox.Yes,
                QMessageBox.No,
                QMessageBox.No
                )
            if reply == QMessageBox.Yes:
                self.ytProvider.delete_playlist(self.playlistIds[self.currentPlaylistRow])
                self.userPlaylistsList0.takeItem(self.currentPlaylistRow)
                self.userPlaylistsList1.takeItem(self.currentPlaylistRow)
        else:
            self.message = QMessageBox()
            self.message.setWindowTitle("Error")
            self.message.setText("You must log in first or you have no playlists.")
            self.message.setDefaultButton(QMessageBox.Ok)
            self.message.open()

    def add_video_to_playlist(self):
        if len(self.videoIds) > 0:
            # buttons' names end in a number from 0 to 5 then we can use that number as an index for array
            senderId = self.sender().objectName()[-1:]

            videoId = self.videoIds[int(senderId)]
            playlistId = self.playlistIds[self.currentPlaylistRow]

            self.ytProvider.add_to_playlist(videoId, playlistId)

    def delete_video_from_playlist(self):
        if len(self.playlistVideoIds) > 0:
            # buttons' names end in a number from 0 to 5 then we can use that number as an index for array
            senderId = self.sender().objectName()[-1:]

            self.ytProvider.delete_from_playlist(self.playlistVideoIds[int(senderId)])
            self.load_playlist()

    def log_in(self):
        json, str = QFileDialog.getOpenFileName(self, 'Open JSON file', '/home/Desktop', "Files (*.JSON)")
        if json != '':
            GoogleLogin.json_log_in(json)
            self.statusBar().showMessage('Logged in!')
            self.list_playlists()

    def delete_anime(self):
        self.tab1AnimesList.takeItem(self.tab1AnimesList.currentRow())

    def add_anime(self):
        title, ok = QInputDialog.getText(self, 'Add anime', 'Enter anime title:')
        if ok:
            self.tab1AnimesList.addItem(title)

    def search(self):
        if self.tab1AnimesList.item(self.currentAnimeRow) is not None:
            if self.ytProvider.login is not None:
                self.videoTitles, self.videoThumbnails, self.videoIds, self.videoUrlIds = self.ytProvider.youtube_search(
                    self.tab1AnimesList.item(self.currentAnimeRow).text(),
                    self.addTextLabel.text())
                self.fill_thumbnails(self.videoThumbnails, "anime")
                self.fill_labels(self.videoTitles, "anime")
                self.update_page_label("anime")
                self.statusBar().showMessage('Search done!')
            else:
                self.showError("You must log in first!")
        else:
            self.showError("You must choose an anime first!")

    def preview(self):
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

    def showError(self, text):
        self.message = QMessageBox()
        self.message.setWindowTitle("Error")
        self.message.setText(text)
        self.message.setDefaultButton(QMessageBox.Ok)
        self.message.open()


    def on_playlist_row_changed(self, item):
        if self.sender().objectName() == "userPlaylistsList0":
            self.currentPlaylistRow = self.userPlaylistsList0.row(item)
        elif self.sender().objectName() == "userPlaylistsList1":
            self.currentPlaylistRow = self.userPlaylistsList1.row(item)

    def on_anime_row_changed(self, item):
        self.currentAnimeRow = self.tab1AnimesList.row(item)
