import sys
import functools

import PyQt5.QtWidgets as w


def greeting(who):
    """Slot function"""
    if msg.text():
        msg.setText("")
    else:
        msg.setText(f"Hello World {who}!")


app = w.QApplication(sys.argv)
window = w.QWidget()
window.setWindowTitle('Signas and slots')
layout = w.QVBoxLayout()


btn = w.QPushButton('Greet')
# btn.clicked.connect(functools.partial(greeting, 'Denis'))
btn.clicked.connect(lambda:greeting('Denis') )

layout.addWidget(btn)
msg = w.QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
