import PySide
import requests
from PIL import Image
from PIL import ImageQt
import platform
import GoogleLogin
import AnimeProvider
import YouTubeProvider

from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtWebKit import QWebView, QWebSettings
from AnimeSTProviderUI import Ui_MainWindow
from io import BytesIO

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # # Menu
        # self.actionOpen_HTML.triggered.connect(self.open_HTML)
        # self.actionAbout.triggered.connect(self.show_about)
        # self.actionLoad_JSON_auth_file.triggered.connect(self.log_in)
        # # Buttons
        # self.closeBtn = QPushButton()
        # self.tab1deleteAnimeBtn.clicked.connect(self.delete_anime)
        # self.tab1addAnimeBtn.clicked.connect(self.add_anime)
        # self.tab1searchYTBtn.clicked.connect(self.search)
        # self.tab0addPlaylistBtn.clicked.connect(self.create_playlist)
        # self.tab1addPlaylistBtn.clicked.connect(self.create_playlist)
        # self.tab0deletePlaylistBtn.clicked.connect(self.delete_playlist)
        # self.tab0loadPlaylistBtn.clicked.connect(self.load_playlist)
        # self.tab0nextPageBtn.clicked.connect(self.nextPage)
        # self.tab1nextPageBtn.clicked.connect(self.nextPage)
        # self.tab0previousPageBtn.clicked.connect(self.previousPage)
        # self.tab1previousPageBtn.clicked.connect(self.previousPage)
        # self.closeBtn.clicked.connect(self.destroy_preview)
        # #Variables
        # self.playlistIds = []
        # self.playlistVideoUrlIds = []
        # self.playlistVideoIds = []
        # self.playlistVideoTitles = []
        # self.playlistVideoThumbnails = []
        # self.videoUrlIds = []
        # self.videoIds = []
        # self.videoTitles = []
        # self.videoThumbnails = []
        # self.currentPlaylistRow = 0
        # self.currentAnimeRow = 0
        # self.totalVideoPages = 0
        # self.totalPlaylistPages = 0
        # self.currentVideoPage = 0
        # self.currentPlaylistPage = 0
        # #Events
        # self.tab0userPlaylistsList.itemClicked.connect(self.on_playlist_row_changed)
        # self.tab1userPlaylistsList.itemClicked.connect(self.on_playlist_row_changed)
        # self.tab1animesList.itemClicked.connect(self.on_anime_row_changed)
        # #Icons
        # self.icon = QIcon("assets/icon.png")
        # #Misc
        # self.previewWindow = QWidget()
        # self.webView = QWebView()
        #
        # self.setWindowIcon(self.icon)

    def initialize_preview(self):
        self.previewWindow.setWindowFlags(Qt.FramelessWindowHint)
        #self.previewWindow.setFixedSize(685,470)
        self.previewWindow.setWindowTitle("Preview")
        self.layout = QVBoxLayout()
        self.previewWindow.setLayout(self.layout)
        self.webView.settings().setAttribute(QWebSettings.PluginsEnabled, True)
        self.closeBtn.setText("Close")
        self.layout.addWidget(self.webView)
        self.layout.addWidget(self.closeBtn)

    def fill_thumbnails(self, thumbnails, tab):
        if tab == "anime":
            views = self.animeViews
            scenes = self.animeScenes
        elif tab == "playlist":
            views = self.videoViews
            scenes = self.videoScenes

        self.clear_thumbnails(tab)

        if len(thumbnails) > 6:
            maxIndex = 6
        else:
            maxIndex = len(thumbnails)

        for i in range(0, maxIndex):
            data = requests.get(thumbnails[i]).content
            image = QImage()
            image.loadFromData(data)
            scenes[i].addPixmap(QPixmap(image))
            views[i].fitInView(QRectF(0, 0, 320, 180), Qt.KeepAspectRatio)
            scenes[i].update()

    def fill_labels(self, titles, tab):
        if tab == "anime":
            labels = self.animeLabels
        elif tab == "playlist":
            labels = self.videoLabels

        self.clear_labels(tab)

        if len(titles) > 6:
            maxIndex = 6
        else:
            maxIndex = len(titles)


        for i in range(0, maxIndex):
            labels[i].setText(titles[i])

    def update_page_label(self, tab):
        if tab == "anime":
            pagesLabel = self.pagesLabel1
            currentPage = self.currentVideoPage
            totalPages = self.totalVideoPages
        elif tab == "playlist":
            pagesLabel = self.pagesLabel0
            currentPage = self.currentPlaylistPage
            totalPages = self.totalPlaylistPages

        pagesLabel.setText("{}/{}".format(currentPage + 1, totalPages + 1)) # pages' variables start with 0 so we are adding one to them

    def nextPage(self):
        senderId = self.sender().objectName()[-1:]

        # Throughout the program '0' most often means that the widget is on playlist management tab and '1' means it is on YT search tab
        if senderId == "1":
            # First we change the page number
            self.currentVideoPage += 1
            # Then we use this number to figure out an index number to use with arrays
            index = self.currentVideoPage * 6
            if self.currentVideoPage <= self.totalVideoPages:
                tab = "anime"
                self.clear_thumbnails(tab)
                self.clear_labels(tab)
                self.fill_thumbnails(self.videoThumbnails[index:], tab)
                self.fill_labels(self.videoTitles[index:], tab)
                self.update_page_label(tab)
            else:
                self.currentVideoPage -= 1

        elif senderId == "0":
            self.currentPlaylistPage += 1
            index = self.currentPlaylistPage * 6
            if self.currentPlaylistPage <= self.totalPlaylistPages:
                tab = "playlist"
                self.clear_thumbnails(tab)
                self.clear_labels(tab)
                self.fill_thumbnails(self.playlistVideoThumbnails[index:], tab)
                self.fill_labels(self.playlistVideoTitles[index:], tab)
                self.update_page_label(tab)
            else:
                self.currentPlaylistPage -= 1

    def previousPage(self):
        senderId = self.sender().objectName()[-1:]

        if senderId == "1":
            self.currentVideoPage -= 1
            index = self.currentVideoPage * 6
            if self.currentVideoPage >= 0:
                tab = "anime"
                self.clear_thumbnails(tab)
                self.clear_labels(tab)
                self.fill_thumbnails(self.videoThumbnails[index:], tab)
                self.fill_labels(self.videoTitles[index:], tab)
                self.update_page_label(tab)
            else:
                self.currentVideoPage += 1

        elif senderId == "0":
            self.currentPlaylistPage -= 1
            index = self.currentPlaylistPage * 6
            if self.currentPlaylistPage >= 0:
                tab = "playlist"
                self.clear_thumbnails(tab)
                self.clear_labels(tab)
                self.fill_thumbnails(self.playlistVideoThumbnails[index:], tab)
                self.fill_labels(self.playlistVideoTitles[index:], tab)
                self.update_page_label(tab)
            else:
                self.currentPlaylistPage += 1

    def open_HTML(self):
        fname, str = QFileDialog.getOpenFileName(self, 'Open file', '/home/Desktop', "Files (*.html)")
        if fname != '':
            animeNames = AnimeProvider.get_anime_from_file(fname)
            for anime in animeNames:
                self.animeListWidget.addItem(anime)
            self.statusBar().showMessage('File successfully loaded from HTML!')

    def list_playlists(self):
        self.tab0userPlaylistsList.clear()
        self.tab1userPlaylistsList.clear()

        titles, self.playlistIds = YouTubeProvider.get_user_playlists()

        for title in titles:
            self.userPlaylistsList0.addItem(title)
            self.userPlaylistsList1.addItem(title)

    def create_playlist(self):
        if YouTubeProvider.login is not None:
            name, ok = QInputDialog.getText(self, 'Add playlist', 'Enter playlist name: ')

            if ok:
                YouTubeProvider.create_playlist(name)
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
                YouTubeProvider.delete_playlist(self.playlistIds[self.currentPlaylistRow])
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

            YouTubeProvider.add_to_playlist(videoId, playlistId)

    def delete_video_from_playlist(self):

        if len(self.playlistVideoIds) > 0:
            # buttons' names end in a number from 0 to 5 then we can use that number as an index for array
            senderId = self.sender().objectName()[-1:]

            YouTubeProvider.delete_from_playlist(self.playlistVideoIds[int(senderId)])
            self.load_playlist()

    def log_in(self):
        json, str = QFileDialog.getOpenFileName(self, 'Open JSON file', '/home/Desktop', "Files (*.JSON)")
        if json != '':
            GoogleLogin.json_log_in(json)
            self.statusBar().showMessage('Logged in!')
            self.list_playlists()

    def delete_anime(self):
        self.animeListWidget.takeItem(self.animeListWidget.currentRow())

    def add_anime(self):
        title, ok = QInputDialog.getText(self, 'Add anime', 'Enter anime title:')
        if ok:
            self.animeListWidget.addItem(title)

    def count_pages(self, videos, tab):
        if tab == "anime":
            self.totalVideoPages = round(len(videos) / 6)
        elif tab == "playlist":
            self.totalPlaylistPages = round(len(videos) / 6)

    def load_playlist(self):
        if len(self.playlistIds) > 0:
            self.playlistVideoTitles, self.playlistVideoThumbnails, self.playlistVideoIds, self.playlistVideoUrlIds	= YouTubeProvider.load_playlist(
                self.playlistIds[self.currentPlaylistRow]
                )

            self.count_pages(self.playlistVideoTitles, "playlist")

            self.fill_thumbnails(self.playlistVideoThumbnails, "playlist")
            self.fill_labels(self.playlistVideoTitles, "playlist")
            self.update_page_label("playlist")
            self.statusBar().showMessage('Playlist loaded!')
        else:
            self.showError("You must log in first or this playlist has no videos.")

    def search(self):

        if self.animeListWidget.item(self.currentAnimeRow) is not None:
            if YouTubeProvider.login is not None:
                self.videoTitles, self.videoThumbnails, self.videoIds, self.videoUrlIds = YouTubeProvider.youtube_search(
                    self.animeListWidget.item(self.currentAnimeRow).text(),
                    self.addTextLabel.text()
                    )

                self.count_pages(self.videoTitles, "anime")

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
            """<p>Copyright &copy; 2015 Jan Kominczyk.
            <p>Python {} - PySide version {} - Qt version {}"""
            .format(platform.python_version(),
                PySide.__version__,
                PySide.QtCore.__version__,
                )
            )

    def showError(text):
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

        self.currentAnimeRow = self.animeListWidget.row(item)
