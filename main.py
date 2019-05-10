#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#    Name :test.py                               :::     ::::::::      :::     #
#                                              :+:      :+:   :+:    :+:       #
#    By: karma, estelle, eyyup               +:+ +:+   +:+   +:+   +:+ +:+     #
#                                          +#+  +:+   +#+   +#+  +#+  +:+      #
#    Create:2019/05/06 10:59:42          +#+#+#+#+#+ +#+   +#+ +#+#+#+#+#+     #
#                                             #+#   #+#   #+#       #+#        #
#          by karma                         ###   #########       ###.error    #
#                                                                              #
# **************************************************************************** #

import os
import sys
import time
from pprint import pprint
from TorrentEngine import NewTorrent, FolderFile
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import (QCloseEvent, QStandardItem, QStandardItemModel)
from PyQt5.QtWidgets import (QAbstractItemView, QAction, QApplication,
							QFileDialog, QGridLayout, QInputDialog, QLineEdit,
							QMainWindow, QPushButton, QTableView,
							QTableWidget, QTableWidgetItem, QVBoxLayout,
							QWidget)

cell = ''
tableThread = []
torrentVal = ['Status', 'File', 'Progress',
		'Seeder', 'Leecher', 'Speed Up', 'Speed Dl','Time', 'size']

class	InitInterface(QMainWindow):
	def __init__(self):
		super().__init__()
		self.row = 0
		self.setWindowTitle("BayTorrent")
		self.window = QWidget()
		self.window.setGeometry(1000, 1000, 1000, 490)
		self.layout = QVBoxLayout()
		self.TorrentButton()
		self.PauseTorrent()
		self.PlayTorrent()
		self.BodyPannel()
		self.layout.addWidget(self.tableview)
		self.window.setLayout(self.layout)
		self.window.show()

	def		BodyPannel(self):
		self.model = QStandardItemModel()
		self.model.setHorizontalHeaderLabels(torrentVal)
		self.tableview = QTableView()
		self.tableview.setModel(self.model)
		self.tableview.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tableview.clicked.connect(self.viewClicked)

	def		TorrentButton(self):
		self.btnTorrent = QPushButton("Add torrent", self)
		self.btnTorrent.setFixedSize(100, 30)
		self.btnTorrent.setGeometry(10, 10, 0, 0)
		# self.btnTorrent.move(0, 0)
		self.btnTorrent.clicked.connect(self.buttonClicked)
		self.layout.addWidget(self.btnTorrent)
	
	def		PauseTorrent(self):
		self.btnPause = QPushButton("Pause", self)
		self.btnPause.setFixedSize(100, 30)
		self.btnPause.setGeometry(10, 10, 30, 0)
		self.btnPause.move(30, 30)
		self.btnPause.clicked.connect(self.Pause)
		self.layout.addWidget(self.btnPause)
	
	def		PlayTorrent(self):
		self.btnPlay = QPushButton("Play", self)
		self.btnPlay.setFixedSize(100, 30)
		self.btnPlay.setGeometry(10, 10, 0, 0)
		self.btnPlay.clicked.connect(self.Play)
		self.layout.addWidget(self.btnPlay)
	
	# def		DeleteTorrent(self):
	# 	self.btnDelete = QPushButton("Delete", self)
	# 	self.btnDelete.setFixedSize(100, 30)
	# 	self.btnDelete.setGeometry(10, 10, 0, 0)
	# 	self.btnDelete.clicked.connect(self.Delete)
	# 	self.layout.addWidget(self.btnDelete)

	def		Pause(self):
		tableThread[self.row].pause = True

	def		Play(self):
		tableThread[self.row].pause = False

	# def		Delete(self):
	# 	print ("delete")
	# 	tableThread[self.row].state = False
	# 	tableThread[self.row].join()
	# 	tableThread.remove(tableThread[self.row])
	# 	for item in tableThread:
	# 		item.statupd = True
	# 	tableThread.remove(tableThread[len(tableThread) - 1])

	def		buttonClicked(self):
		sender = self.sender()
		init = FolderFile()
		src = init.explorer()
		dest = init.explorerDestination()
		tableThread.append(NewTorrent({
			'src': src, 'dest': dest,'table': self.tableview,
			'model': self.model
			}))
		self.nb = self.model.rowCount()
		tableThread[len(tableThread) - 1].start()

	def		viewClicked(self, clickedIndex):
		self.row = clickedIndex.row()

def		close():
	c = 0
	while c < len(tableThread):
		tableThread[c].state = False
		tableThread[c].join()
		c = c + 1

def		main():
	app = QApplication(sys.argv)
	ex = InitInterface()
	app.aboutToQuit.connect(close)
	sys.exit(app.exec_())

main()
