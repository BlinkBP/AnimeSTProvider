import sys
import PySideWindow
from PySide.QtGui import QApplication


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    # window = PyQTWindow.Window()
    window = PySideWindow.Window()
    window.show()
    sys.exit(app.exec_())
