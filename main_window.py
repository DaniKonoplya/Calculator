import sys

import PyQt5.QtWidgets as wid


class Window(wid.QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle('QMainWindow')
        self.setCentralWidget(wid.QLabel("I'm the Central Widget"))
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Exit', self.close)

    def _createToolBar(self):
        tools = wid.QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _createStatusBar(self):
        status = wid.QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)


if __name__ == '__main__':
    app = wid.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
