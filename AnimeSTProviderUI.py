from PySide import QtCore, QtGui

class Ui_MainWindow(object):

    def onResize(self, newSize):
        pass
        #self.tabWidget.resize(self.centralWidget.size())
        #self.centralWidget.resize(self.MW.size())

    def setupUi(self, MainWindow):
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        ### Main Window
        #MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(640, 640))
        self.MW = MainWindow
        MainWindow.resizeEvent = self.onResize

        ### Central Widget
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setSizePolicy(sizePolicy)
        #self.centralwidget.setMinimumSize(QtCore.QSize(600, 450))

        ### Main tabWidget
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(MainWindow.geometry())
        self.tabWidget.setSizePolicy(sizePolicy)
        #self.tabWidget.setMinimumSize(QtCore.QSize(600,450))

        ### Vertical Layout - Playlist Management - Playlists list
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        ### Main Window
        #MainWindow.resize(600, 450)
        MainWindow.setSizePolicy(sizePolicy)
        #MainWindow.setMinimumSize(QtCore.QSize(900, 650))

        ### Central Widget
        self.centralwidget = QtGui.QWidget(MainWindow)
        #self.centralwidget.setSizePolicy(sizePolicy)
        self.centralLayout = QtGui.QHBoxLayout()
        self.centralwidget.setLayout(self.centralLayout)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.centralLayout.addWidget(self.tabWidget)

        ######### Tab 0
        self.tab = QtGui.QWidget(self.tabWidget)
        self.tab0Layout = BorderLayout()
        self.tab.setLayout(self.tab0Layout)

        #Tab 0 videopreviews
        self.tab0VideoPrevWidget = QtGui.QWidget(self.tab)
        #self.tab0VideoPrevWidget.setMaximumWidth(240)
        self.tab0Layout.addWidget(self.tab0VideoPrevWidget, BorderLayout.Center)
        self.tab0VideoPrevLayout = QtGui.QVBoxLayout(self.tab0VideoPrevWidget)
        self.tab0VideoPrevLayout.setSpacing(16)

        self.videoView0 = QGraphicsView(self.tab0VideoPrevWidget)
        self.tab0VideoPrevLayout.addWidget(self.videoView0)

        self.videoView1 = QGraphicsView(self.tab0VideoPrevWidget)
        self.tab0VideoPrevLayout.addWidget(self.videoView1)

        self.videoView2 = QGraphicsView(self.tab0VideoPrevWidget)
        self.tab0VideoPrevLayout.addWidget(self.videoView2)

        self.videoView3 = QGraphicsView(self.tab0VideoPrevWidget)
        self.tab0VideoPrevLayout.addWidget(self.videoView3)

        self.videoView4 = QGraphicsView(self.tab0VideoPrevWidget)
        self.tab0VideoPrevLayout.addWidget(self.videoView4)

        self.videoView5 = QGraphicsView(self.tab0VideoPrevWidget)
        self.tab0VideoPrevLayout.addWidget(self.videoView5)

        #Tab 0 labels
        self.tab0GridWidget = QtGui.QWidget(self.tab)
        self.tab0Layout.addWidget(self.tab0GridWidget, BorderLayout.East)
        self.tab0GridLayout = QtGui.QGridLayout(self.tab0GridWidget)
        self.tab0GridLayout.setHorizontalSpacing(6)
        self.tab0GridLayout.setVerticalSpacing(25)

        self.videoLabel0 = QtGui.QLabel(self.tab0GridWidget)
        self.videoLabel0.setLineWidth(1)
        self.videoLabel0.setText("")
        self.videoLabel0.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.tab0GridLayout.addWidget(self.videoLabel0, 0, 0, 1, 1)

        self.videoLabel1 = QtGui.QLabel(self.tab0GridWidget)
        self.videoLabel1.setText("")
        self.videoLabel1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.tab0GridLayout.addWidget(self.videoLabel1, 1, 0, 1, 1)

        self.videoLabel2 = QtGui.QLabel(self.tab0GridWidget)
        self.videoLabel2.setText("")
        self.videoLabel2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.tab0GridLayout.addWidget(self.videoLabel2, 2, 0, 1, 1)

        self.videoLabel3 = QtGui.QLabel(self.tab0GridWidget)
        self.videoLabel3.setText("")
        self.videoLabel3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.tab0GridLayout.addWidget(self.videoLabel3, 3, 0, 1, 1)

        self.videoLabel4 = QtGui.QLabel(self.tab0GridWidget)
        self.videoLabel4.setText("")
        self.videoLabel4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.tab0GridLayout.addWidget(self.videoLabel4, 4, 0, 1, 1)

        self.videoLabel5 = QtGui.QLabel(self.tab0GridWidget)
        self.videoLabel5.setText("")
        self.videoLabel5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.tab0GridLayout.addWidget(self.videoLabel5, 5, 0, 1, 1)

        ### Vertical Layout - Playlist Management - Playlists list
        self.verticalLayoutWidget = QtGui.QWidget(self.tab)
        self.tab0Layout.addWidget(self.verticalLayoutWidget, BorderLayout.West)
        #self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 200, 400))
        self.verticalLayoutWidget.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget.setMinimumSize(QtCore.QSize(200,300))
