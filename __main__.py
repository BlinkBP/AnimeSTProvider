import sys
import os
import PySideWindow
from PySide.QtGui import QApplication, QImageReader
from PySide.QtCore import QCoreApplication


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    # We need to load plugin to show thumbnails
    app.addLibraryPath('/Python34/Lib/site-packages/PySide/plugins/')
    window = PySideWindow.Window()
    window.show()
    sys.exit(app.exec_())
