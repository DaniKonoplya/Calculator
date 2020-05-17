import sys
import PyQt5.QtWidgets as widgets


class Dialog(widgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('QDialog')
        dlgLayout = widgets.QVBoxLayout()
        formLayout = widgets.QFormLayout()
        formLayout.addRow('Name:', widgets.QLineEdit())
        formLayout.addRow('Age:', widgets.QLineEdit())
        formLayout.addRow('Job:', widgets.QLineEdit())
        formLayout.addRow('Hobbies:', widgets.QLineEdit())
        dlgLayout.addLayout(formLayout)
        btns = widgets.QDialogButtonBox()
        btns.setStandardButtons(
            widgets.QDialogButtonBox.Cancel | widgets.QDialogButtonBox.Ok)
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)


if __name__ == '__main__':
    app = widgets.QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
