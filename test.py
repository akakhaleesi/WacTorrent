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
from threading import Thread
import subprocess
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtWidgets import QMainWindow,QTableWidget,QAbstractItemView,QTableView,QGridLayout,QVBoxLayout,QTableWidgetItem, QPushButton,QWidget, QApplication, QInputDialog, QLineEdit, QFileDialog

cell = ''
dlValue = {'status': 'Dl', 'dlstat': 0, 'seeders':0, 'leecher':0, 'time': 0 }
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

class	NewTorrent(Thread):

	def		__init__(self, data):
		Thread.__init__(self)
		self.data = data
		self.state = True
		self.nrow = 0

	def run(self):
		nameFile = self.data['src'].split('/')
		file = nameFile[len(nameFile) - 1].split('.')[0]
		# print(self.data['model'].rowCount())
		values = ['Dl',file, '0%', '0', '0', "NAN"]
		row = []
		for val in values:
			cell = QStandardItem(str(val))
			row.append(cell)
		self.data['model'].appendRow(row)
		self.nrow = self.data['model'].rowCount() - 1
		self.connected()

	def		connected(self):
		ses = lt.session({'listen_interfaces': '0.0.0.0:8080'})
		info = lt.torrent_info(self.data['src'])
		h = ses.add_torrent({'ti': info, 'save_path': self.data['dest']})
		status = h.status()
		while (not status.is_seeding and self.state == True):
			print("=======================")
			print(self.nrow)
			status = h.status()
			print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % (
			status.progress * 100, status.download_rate / 1000, status.upload_rate / 1000,
				status.num_peers, status.state))
			alerts = ses.pop_alerts()
			for a in alerts:
				if a.category() & lt.alert.category_t.error_notification:
						print(a)
			sys.stdout.flush()
			time.sleep(1)

		if (self.state == False):
			print(self.nrow)
			self.data['model'][self.nrow.row()][0] = "Pause"
		print(h.name(), 'complete')


class	InitInterface(QMainWindow):
	def __init__(self):
		super().__init__()
		self.tableThread = []
		self.row = 0
		self.setWindowTitle("BayTorrent")
		self.window = QWidget()
		self.window.setGeometry(1000, 1000, 1000, 490)
		self.layout = QVBoxLayout()
		self.TorrentButton()
		self.layout.addWidget(self.btn1)
		self.BodyPannel()
		self.layout.addWidget(self.tableview)
		self.window.setLayout(self.layout)
		self.window.show()
		

	def		BodyPannel(self):
		self.model = QStandardItemModel()
		self.model.setHorizontalHeaderLabels(['Status', 'File', 'Progress',
		'Seeder', 'Leecher', 'Time'])
		self.tableview = QTableView()
		self.tableview.setModel(self.model)
		self.tableview.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tableview.clicked.connect(self.viewClicked)

	def		TorrentButton(self):
		self.btn1 = QPushButton("Add torrent", self)
		self.btn1.setFixedSize(100, 30)
		self.btn1.setGeometry(10, 10, 0, 0)
		self.btn1.move(0, 0)
		self.btn1.clicked.connect(self.buttonClicked)

	def buttonClicked(self):
		sender = self.sender()
		init = FolderFile()
		src = init.explorer()
		dest = init.explorerDestination()
		self.tableThread.append(NewTorrent({'src': src, 'dest': dest, 'table': self.tableview,
		'model': self.model}))
		self.nb = self.model.rowCount()
		self.tableThread[len(self.tableThread) - 1].start()

	def		viewClicked(self, clickedIndex):
		row = clickedIndex.row()
		self.row = row
		self.tableThread[row].state = False


def		main():
	app = QApplication(sys.argv)
	ex = InitInterface()
	sys.exit(app.exec_())


main()

