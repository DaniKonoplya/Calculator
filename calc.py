import sys
import controller
import model
import PyQt5.QtWidgets as w
from PyQt5.QtCore import Qt


__version__ = '0.1'
__author__ = 'Dani Konoplya'


class PyCalcUi(w.QMainWindow):
    """ PyCalc's View (GUI)"""

    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyCalc')
        self.setFixedSize(235, 235)

        self.generalLayout = w.QVBoxLayout()
        # This is a parent for the rest of the Gui component.
        self._centralWidget = w.QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        """Create Display"""
        self.display = w.QLineEdit()

        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)

        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        """Create the buttons."""
        self.buttons = {}

        buttonsLayout = w.QGridLayout()
        t = tuple(('7', '8', '9', '/', 'C', '4', '5', '6', '*',
                   '(', '1', '2', '3', '-', ')', '0', '00', '.', '+', '='))

        buttons = {}
        counter = 0
        for i in range(4):
            for y in range(5):
                buttons[t[counter]] = i, y
                counter += 1

        for btnText, pos in buttons.items():
            self.buttons[btnText] = w.QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])

        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        """Set display's text"""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        return self.display.text()

    def clearDisplay(self):
        """Clear display"""
        self.setDisplayText('')


def main():
    pycalc = w.QApplication(sys.argv)
    view = PyCalcUi()
    view.show()
    mod = model.evaluateExpression
    controller.PyCalcCtrl(view=view, model=mod)
    sys.exit(pycalc.exec_())


if __name__ == '__main__':
    main()
