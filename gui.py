import sys
from itertools import groupby
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout,
    QLabel, QTextEdit, QPushButton)

from renderer import mathTex_to_QPixmap
import typewriter as tw

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.tw = tw.Typewriter()
        self.initUI()

    def initUI(self):

        self.text_label = QLabel('Input here')
        self.text_edit = QTextEdit()

        # buttons invalidate space bar press registered on linux
        # self.generate_btn = QPushButton('Generate')

        self.output_text = ''
        # self.output_label = QLabel(self.output_text, self)
        self.output_label = QLabel()
        self.render_latex()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.text_label, 1, 0)
        # grid.addWidget(self.generate_btn, 3, 0)
        # grid.addWidget(self.text_edit, 1, 1, 2, 1)
        grid.addWidget(self.output_label, 3, 1)

        self.setLayout(grid)
        self.setGeometry(100, 100, 500, 200)
        self.setWindowTitle('typewriter')
        self.show()

    # def keyPressEvent(self, event):
    #
    #     if event.key() == Qt.Key_Escape:
    #         self.close()
    #
    #     modifiers = QApplication.keyboardModifiers()
    #     if modifiers == Qt.ShiftModifier:
    #         mod_text = 'Shift'
    #     elif modifiers == Qt.ControlModifier:
    #         pass
    #     elif modifiers == (Qt.ControlModifier | Qt.ShiftModifier):
    #         mod_text = 'Ctrl+Shift'
    #     else:
    #         mod_text = ''
    #
    #     text = 'Letter: {mod} {let}'.format(mod=mod_text, let=event.key())
    #     self.output_label.setText(text)


    # def keyPressEvent(self, event):
    #
    #     if event.key() == Qt.Key_Escape:
    #         self.close()
    #
    #     key_str = str(event.key())
    #     if self.key_lst == [] or not event.isAutoRepeat():
    #         self.num_pressed += 1
    #         self.key_lst.append(key_str)
    #
    # def keyReleaseEvent(self, event):
    #
    #     if self.num_pressed > 0:
    #         self.num_pressed -= 1
    #
    #     if self.num_pressed == 0:
    #         self.updateRender(self.key_lst)
    #         self.key_lst = []

    def keyPressEvent(self, event):
        logging.info("Key pressed")

        if event.key() == Qt.Key_Escape:
            self.close()

        key_str = str(event.key())
        logging.debug("keyPressEvent: '{}' {} mod: {} mod raw: {}".format(event.text(),event.key(), event.nativeModifiers(), int(event.modifiers())))

        if not event.isAutoRepeat() and key_str != '16777249': # no mac cmd pressed, because key releases not fully captured
            self.tw.process_key_pressed(key_str)
            self.render_latex(self.tw.key_lst)

    def keyReleaseEvent(self, event):
        self.tw.process_key_released()
        logging.info("Key released")


    def render_latex(self, input=None):

        if input is None:
            self.pixmap = QPixmap()
        else:
            latex_str = self.tw.latex_str
            logger.debug("Latex: {} {}".format(latex_str, input))
            if latex_str != '':
                self.pixmap = mathTex_to_QPixmap(r'${latex_str}$'.format(latex_str=latex_str),
                                                 fontsize=24)
        self.output_label.setPixmap(self.pixmap)

def main():

    app = QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

#### PyQT4 version

# from PyQt4 import QtGui, QtCore
# import sys
#
#
# class MainWindow(QtGui.QMainWindow):
#     # initialize instance
#     def __init__(self):
#         # super gives parent class
#         # initialize methods from parent class
#         super().__init__()
#         self.create_ui()
#
#     def create_ui(self):
#
#         # define open entry
#         open_file = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
#         open_file.setShortcut('Ctrl+O')
#         open_file.setStatusTip('Open new File')
#         open_file.triggered.connect(self.show_file_dialog)
#
#         # define quit entry
#         exit_program = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
#         exit_program.setShortcut('Ctrl+Q')
#         exit_program.setStatusTip('Exit application')
#         exit_program.triggered.connect(QtGui.qApp.quit)
#
#         # define menu bar
#         menubar = self.menuBar()
#         file_menu = menubar.addMenu('&File')
#         file_menu.addAction(open_file)
#         file_menu.addAction(exit_program)
#
#         # add status bar
#         self.statusBar()
#
#         # add fields
#         text_edit = QtGui.QTextEdit()
#         button = QtGui.QPushButton('press me')
#
#         grid = QtGui.QGridLayout()
#         grid.addWidget(button, 0,0)
#         grid.addWidget(text_edit, 2, 0, 1, 1)
#
#
#         self.center = QtGui.QWidget()
#         self.center.setLayout(grid)
#         self.setCentralWidget(self.center)
#
#
#         self.setGeometry(100, 100, 500, 500)
#         self.setWindowTitle('typewriter')
#         self.show()
#
#
#     def show_file_dialog(self):
#         fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
#         f = open(fname, 'r')
#         with f:
#             data = f.read()
#             self.text_edit.setText(data)
#
#     def paintEvent(self, e):
#
#         qp = QtGui.QPainter()
#         qp.begin(self)
# #        self.drawPoints(qp)
#         qp.end()
#
# def main():
#
#     app = QtGui.QApplication(sys.argv)
#     mw = MainWindow()
#
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()
