from PySide import QtCore, QtGui
from YouTubeProvider import Video
import requests

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        ### Main Window
        MainWindow.setMinimumSize(QtCore.QSize(900, 650))
        self.MW = MainWindow

        ### Central Widget
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setSizePolicy(sizePolicy)

        ### Main tabWidget
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(MainWindow.geometry())

        ### Central Widget
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralLayout = QtGui.QHBoxLayout()
        self.centralwidget.setLayout(self.centralLayout)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.centralLayout.addWidget(self.tabWidget)

        ######### Tab 0
        self.tab = QtGui.QWidget(self.tabWidget)
        self.tab0Layout = BorderLayout()
        self.tab.setLayout(self.tab0Layout)
        self.tabWidget.addTab(self.tab, "")

        ##Tab 0 right side
        self.tab0RightWidget = QtGui.QWidget(self.tab)
        self.tab0RightLayout = QtGui.QVBoxLayout(self.tab0RightWidget)

        self.tab0RightScrollArea = QtGui.QScrollArea(self.tab0RightWidget)
        self.tab0RightLayout.addWidget(self.tab0RightScrollArea)
        self.tab0Layout.addWidget(self.tab0RightWidget, BorderLayout.Center)

        self.tab0RightContainerWidget = QtGui.QWidget(self.tab0RightScrollArea)
        self.tab0RightContainerWidget.setLayout(QtGui.QVBoxLayout(self.tab0RightContainerWidget))

        self.tab0RightScrollArea.setWidget(self.tab0RightContainerWidget)
        self.tab0RightScrollArea.setWidgetResizable(True)

        ###Tab 0 Playlist Management
        self.tab0LeftWidget = QtGui.QWidget(self.tab)
        self.tab0Layout.addWidget(self.tab0LeftWidget, BorderLayout.West)
        self.tab0LeftLayout = QtGui.QVBoxLayout(self.tab0LeftWidget)

        self.tab0YourPlaylistsLabel = QtGui.QLabel(self.tab0LeftWidget)
        self.tab0LeftLayout.addWidget(self.tab0YourPlaylistsLabel)
        self.tab0UserPlaylistsList = QtGui.QListWidget(self.tab0LeftWidget)
        self.tab0LeftLayout.addWidget(self.tab0UserPlaylistsList)
        self.tab0LoadPlaylistBtn = QtGui.QPushButton(self.tab0LeftWidget)
        self.tab0LeftLayout.addWidget(self.tab0LoadPlaylistBtn)

        self.tab0BtnHLayout = QtGui.QHBoxLayout()
        self.tab0BtnHLayout.setSpacing(3)
        self.tab0AddPlaylistBtn = QtGui.QPushButton(self.tab0LeftWidget)
        self.tab0BtnHLayout.addWidget(self.tab0AddPlaylistBtn)
        self.tab0DeletePlaylistBtn = QtGui.QPushButton(self.tab0LeftWidget)
        self.tab0BtnHLayout.addWidget(self.tab0DeletePlaylistBtn)

        self.tab0LeftLayout.addLayout(self.tab0BtnHLayout)

        #####Tab 1
        self.tab1 = QtGui.QWidget(self.tabWidget)
        self.tab1Layout = BorderLayout()
        self.tab1.setLayout(self.tab1Layout)
        self.tabWidget.addTab(self.tab1, "")

        #Tab 1 right side
        self.tab1RightWidget = QtGui.QWidget(self.tab1)
        self.tab1RightLayout = QtGui.QVBoxLayout(self.tab1RightWidget)

        self.tab1RightScrollArea = QtGui.QScrollArea(self.tab1RightWidget)
        self.tab1RightLayout.addWidget(self.tab1RightScrollArea)
        self.tab1Layout.addWidget(self.tab1RightWidget, BorderLayout.Center)

        self.tab1RightContainerWidget = QtGui.QWidget(self.tab1RightScrollArea)
        self.tab1RightContainerWidget.setLayout(QtGui.QVBoxLayout(self.tab1RightContainerWidget))

        self.tab1RightScrollArea.setWidget(self.tab1RightContainerWidget)
        self.tab1RightScrollArea.setWidgetResizable(True)

        ####Tab 1 Playlist Management + YT search
        self.tab1LeftWidget = QtGui.QWidget(self.tab1)
        self.tab1Layout.addWidget(self.tab1LeftWidget, BorderLayout.West)
        self.tab1LeftLayout = QtGui.QVBoxLayout(self.tab1LeftWidget)

        self.tab1YourPlaylistsLabel = QtGui.QLabel(self.tab1LeftWidget)
        self.tab1LeftLayout.addWidget(self.tab1YourPlaylistsLabel)
        self.tab1UserPlaylistsList = QtGui.QListWidget(self.tab1LeftWidget)
        self.tab1LeftLayout.addWidget(self.tab1UserPlaylistsList)

        self.tab1AddPlaylistBtn = QtGui.QPushButton(self.tab1LeftWidget)
        self.tab1LeftLayout.addWidget(self.tab1AddPlaylistBtn)

        self.tab1FoundAnimesLabel = QtGui.QLabel(self.tab1LeftWidget)
        self.tab1LeftLayout.addWidget(self.tab1FoundAnimesLabel)

        self.tab1AnimesList = QtGui.QListWidget(self.tab1LeftWidget)
        self.tab1LeftLayout.addWidget(self.tab1AnimesList)

        self.tab1BtnHLayout = QtGui.QHBoxLayout()
        self.tab1BtnHLayout.setSpacing(3)
        self.tab1AddAnimeBtn = QtGui.QPushButton(self.tab1LeftWidget)
        self.tab1BtnHLayout.addWidget(self.tab1AddAnimeBtn)
        self.tab1DeleteAnimeBtn = QtGui.QPushButton(self.tab1LeftWidget)
        self.tab1BtnHLayout.addWidget(self.tab1DeleteAnimeBtn)
        self.tab1LeftLayout.addLayout(self.tab1BtnHLayout)

        self.tab1InfoLabel0 = QtGui.QLabel(self.tab1LeftWidget)
        self.tab1LeftLayout.addWidget(self.tab1InfoLabel0)

        self.tab1InfoLabel1 = QtGui.QLabel(self.tab1LeftWidget)
        self.tab1LeftLayout.addWidget(self.tab1InfoLabel1)

        self.tab1AddTextLabel = QtGui.QLineEdit(self.tab1LeftWidget)
        self.tab1LeftLayout.addWidget(self.tab1AddTextLabel)

        self.tab1SearchYTBtn = QtGui.QPushButton(self.tab1LeftWidget)
        self.tab1LeftLayout.addWidget(self.tab1SearchYTBtn)

        MainWindow.setCentralWidget(self.centralwidget)
        ###Menu bar/Status bar
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuAbout = QtGui.QMenu(self.menubar)
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.actionOpen_HTML = QtGui.QAction(MainWindow)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionLog_In = QtGui.QAction(MainWindow)

        self.menuFile.addAction(self.actionLog_In)
        self.menuFile.addAction(self.actionOpen_HTML)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        #self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "AnimeSTProvider", None, QtGui.QApplication.UnicodeUTF8))
        self.tab0YourPlaylistsLabel.setText(QtGui.QApplication.translate("MainWindow", "Your playlists:", None, QtGui.QApplication.UnicodeUTF8))
        self.tab0LoadPlaylistBtn.setText(QtGui.QApplication.translate("MainWindow", "Load playlist", None, QtGui.QApplication.UnicodeUTF8))
        self.tab0AddPlaylistBtn.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.tab0DeletePlaylistBtn.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Playlist management", None, QtGui.QApplication.UnicodeUTF8))
        self.tab1YourPlaylistsLabel.setText(QtGui.QApplication.translate("MainWindow", "Your playlists:", None, QtGui.QApplication.UnicodeUTF8))
        self.tab1AddPlaylistBtn.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.tab1FoundAnimesLabel.setText(QtGui.QApplication.translate("MainWindow", "Found animes:", None, QtGui.QApplication.UnicodeUTF8))
        self.tab1AddAnimeBtn.setToolTip(QtGui.QApplication.translate("MainWindow", "Add anime to this list", None, QtGui.QApplication.UnicodeUTF8))
        self.tab1AddAnimeBtn.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.tab1DeleteAnimeBtn.setToolTip(QtGui.QApplication.translate("MainWindow", "Delete anime from this list", None, QtGui.QApplication.UnicodeUTF8))
        self.tab1DeleteAnimeBtn.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.tab1InfoLabel0.setText(QtGui.QApplication.translate("MainWindow", "Text to add at the end of anime title:", None, QtGui.QApplication.UnicodeUTF8))
        self.tab1InfoLabel1.setText(QtGui.QApplication.translate("MainWindow", "(like OP, ED or OST)", None, QtGui.QApplication.UnicodeUTF8))
        self.tab1SearchYTBtn.setText(QtGui.QApplication.translate("MainWindow", "Search YouTube", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QtGui.QApplication.translate("MainWindow", "Anime ST Search", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_HTML.setText(QtGui.QApplication.translate("MainWindow", "Open HTML", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About AnimeSTProvider", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLog_In.setText(QtGui.QApplication.translate("MainWindow", "Log in", None, QtGui.QApplication.UnicodeUTF8))

class VideoItem(QtGui.QWidget):
    def __init__(self, parent = None, video = None):
        QtGui.QWidget.__init__(self, parent)
        self.videoID = video.id
        self.videoURL = video.videoId
        self.thumbW = 112
        self.thumbH = 63
        self.createWidget()
        self.setContent(video)


    def createWidget(self):
        self.layout = QtGui.QHBoxLayout(self)

        self.videoView = QtGui.QGraphicsView(self)
        self.videoView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.videoView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.videoView.setMaximumSize(self.thumbW, self.thumbH) #16:9
        self.layout.addWidget(self.videoView)

        self.label = QtGui.QLabel(self)
        self.layout.addWidget(self.label)

        self.btn = QtGui.QPushButton(self)
        self.layout.addWidget(self.btn)

        self.previewBtn = QtGui.QPushButton(self, "Preview")
        self.layout.addWidget(self.previewBtn)

    def setContent(self, video):
        self.setLabel(video.title)
        self.setThumbnail(video.thumbUrl)

    def setLabel(self, text):
        self.label.setText(text)

    def setThumbnail(self, thumb_url):
        data = requests.get(thumb_url).content
        thumbImg = QtGui.QImage()
        thumbImg.loadFromData(data)
        thumbPix = QtGui.QPixmap()
        thumbPix.convertFromImage(thumbImg.scaled(self.thumbW, self.thumbH))
        self.videoScene = QtGui.QGraphicsScene()
        self.videoScene.addPixmap(thumbPix)
        self.videoView.setScene(self.videoScene)

class BorderLayout(QtGui.QLayout):
    West, North, South, East, Center = range(5)
    MinimumSize, SizeHint = range(2)

    def __init__(self, parent=None, margin=0, spacing=-1):
        super(BorderLayout, self).__init__(parent)

        self.setContentsMargins(margin, margin, margin, margin)
        self.setSpacing(spacing)
        self.list = []

    def __del__(self):
        l = self.takeAt(0)
        while l:
            l = self.takeAt(0)

    def addItem(self, item):
        self.add(item, BorderLayout.West)

    def addWidget(self, widget, position):
        self.add(QtGui.QWidgetItem(widget), position)

    def expandingDirections(self):
        return QtCore.Qt.Horizontal | QtCore.Qt.Vertical

    def hasHeightForWidth(self):
        return False

    def count(self):
        return len(self.list)

    def itemAt(self, index):
        if index < len(self.list):
            return self.list[index].item

        return None

    def minimumSize(self):
        return self.calculateSize(BorderLayout.MinimumSize)

    def setGeometry(self, rect):
        center = None
        eastWidth = 0
        westWidth = 0
        northHeight = 0
        southHeight = 0
        centerHeight = 0

        super(BorderLayout, self).setGeometry(rect)

        for wrapper in self.list:
            item = wrapper.item
            position = wrapper.position

            if position == BorderLayout.North:
                item.setGeometry(QtCore.QRect(rect.x(), northHeight,
                        rect.width(), item.sizeHint().height()))

                northHeight += item.geometry().height() + self.spacing()

            elif position == BorderLayout.South:
                item.setGeometry(QtCore.QRect(item.geometry().x(),
                        item.geometry().y(), rect.width(),
                        item.sizeHint().height()))

                southHeight += item.geometry().height() + self.spacing()

                item.setGeometry(QtCore.QRect(rect.x(),
                        rect.y() + rect.height() - southHeight + self.spacing(),
                        item.geometry().width(), item.geometry().height()))

            elif position == BorderLayout.Center:
                center = wrapper

        centerHeight = rect.height() - northHeight - southHeight

        for wrapper in self.list:
            item = wrapper.item
            position = wrapper.position

            if position == BorderLayout.West:
                item.setGeometry(QtCore.QRect(rect.x() + westWidth,
                        northHeight, item.sizeHint().width(), centerHeight))

                westWidth += item.geometry().width() + self.spacing()

            elif position == BorderLayout.East:
                item.setGeometry(QtCore.QRect(item.geometry().x(),
                        item.geometry().y(), item.sizeHint().width(),
                        centerHeight))

                eastWidth += item.geometry().width() + self.spacing()

                item.setGeometry(QtCore.QRect(rect.x() + rect.width() - eastWidth + self.spacing(),
                        northHeight, item.geometry().width(),
                        item.geometry().height()))

        if center:
            center.item.setGeometry(QtCore.QRect(westWidth, northHeight,
                    rect.width() - eastWidth - westWidth, centerHeight))

    def sizeHint(self):
        return self.calculateSize(BorderLayout.SizeHint)

    def takeAt(self, index):
        if index >= 0 and index < len(self.list):
            layoutStruct = self.list.pop(index)
            return layoutStruct.item

        return None

    def add(self, item, position):
        self.list.append(ItemWrapper(item, position))

    def calculateSize(self, sizeType):
        totalSize = QtCore.QSize()

        for wrapper in self.list:
            position = wrapper.position
            itemSize = QtCore.QSize()

            if sizeType == BorderLayout.MinimumSize:
                itemSize = wrapper.item.minimumSize()
            else: # sizeType == BorderLayout.SizeHint
                itemSize = wrapper.item.sizeHint()

            if position in (BorderLayout.North, BorderLayout.South, BorderLayout.Center):
                totalSize.setHeight(totalSize.height() + itemSize.height())

            if position in (BorderLayout.West, BorderLayout.East, BorderLayout.Center):
                totalSize.setWidth(totalSize.width() + itemSize.width())

        return totalSize

class ItemWrapper(object):
    def __init__(self, i, p):
        self.item = i
        self.position = p