##Debug widget backgroud color
        #self.verticalLayoutWidget.setAutoFillBackground(True)
        #p = self.verticalLayoutWidget.palette()
        #p.setColor(self.verticalLayoutWidget.backgroundRole(), QtGui.QColor(255,0,0,255))
        #self.verticalLayoutWidget.setPalette(p)

        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)

        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.label)

        self.userPlaylistsList0 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.userPlaylistsList0)

        self.loadPlaylistBtn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.loadPlaylistBtn)

        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)

        self.addPlaylistBtn0 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.horizontalLayout.addWidget(self.addPlaylistBtn0)

        self.deletePlaylistBtn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.deletePlaylistBtn.setMaximumSize(QtCore.QSize(90, 90))
        self.horizontalLayout.addWidget(self.deletePlaylistBtn)

        self.verticalLayout.addLayout(self.horizontalLayout)

        ###Tab 0 buttons grid
        self.deleteFromPlaylistBtn1 = QtGui.QPushButton(self.tab0GridWidget)
        self.deleteFromPlaylistBtn1.setObjectName("deleteFromPlaylistBtn1")
        self.tab0GridLayout.addWidget(self.deleteFromPlaylistBtn1, 1, 2, 1, 1)

        self.deleteFromPlaylistBtn4 = QtGui.QPushButton(self.tab0GridWidget)
        self.deleteFromPlaylistBtn4.setObjectName("deleteFromPlaylistBtn4")
        self.tab0GridLayout.addWidget(self.deleteFromPlaylistBtn4, 4, 2, 1, 1)

        self.deleteFromPlaylistBtn2 = QtGui.QPushButton(self.tab0GridWidget)
        self.deleteFromPlaylistBtn2.setObjectName("deleteFromPlaylistBtn2")
        self.tab0GridLayout.addWidget(self.deleteFromPlaylistBtn2, 2, 2, 1, 1)

        self.deleteFromPlaylistBtn3 = QtGui.QPushButton(self.tab0GridWidget)
        self.deleteFromPlaylistBtn3.setObjectName("deleteFromPlaylistBtn3")
        self.tab0GridLayout.addWidget(self.deleteFromPlaylistBtn3, 3, 2, 1, 1)

        self.deleteFromPlaylistBtn0 = QtGui.QPushButton(self.tab0GridWidget)
        self.deleteFromPlaylistBtn0.setObjectName("deleteFromPlaylistBtn0")
        self.tab0GridLayout.addWidget(self.deleteFromPlaylistBtn0, 0, 2, 1, 1)

        self.deleteFromPlaylistBtn5 = QtGui.QPushButton(self.tab0GridWidget)
        self.deleteFromPlaylistBtn5.setObjectName("deleteFromPlaylistBtn5")
        self.tab0GridLayout.addWidget(self.deleteFromPlaylistBtn5, 5, 2, 1, 1)

        self.playlistVideoPreviewBtn0 = QtGui.QPushButton(self.tab0GridWidget)
        self.tab0GridLayout.addWidget(self.playlistVideoPreviewBtn0, 0, 1, 1, 1)

        self.playlistVideoPreviewBtn1 = QtGui.QPushButton(self.tab0GridWidget)
        self.tab0GridLayout.addWidget(self.playlistVideoPreviewBtn1, 1, 1, 1, 1)

        self.playlistVideoPreviewBtn2 = QtGui.QPushButton(self.tab0GridWidget)
        self.tab0GridLayout.addWidget(self.playlistVideoPreviewBtn2, 2, 1, 1, 1)

        self.playlistVideoPreviewBtn3 = QtGui.QPushButton(self.tab0GridWidget)
        self.tab0GridLayout.addWidget(self.playlistVideoPreviewBtn3, 3, 1, 1, 1)

        self.playlistVideoPreviewBtn4 = QtGui.QPushButton(self.tab0GridWidget)
        self.tab0GridLayout.addWidget(self.playlistVideoPreviewBtn4, 4, 1, 1, 1)

        self.playlistVideoPreviewBtn5 = QtGui.QPushButton(self.tab0GridWidget)
        self.tab0GridLayout.addWidget(self.playlistVideoPreviewBtn5, 5, 1, 1, 1)

        ###Tab 0 arrows
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.tab)
        self.tab0Layout.addWidget(self.horizontalLayoutWidget_2, BorderLayout.South)
        #self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(610, 560, 232, 31))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.pagesLabel0 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.addWidget(self.pagesLabel0)

        self.previousPageBtn0 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.addWidget(self.previousPageBtn0)

        self.nextPageBtn0 = QtGui.QPushButton(self.horizontalLayoutWidget_2)

        self.horizontalLayout_4.addWidget(self.nextPageBtn0)

        self.tabWidget.addTab(self.tab, "")

        #####Tab 1
        self.tab1 = QtGui.QWidget(self.tabWidget)
        self.tab1Layout = BorderLayout()
        self.tab1.setLayout(self.tab1Layout)

        #Tab 1 videopreviews
        self.tab1VideoPrevWidget = QtGui.QWidget(self.tab1)
        self.tab1Layout.addWidget(self.tab1VideoPrevWidget, BorderLayout.Center)
        self.tab1VideoPrevLayout = QtGui.QVBoxLayout(self.tab1VideoPrevWidget)
        self.tab1VideoPrevLayout.setSpacing(16)

        self.animeView0 = QtGui.QGraphicsView(self.tab1VideoPrevWidget)
        self.tab1VideoPrevLayout.addWidget(self.animeView0)

        self.animeView1 = QtGui.QGraphicsView(self.tab1VideoPrevWidget)
        self.tab1VideoPrevLayout.addWidget(self.animeView1)

        self.animeView2 = QtGui.QGraphicsView(self.tab1VideoPrevWidget)
        self.tab1VideoPrevLayout.addWidget(self.animeView2)

        self.animeView3 = QtGui.QGraphicsView(self.tab1VideoPrevWidget)
        self.tab1VideoPrevLayout.addWidget(self.animeView3)

        self.animeView4 = QtGui.QGraphicsView(self.tab1VideoPrevWidget)
        self.tab1VideoPrevLayout.addWidget(self.animeView4)

        self.animeView5 = QtGui.QGraphicsView(self.tab1VideoPrevWidget)
        self.tab1VideoPrevLayout.addWidget(self.animeView5)

        #Tab 1 labels
        self.tab1GridWidget = QtGui.QWidget(self.tab1)
        self.tab1Layout.addWidget(self.tab1GridWidget, BorderLayout.East)
        self.tab1GridLayout = QtGui.QGridLayout(self.tab1GridWidget)
        self.tab1GridLayout.setHorizontalSpacing(6)
        self.tab1GridLayout.setVerticalSpacing(25)

        self.animeLabel0 = QtGui.QLabel(self.tab1GridWidget)
        self.animeLabel0.setLineWidth(1)
        self.animeLabel0.setText("")
        self.animeLabel0.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.tab1GridLayout.addWidget(self.animeLabel0, 0, 0, 1, 1)

        self.animeLabel1 = QtGui.QLabel(self.tab1GridWidget)
        self.animeLabel1.setText("")
        self.animeLabel1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.tab1GridLayout.addWidget(self.animeLabel1, 1, 0, 1, 1)

        self.animeLabel2 = QtGui.QLabel(self.tab1GridWidget)
        self.animeLabel2.setText("")
        self.animeLabel2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.tab1GridLayout.addWidget(self.animeLabel2, 2, 0, 1, 1)

        self.animeLabel3 = QtGui.QLabel(self.tab1GridWidget)
        self.animeLabel3.setText("")
        self.animeLabel3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.tab1GridLayout.addWidget(self.animeLabel3, 3, 0, 1, 1)

        self.animeLabel4 = QtGui.QLabel(self.tab1GridWidget)
        self.animeLabel4.setText("")
        self.animeLabel4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.tab1GridLayout.addWidget(self.animeLabel4, 4, 0, 1, 1)

        self.animeLabel5 = QtGui.QLabel(self.tab1GridWidget)
        self.animeLabel5.setText("")
        self.animeLabel5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.tab1GridLayout.addWidget(self.animeLabel5, 5, 0, 1, 1)

        #Tab1 buttons
        self.addToPlaylistBtn3 = QtGui.QPushButton(self.tab1GridWidget)
        self.tab1GridLayout.addWidget(self.addToPlaylistBtn3, 3, 2, 1, 1)

        self.addToPlaylistBtn1 = QtGui.QPushButton(self.tab1GridWidget)
        self.tab1GridLayout.addWidget(self.addToPlaylistBtn1, 1, 2, 1, 1)

        self.addToPlaylistBtn4 = QtGui.QPushButton(self.tab1GridWidget)
        self.tab1GridLayout.addWidget(self.addToPlaylistBtn4, 4, 2, 1, 1)

        self.addToPlaylistBtn0 = QtGui.QPushButton(self.tab1GridWidget)
        self.tab1GridLayout.addWidget(self.addToPlaylistBtn0, 0, 2, 1, 1)

        self.addToPlaylistBtn5 = QtGui.QPushButton(self.tab1GridWidget)
        self.tab1GridLayout.addWidget(self.addToPlaylistBtn5, 5, 2, 1, 1)

        self.addToPlaylistBtn2 = QtGui.QPushButton(self.tab1GridWidget)
        self.tab1GridLayout.addWidget(self.addToPlaylistBtn2, 2, 2, 1, 1)

        self.videoPreviewBtn0 = QtGui.QPushButton(self.tab1GridWidget)
        self.tab1GridLayout.addWidget(self.videoPreviewBtn0, 0, 1, 1, 1)

        self.videoPreviewBtn1 = QtGui.QPushButton(self.tab1GridWidget)
        self.tab1GridLayout.addWidget(self.videoPreviewBtn1, 1, 1, 1, 1)

        self.videoPreviewBtn2 = QtGui.QPushButton(self.tab1GridWidget)
        self.tab1GridLayout.addWidget(self.videoPreviewBtn2, 2, 1, 1, 1)

        self.videoPreviewBtn3 = QtGui.QPushButton(self.tab1GridWidget)
        self.tab1GridLayout.addWidget(self.videoPreviewBtn3, 3, 1, 1, 1)

        self.videoPreviewBtn4 = QtGui.QPushButton(self.tab1GridWidget)
        self.tab1GridLayout.addWidget(self.videoPreviewBtn4, 4, 1, 1, 1)

        self.videoPreviewBtn5 = QtGui.QPushButton(self.tab1GridWidget)
        self.tab1GridLayout.addWidget(self.videoPreviewBtn5, 5, 1, 1, 1)

        #Tab 1 'your playlists'
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.tab1)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 181, 201))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        #self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.verticalLayout_3.addWidget(self.label_8)

        self.userPlaylistsList1 = QtGui.QListWidget(self.verticalLayoutWidget_3)
        self.verticalLayout_3.addWidget(self.userPlaylistsList1)

        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)

        self.addPlaylistBtn1 = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.horizontalLayout_2.addWidget(self.addPlaylistBtn1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayoutWidget_5 = QtGui.QWidget(self.tab1)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 220, 188, 321))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)

        self.label_15 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.verticalLayout_5.addWidget(self.label_15)

        self.animeListWidget = QtGui.QListWidget(self.verticalLayoutWidget_5)
        self.verticalLayout_5.addWidget(self.animeListWidget)

        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setContentsMargins(0, -1, -1, -1)

        self.addAnimeBtn = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.horizontalLayout_6.addWidget(self.addAnimeBtn)

        self.deleteAnimeBtn = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.horizontalLayout_6.addWidget(self.deleteAnimeBtn)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.verticalLayout_5.addWidget(self.label_2)

        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.verticalLayout_5.addWidget(self.label_3)

        self.addTextLabel = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.verticalLayout_5.addWidget(self.addTextLabel)

        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)

        self.searchYTBtn = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.horizontalLayout_3.addWidget(self.searchYTBtn)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        #Tab 1 Page numbers
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.tab1)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(610, 560, 232, 31))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)

        self.pagesLabel1 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.addWidget(self.pagesLabel1)

        self.previousPageBtn1 = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.addWidget(self.previousPageBtn1)

        self.nextPageBtn1 = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.addWidget(self.nextPageBtn1)

        self.tabWidget.addTab(self.tab1, "")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1090, 21))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuAbout = QtGui.QMenu(self.menubar)
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.actionOpen_HTML = QtGui.QAction(MainWindow)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionLoad_JSON_auth_file = QtGui.QAction(MainWindow)

        self.menuFile.addAction(self.actionLoad_JSON_auth_file)
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

    def heightForWidth(self, width):
        return width * 1.5

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "AnimeSTProvider", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Your playlists:", None, QtGui.QApplication.UnicodeUTF8))
        self.loadPlaylistBtn.setText(QtGui.QApplication.translate("MainWindow", "Load playlist", None, QtGui.QApplication.UnicodeUTF8))
        self.addPlaylistBtn0.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.deletePlaylistBtn.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteFromPlaylistBtn1.setText(QtGui.QApplication.translate("MainWindow", "Delete from playlist", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteFromPlaylistBtn4.setText(QtGui.QApplication.translate("MainWindow", "Delete from playlist", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteFromPlaylistBtn2.setText(QtGui.QApplication.translate("MainWindow", "Delete from playlist", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteFromPlaylistBtn3.setText(QtGui.QApplication.translate("MainWindow", "Delete from playlist", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteFromPlaylistBtn0.setText(QtGui.QApplication.translate("MainWindow", "Delete from playlist", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteFromPlaylistBtn5.setText(QtGui.QApplication.translate("MainWindow", "Delete from playlist", None, QtGui.QApplication.UnicodeUTF8))
        self.playlistVideoPreviewBtn0.setText(QtGui.QApplication.translate("MainWindow", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.playlistVideoPreviewBtn1.setText(QtGui.QApplication.translate("MainWindow", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.playlistVideoPreviewBtn2.setText(QtGui.QApplication.translate("MainWindow", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.playlistVideoPreviewBtn3.setText(QtGui.QApplication.translate("MainWindow", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.playlistVideoPreviewBtn4.setText(QtGui.QApplication.translate("MainWindow", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.playlistVideoPreviewBtn5.setText(QtGui.QApplication.translate("MainWindow", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.pagesLabel0.setText(QtGui.QApplication.translate("MainWindow", "0/0", None, QtGui.QApplication.UnicodeUTF8))
        self.previousPageBtn0.setText(QtGui.QApplication.translate("MainWindow", "<---", None, QtGui.QApplication.UnicodeUTF8))
        self.nextPageBtn0.setText(QtGui.QApplication.translate("MainWindow", "--->", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Playlist management", None, QtGui.QApplication.UnicodeUTF8))
        self.addToPlaylistBtn3.setText(QtGui.QApplication.translate("MainWindow", "Add to playlist", None, QtGui.QApplication.UnicodeUTF8))
        self.addToPlaylistBtn1.setText(QtGui.QApplication.translate("MainWindow", "Add to playlist", None, QtGui.QApplication.UnicodeUTF8))
        self.addToPlaylistBtn4.setText(QtGui.QApplication.translate("MainWindow", "Add to playlist", None, QtGui.QApplication.UnicodeUTF8))
        self.addToPlaylistBtn0.setText(QtGui.QApplication.translate("MainWindow", "Add to playlist", None, QtGui.QApplication.UnicodeUTF8))
        self.addToPlaylistBtn5.setText(QtGui.QApplication.translate("MainWindow", "Add to playlist", None, QtGui.QApplication.UnicodeUTF8))
        self.addToPlaylistBtn2.setText(QtGui.QApplication.translate("MainWindow", "Add to playlist", None, QtGui.QApplication.UnicodeUTF8))
        self.videoPreviewBtn0.setText(QtGui.QApplication.translate("MainWindow", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.videoPreviewBtn1.setText(QtGui.QApplication.translate("MainWindow", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.videoPreviewBtn2.setText(QtGui.QApplication.translate("MainWindow", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.videoPreviewBtn3.setText(QtGui.QApplication.translate("MainWindow", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.videoPreviewBtn4.setText(QtGui.QApplication.translate("MainWindow", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.videoPreviewBtn5.setText(QtGui.QApplication.translate("MainWindow", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Your playlists:", None, QtGui.QApplication.UnicodeUTF8))
        self.addPlaylistBtn1.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "Found animes:", None, QtGui.QApplication.UnicodeUTF8))
        self.addAnimeBtn.setToolTip(QtGui.QApplication.translate("MainWindow", "Add anime to this list", None, QtGui.QApplication.UnicodeUTF8))
        self.addAnimeBtn.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteAnimeBtn.setToolTip(QtGui.QApplication.translate("MainWindow", "Delete anime from this list", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteAnimeBtn.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Text to add at the end of anime title:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "(like OP, ED or OST)", None, QtGui.QApplication.UnicodeUTF8))
        self.searchYTBtn.setText(QtGui.QApplication.translate("MainWindow", "Search YouTube", None, QtGui.QApplication.UnicodeUTF8))
        self.pagesLabel1.setText(QtGui.QApplication.translate("MainWindow", "0/0", None, QtGui.QApplication.UnicodeUTF8))
        self.previousPageBtn1.setText(QtGui.QApplication.translate("MainWindow", "<---", None, QtGui.QApplication.UnicodeUTF8))
        self.nextPageBtn1.setText(QtGui.QApplication.translate("MainWindow", "--->", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QtGui.QApplication.translate("MainWindow", "Anime ST Search", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_HTML.setText(QtGui.QApplication.translate("MainWindow", "Open HTML", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About AnimeSTProvider", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_JSON_auth_file.setText(QtGui.QApplication.translate("MainWindow", "Load JSON auth file", None, QtGui.QApplication.UnicodeUTF8))

class QGraphicsView(QtGui.QGraphicsView):
    def __init__(self, parent = None):
        QtGui.QGraphicsView.__init__(self, parent)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        #sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)

    def heightForWidth(self, width):
        return width * 9 / 16

    def sizeHint(self):
        return QtCore.QSize(240, 120)

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
