import sys

import PyQt5.QtWidgets as widgets


def create_gui(title='PyQt5 App', label='Hello World1'):
    app = widgets.QApplication(sys.argv)
    window = widgets.QWidget()
    window.setWindowTitle(title)
    layout = widgets.QGridLayout()
    layout.addWidget(widgets.QPushButton('Left'), 0, 0)
    layout.addWidget(widgets.QPushButton('Center'), 0, 1)
    layout.addWidget(widgets.QPushButton('Right'), 0, 2)
    layout.addWidget(widgets.QPushButton('Left'), 1, 0)
    layout.addWidget(widgets.QPushButton('Center'), 1, 1)
    layout.addWidget(widgets.QPushButton('Right'), 1, 2)
    layout.addWidget(widgets.QPushButton('Right'), 2, 0)
    layout.addWidget(widgets.QPushButton(
        'Button (2,1) + 2 Columns Span'), 2, 1, 1, 2)
    window.setLayout(layout)
    # window.setGeometry(300, 300, 500, 500)
    # window.move(60, 15)
    # helloMsg = QLabel(f'<h1>{label}</h1>', parent=window)
    # helloMsg.move(60, 15)
    window.show()
    sys.exit(app.exec_())

def create_gui_form(title='PyQt5 App', label='Hello World1'):
    app = widgets.QApplication(sys.argv)
    window = widgets.QWidget()
    window.setWindowTitle(title)
    layout = widgets.QFormLayout()
    layout.addRow('Name:',widgets.QLineEdit())
    layout.addRow('Age:',widgets.QLineEdit())
    layout.addRow('Job:',widgets.QLineEdit())
    layout.addRow('Hobbies:',widgets.QLineEdit())
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    create_gui()
