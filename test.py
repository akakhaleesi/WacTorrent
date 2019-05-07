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
import random
from pprint import pprint
import subprocess
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtWidgets import QMainWindow,QTableWidget,QAbstractItemView,QTableView,QGridLayout,QVBoxLayout,QTableWidgetItem, QPushButton,QWidget, QApplication, QInputDialog, QLineEdit, QFileDialog

class	FolderFile(QWidget):

	def explorer(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		file_location, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName(~/Dowload)", "","Torrent Files (*.torrent);;All Files (*)", options=options)
		if file_location:
			return (file_location)

	def explorerDestination(self):
		folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
		if folder:
			return (folder)

	def initDL(self, src, dest):
		print(dest)

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
		self.setWindowTitle("toto")
		self.window = QWidget()
		# self.table = ['pause', 'delete', 'dl', getattr(FileTorrent, "FileTorrent")]
		self.window.setGeometry(600, 600, 600, 490)
		self.layout = QVBoxLayout()
		self.TorrentButton()
		self.layout.addWidget(self.btn1)
		self.InitNavBar()
		self.layout.addWidget(self.tableview)
		self.window.setLayout(self.layout)
		self.window.show()
		

	def		InitNavBar(self):
		header = ['file', "toto"]
		self.model = QStandardItemModel()
		self.model.setHorizontalHeaderLabels(['Status', 'File', 'Progress',
		'Seeder', 'Leecher'])
		self.tableview = QTableView()
		self.tableview.setModel(self.model)
		self.tableview.setEditTriggers(QAbstractItemView.NoEditTriggers)
		# self.populate()

	# def populate(self):
	# 	# GENERATE A 4x10 GRID OF RANDOM NUMBERS.
	# 	# VALUES WILL CONTAIN A LIST OF INT.
	# 	# MODEL ONLY ACCEPTS STRINGS - MUST CONVERT.
	# 	values = []
	# 	for i in range(1):
	# 		sub_values = []
	# 		for i in range(4):
	# 			value = random.randrange(1, 100)
	# 			sub_values.append(value)
	# 		values.append(sub_values)
 
	# 	for value in values:
	# 		row = []
	# 		for item in value:
	# 			cell = QStandardItem(str(item))
	# 			row.append(cell)
	# 		self.model.appendRow(row)

	def		TorrentButton(self):
		self.btn1 = QPushButton("Add torrent", self)
		self.btn1.setFixedSize(100, 30)
		self.btn1.setGeometry(10, 10, 0, 0)
		self.btn1.move(0, 0)
		self.btn1.clicked.connect(self.buttonClicked)

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
		init = FolderFile()
		src = init.explorer()
		dest = init.explorerDestination()
		init.initDL(src, dest)
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
