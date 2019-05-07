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

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow,QTableWidget, QVBoxLayout,QTableWidgetItem, QPushButton,QWidget, QApplication, QInputDialog, QLineEdit, QFileDialog

class	FolderFile(QWidget):
	# def __init__(self):
		# super().__init__()
		# return self.initUI()

	# def initUI(self):
		# return (self.openFileNameDialog())
		# self.openFileNamesDialog()
		# self.saveFileDialog()

	def explorer(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		file_location, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName(~/Dowload)", "","Torrent Files (*.torrent);;All Files (*)", options=options)
		if file_location:
			return (file_location)
	def initDL(self, file):
		print(file)

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

class	NewTorrent(QMainWindow):
	def __init(self):
		super().__init__()
		self.intDL()

	def initDL(self):
		print ("okok")


class	InitInterface(QMainWindow):
	def __init__(self):
		super().__init__()
		# self.table = ['pause', 'delete', 'dl', getattr(FileTorrent, "FileTorrent")]
		self.InitNavBar()

	def		InitNavBar(self):
		self.window = QWidget()
		self.layout = QVBoxLayout()
		self.TorrentButton()
		self.TableDl()
		self.setGeometry(600, 600, 490, 450)
		self.setWindowTitle('Event sender')
		self.window.setLayout(self.layout)
		self.show()

	def		TorrentButton(self):
		btn1 = QPushButton("Add torrent", self)
		btn1.move(0, 0)
		btn1.clicked.connect(self.buttonClicked)
		# self.table[3]()
		# for elem in self.table:
			# print(elem)

	def		TableDl(self):
		print ("dl")
		# self.corp = QLabel()
		# self.corp.setLineWidth = 400
		# self.corp.setRowCount(2)
		# self.corp.setColumnCount(1)
		# self.corp.setItem(0, 1,QTableWidgetItem("toto"))
		
		# self.corp.move(0, 50)

	def buttonClicked(self):
		sender = self.sender()
		ex2 = FolderFile().explorer()
		init = FolderFile()
		init.initDL(ex2)
		self.statusBar().showMessage(sender.text() + ' was pressed')


def		main():
	app = QApplication(sys.argv)
	ex = InitInterface()
	sys.exit(app.exec_())


main()
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
