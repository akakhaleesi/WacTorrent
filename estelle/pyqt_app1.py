from PyQt5 import QtWidgets, QtGui, QtCore
import sys

font_but = QtGui.QFont()
font_but.setFamily("Segoe UI Symbol")
font_but.setPointSize(10)
font_but.setWeight(95)

class Form(QtWidgets.QDialog):
   def __init__(self, parent=None):
      super(Form, self).__init__(parent)

      layout = QtWidgets.QVBoxLayout()
      self.b1 = QtWidgets.QPushButton("Button1")
      self.b1.setCheckable(True)
      self.b1.toggle()
      self.b1.clicked.connect(lambda:self.whichbtn(self.b1))
      self.b1.clicked.connect(self.btnstate)
      layout.addWidget(self.b1)

      self.b2 = QtWidgets.QPushButton()
      self.b2.setIcon(QtWidgets.QIcon(QPixmap("python.gif")))
      self.b2.clicked.connect(lambda:self.whichbtn(self.b2))
      layout.addWidget(self.b2)
      self.setLayout(layout)
      self.b3 = QtCore.QPushButton("Disabled")
      self.b3.setEnabled(False)
      layout.addWidget(self.b3)

      self.b4 = QtWidgets.QPushButton("&Default")
      self.b4.setDefault(True)
      self.b4.clicked.connect(lambda:self.whichbtn(self.b4))
      layout.addWidget(self.b4)

      self.setWindowTitle("Button demo")

   def btnstate(self):
      if self.b1.isChecked():
         print ("button pressed")
      else:
         print ("button released")

   def whichbtn(self,b):
      print ("clicked button is " + b.text())

def main():
   app = QtWidgets.QApplication(sys.argv)
   ex = Form()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()

# class PushBut1(QtWidgets.QPushButton):
    # def __init__(self, parent=None):
    #     super(PushBut1, self).__init__(parent)
    #     self.setMouseTracking(True)
    #     self.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(1,255,255,100); color: rgba(0,190,255,255); border-style: solid;"
    #                        "border-radius: 3px; border-width: 0.5px; border-color: rgba(127,127,255,255);")
    #
    # def enterEvent(self, event):
    #     if self.isEnabled() is True:
    #         self.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(1,255,255,100); color: rgba(0,230,255,255);"
    #                            "border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: rgba(0,230,255,255);")
    #     if self.isEnabled() is False:
    #         self.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(1,255,255,100); color: rgba(0,190,255,255); border-style: solid;"
    #                            "border-radius: 3px; border-width: 0.5px; border-color: rgba(127,127,255,255);")
    #
    # def leaveEvent(self, event):
    #     self.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(1,255,255,100); color: rgba(0,190,255,255); border-style: solid;"
    #                        "border-radius: 3px; border-width: 0.5px; border-color: rgba(127,127,255,255);")
        # def __init__(self, parent=None):
        #     super(PushBut1, self).__init__(parent)
        #     self.title = 'PyQt5 file dialogs - pythonspot.com'
        #     self.left = 10
        #     self.top = 10
        #     self.width = 640
        #     self.height = 480
        #     self.initUI()
        #
        # def initUI(self):
        #     self.setWindowTitle(self.title)
        #     self.setGeometry(self.left, self.top, self.width, self.height)
        #
        #     self.openFileNameDialog()
        #     self.openFileNamesDialog()
        #     self.saveFileDialog()
        #
        #     self.show()
        #
        # def openFileNameDialog(self):
        #     options = QtWidgets.QFileDialog.Options()
        #     options |= QtWidgets.QFileDialog.DontUseNativeDialog
        #     fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        #     if fileName:
        #         print(fileName)

        # def openFileNamesDialog(self):
        #     options = QtWidgets.QFileDialog.Options()
        #     options |= QtWidgets.QFileDialog.DontUseNativeDialog
        #     files, _ = QtWidgets.QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        #     if files:
        #         print(files)
        #
        # def saveFileDialog(self):
        #     options = QtWidgets.QFileDialog.Options()
        #     options |= QtWidgets.QFileDialog.DontUseNativeDialog
        #     fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        #     if fileName:
        #         print(fileName)

        # if __name__ == '__main__':
        #     App = QtWidgets.QApplication(sys.argv)
        #     ex = App()
        #     sys.exit(app.exec_())


