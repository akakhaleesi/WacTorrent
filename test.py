#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#    Name :test.py                               :::     ::::::::      :::     #
#                                              :+:      :+:   :+:    :+:       #
#    By: karma                               +:+ +:+   +:+   +:+   +:+ +:+     #
#                                          +#+  +:+   +#+   +#+  +#+  +:+      #
#    Create:2019/05/06 10:59:42          +#+#+#+#+#+ +#+   +#+ +#+#+#+#+#+     #
#                                             #+#   #+#   #+#       #+#        #
#          by karma                         ###   #########       ###.error    #
#                                                                              #
# **************************************************************************** #

import libtorrent as lt
import time
import sys
import os
from pprint import pprint
import subprocess
# from PyQt5 import QtWidgets, QtGui, QtCore, Qt


from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QApplication, QInputDialog, QLineEdit, QFileDialog

class	FolderFile(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.openFileNameDialog()
		# self.openFileNamesDialog()
		# self.saveFileDialog()

	def openFileNameDialog(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
		if fileName:
			print(fileName)
	
	# def openFileNamesDialog(self):
	# 	options = QFileDialog.Options()
	# 	options |= QFileDialog.DontUseNativeDialog
	# 	files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
	# 	if files:
	# 		print(files)
	
	# def saveFileDialog(self):
	# 	options = QFileDialog.Options()
	# 	options |= QFileDialog.DontUseNativeDialog
	# 	fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
	# 	if fileName:
	# 		print(fileName)

class	NavButton(QMainWindow):
	
	def __init__(self):
		super().__init__()
		
		self.initUI()
		
		
	def initUI(self):
		btn1 = QPushButton("Add torrent", self)
		btn2 = QPushButton("Button 2", self)
		btn2.move(150, 0)
		btn1.clicked.connect(self.buttonClicked)
		btn2.clicked.connect(self.buttonClicked)
		self.statusBar()
		self.setGeometry(300, 300, 290, 150)
		self.setWindowTitle('Event sender')
		self.show()
		
		
	def buttonClicked(self):
		sender = self.sender()
		pprint(sender)
		ex2 = FolderFile()
		self.statusBar().showMessage(sender.text() + ' was pressed')

if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	ex = NavButton()
	sys.exit(app.exec_())
# ses = lt.session({'listen_interfaces': '0.0.0.0:443'})

# info = lt.torrent_info(sys.argv[1])
# h = ses.add_torrent({'ti': info, 'save_path': '.'})
# s = h.status()
# print('starting', s.name)

# while (not s.is_seeding):
#     s = h.status()

#     print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % (
#         s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
#         s.num_peers, s.state))

#     alerts = ses.pop_alerts()
#     for a in alerts:
#         if a.category() & lt.alert.category_t.error_notification:
#             print(a)

#     sys.stdout.flush()

#     time.sleep(1)

# print(h.name(), 'complete')
