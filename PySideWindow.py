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
        #Arrays
        self.animeScenes = [QGraphicsScene(), QGraphicsScene(), QGraphicsScene(),
                QGraphicsScene(), QGraphicsScene(), QGraphicsScene()]
        self.videoScenes = [QGraphicsScene(), QGraphicsScene(), QGraphicsScene(),
                QGraphicsScene(), QGraphicsScene(), QGraphicsScene()]
        self.animeViews = [self.animeView0, self.animeView1, self.animeView2,
                self.animeView3, self.animeView4, self.animeView5]
        self.videoViews = [self.videoView0, self.videoView1, self.videoView2,
                self.videoView3, self.videoView4, self.videoView5]
        self.animeLabels = [self.animeLabel0, self.animeLabel1, self.animeLabel2,
                self.animeLabel3, self.animeLabel4, self.animeLabel5]
        self.videoLabels = [self.videoLabel0, self.videoLabel1, self.videoLabel2,
                self.videoLabel3, self.videoLabel4, self.videoLabel5]
        # Menu
        self.actionOpen_HTML.triggered.connect(self.open_HTML)
        self.actionAbout.triggered.connect(self.show_about)
        self.actionLoad_JSON_auth_file.triggered.connect(self.log_in)
        # Buttons
        self.closeBtn = QPushButton()
        self.deleteAnimeBtn.clicked.connect(self.delete_anime)
        self.addAnimeBtn.clicked.connect(self.add_anime)
        self.searchYTBtn.clicked.connect(self.search)
        self.addPlaylistBtn0.clicked.connect(self.create_playlist)
        self.addPlaylistBtn1.clicked.connect(self.create_playlist)
        self.deletePlaylistBtn.clicked.connect(self.delete_playlist)
        self.loadPlaylistBtn.clicked.connect(self.load_playlist)
        self.videoPreviewBtn0.clicked.connect(self.preview)
        self.videoPreviewBtn1.clicked.connect(self.preview)
        self.videoPreviewBtn2.clicked.connect(self.preview)
        self.videoPreviewBtn3.clicked.connect(self.preview)
        self.videoPreviewBtn4.clicked.connect(self.preview)
        self.videoPreviewBtn5.clicked.connect(self.preview)
        self.playlistVideoPreviewBtn0.clicked.connect(self.preview)
        self.playlistVideoPreviewBtn1.clicked.connect(self.preview)
        self.playlistVideoPreviewBtn2.clicked.connect(self.preview)
        self.playlistVideoPreviewBtn3.clicked.connect(self.preview)
        self.playlistVideoPreviewBtn4.clicked.connect(self.preview)
        self.playlistVideoPreviewBtn5.clicked.connect(self.preview)
        self.addToPlaylistBtn0.clicked.connect(self.add_video_to_playlist)
        self.addToPlaylistBtn1.clicked.connect(self.add_video_to_playlist)
        self.addToPlaylistBtn2.clicked.connect(self.add_video_to_playlist)
        self.addToPlaylistBtn3.clicked.connect(self.add_video_to_playlist)
        self.addToPlaylistBtn4.clicked.connect(self.add_video_to_playlist)
        self.addToPlaylistBtn5.clicked.connect(self.add_video_to_playlist)
        self.deleteFromPlaylistBtn0.clicked.connect(self.delete_video_from_playlist)
        self.deleteFromPlaylistBtn1.clicked.connect(self.delete_video_from_playlist)
        self.deleteFromPlaylistBtn2.clicked.connect(self.delete_video_from_playlist)
        self.deleteFromPlaylistBtn3.clicked.connect(self.delete_video_from_playlist)
        self.deleteFromPlaylistBtn4.clicked.connect(self.delete_video_from_playlist)
        self.deleteFromPlaylistBtn5.clicked.connect(self.delete_video_from_playlist)
        self.nextPageBtn0.clicked.connect(self.nextPage)
        self.nextPageBtn1.clicked.connect(self.nextPage)
        self.previousPageBtn0.clicked.connect(self.previousPage)
        self.previousPageBtn1.clicked.connect(self.previousPage)
        self.closeBtn.clicked.connect(self.destroy_preview)
        #Variables
        self.playlistIds = []
        self.playlistVideoUrlIds = []
        self.playlistVideoIds = []
        self.playlistVideoTitles = []
        self.playlistVideoThumbnails = []
        self.videoUrlIds = []
        self.videoIds = []
        self.videoTitles = []
        self.videoThumbnails = []
        self.currentPlaylistRow = 0
        self.currentAnimeRow = 0
        self.totalVideoPages = 0
        self.totalPlaylistPages = 0
        self.currentVideoPage = 0
        self.currentPlaylistPage = 0
        #Events
        self.userPlaylistsList0.itemClicked.connect(self.on_playlist_row_changed)
        self.userPlaylistsList1.itemClicked.connect(self.on_playlist_row_changed)
        self.animeListWidget.itemClicked.connect(self.on_anime_row_changed)
        #Icons
        self.icon = QIcon("assets/icon.png")
        #Misc
        self.previewWindow = QWidget()
        self.webView = QWebView()

        self.setWindowIcon(self.icon)
        self.initialize_thumbnails()
        self.initialize_preview()

    def initialize_thumbnails(self):

        for i in range(0, 6):
            self.animeViews[i].setScene(self.animeScenes[i])
            self.videoViews[i].setScene(self.videoScenes[i])
            self.animeScenes[i].clear()
            self.videoScenes[i].clear()

    def initialize_preview(self):

        self.previewWindow.setWindowFlags(Qt.FramelessWindowHint)
        self.previewWindow.setFixedSize(685,470)
        self.previewWindow.setWindowTitle("Preview")
        self.layout = QVBoxLayout()
        self.previewWindow.setLayout(self.layout)
        self.webView.settings().setAttribute(QWebSettings.PluginsEnabled, True)
        self.closeBtn.setText("Close")
        self.layout.addWidget(self.webView)
        self.layout.addWidget(self.closeBtn)

    def clear_labels(self, tab):

       if tab == "anime":
            labels = self.animeLabels
            for i in range(0, 6):
                labels[i].setText("")
       elif tab == "playlist":
            labels = self.videoLabels
            for i in range(0, 6):
                labels[i].setText("")

    def clear_thumbnails(self, tab):

        if tab == "anime":
            for i in range(0, 6):
                self.animeScenes[i].clear()
                self.animeScenes[i].update()
        elif tab == "playlist":
            for i in range(0, 6):
                self.videoScenes[i].clear()
                self.videoScenes[i].update()

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

        self.userPlaylistsList0.clear()
        self.userPlaylistsList1.clear()

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
            self.message = QMessageBox()
            self.message.setWindowTitle("Error")
            self.message.setText("You must log in first.")
            self.message.setDefaultButton(QMessageBox.Ok)
            self.message.open()

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
            self.message = QMessageBox()
            self.message.setWindowTitle("Error")
            self.message.setText("You must log in first or this playlist has no videos.")
            self.message.setDefaultButton(QMessageBox.Ok)
            self.message.open()

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
                self.message = QMessageBox()
                self.message.setWindowTitle("Error")
                self.message.setText("You must log in first.")
                self.message.setDefaultButton(QMessageBox.Ok)
                self.message.open()
        else:
            self.message = QMessageBox()
            self.message.setWindowTitle("Error")
            self.message.setText("You must choose anime title first.")
            self.message.setDefaultButton(QMessageBox.Ok)
            self.message.open()

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

    def on_playlist_row_changed(self, item):

        if self.sender().objectName() == "userPlaylistsList0":
            self.currentPlaylistRow = self.userPlaylistsList0.row(item)
        elif self.sender().objectName() == "userPlaylistsList1":
            self.currentPlaylistRow = self.userPlaylistsList1.row(item)

    def on_anime_row_changed(self, item):

        self.currentAnimeRow = self.animeListWidget.row(item)