class PyQtApp(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("PyQt Application")
        self.setWindowIcon(QtGui.QIcon("Path/to/Your/image/file.png"))
        self.setMinimumWidth(resolution.width() / 3)
        self.setMinimumHeight(resolution.height() / 1.5)
        self.setStyleSheet("QWidget {background-color: rgba(0,41,59,255);} QScrollBar:horizontal {width: 1px; height: 1px;"
                           "background-color: rgba(0,41,59,255);} QScrollBar:vertical {width: 1px; height: 1px;"
                           "background-color: rgba(0,41,59,255);}")
        self.textf = QtWidgets.QTextEdit(self)
        self.textf.setPlaceholderText("Results...")
        self.textf.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(0,255,255,100); color: rgba(0,190,255,255);"
                                 "border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: rgba(0,140,255,255);")
        self.but1 = PushBut1(self)
        self.but1.setText("")
        self.but1.setFixedWidth(72)
        self.but1.setFont(font_but)
        self.but2 = PushBut1(self)
        self.but2.setText("")
        self.but2.setFixedWidth(72)
        self.but2.setFont(font_but)
        self.but3 = PushBut1(self)
        self.but3.setText("")
        self.but3.setFixedWidth(72)
        self.but3.setFont(font_but)
        self.but4 = PushBut1(self)
        self.but4.setText("")
        self.but4.setFixedWidth(72)
        self.but4.setFont(font_but)
        self.but5 = PushBut1(self)
        self.but5.setText("")
        self.but5.setFixedWidth(72)
        self.but5.setFont(font_but)
        self.but6 = PushBut1(self)
        self.but6.setText("")
        self.but6.setFixedWidth(72)
        self.but6.setFont(font_but)
        self.but7 = PushBut1(self)
        self.but7.setText("")
        self.but7.setFixedWidth(72)
        self.but7.setFont(font_but)
        self.lb1 = QtWidgets.QLabel(self)
        self.lb1.setFixedWidth(72)
        self.lb1.setFixedHeight(72)
        self.grid1 = QtWidgets.QGridLayout()
        self.grid1.addWidget(self.textf, 0, 0, 14, 13)
        self.grid1.addWidget(self.but1, 0, 14, 1, 1)
        self.grid1.addWidget(self.but2, 1, 14, 1, 1)
        self.grid1.addWidget(self.but3, 2, 14, 1, 1)
        self.grid1.addWidget(self.but4, 3, 14, 1, 1)
        self.grid1.addWidget(self.but5, 4, 14, 1, 1)
        self.grid1.addWidget(self.but6, 5, 14, 1, 1)
        self.grid1.addWidget(self.but7, 6, 14, 1, 1)
        self.grid1.addWidget(self.lb1, 12, 14, 1, 1)
        self.grid1.setContentsMargins(7, 7, 7, 7)
        self.setLayout(self.grid1)
        self.but1.clicked.connect(self.on_but1)
        self.but2.clicked.connect(self.on_but2)

    def on_but1(self):
        self.textf.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(1,255,217,100); color: rgba(0,190,255,255);"
                                 "border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: rgba(0,140,255,255);")

    def on_but2(self):
        txt = self.textf.toPlainText()
        try:
            img = QtGui.QPixmap(txt)
            self.lb1.setPixmap(img.scaledToWidth(72, QtCore.Qt.SmoothTransformation))
        except:
            pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    desktop = QtWidgets.QApplication.desktop()
    resolution = desktop.availableGeometry()
    myapp = PyQtApp()
    myapp.setWindowOpacity(0.95)
    myapp.show()
    myapp.move(resolution.center() - myapp.rect().center())
    sys.exit(app.exec_())
else:
    desktop = QtWidgets.QApplication.desktop()
    resolution = desktop.availableGeometry()

# class App(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.title = 'PyQt5 file dialogs - pythonspot.com'
#         self.left = 10
#         self.top = 10
#         self.width = 640
#         self.height = 480
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#
#         self.openFileNameDialog()
#         self.openFileNamesDialog()
#         self.saveFileDialog()
#
#         self.show()
#
#     def openFileNameDialog(self):
#         options = QFileDialog.Options()
#         options |= QFileDialog.DontUseNativeDialog
#         fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
#         if fileName:
#             print(fileName)
#
#     def openFileNamesDialog(self):
#         options = QFileDialog.Options()
#         options |= QFileDialog.DontUseNativeDialog
#         files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
#         if files:
#             print(files)
#
#     def saveFileDialog(self):
#         options = QFileDialog.Options()
#         options |= QFileDialog.DontUseNativeDialog
#         fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
#         if fileName:
#             print(fileName)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())
