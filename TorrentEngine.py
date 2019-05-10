# **************************************************************************** #
#                                                                              #
#    Name :TorrentEngine.py                      :::     ::::::::      :::     #
#                                              :+:      :+:   :+:    :+:       #
#    By: karma, estelle, eyyup               +:+ +:+   +:+   +:+   +:+ +:+     #
#                                          +#+  +:+   +#+   +#+  +#+  +:+      #
#    Create:2019/05/10 02:08:05          +#+#+#+#+#+ +#+   +#+ +#+#+#+#+#+     #
#                                             #+#   #+#   #+#       #+#        #
#          by karma                         ###   #########       ###.error    #
#                                                                              #
# **************************************************************************** #


import libtorrent as lt
import time
from PyQt5.QtGui import (QCloseEvent, QStandardItem, QStandardItemModel)
from threading import Thread
from PyQt5.QtWidgets import (QAbstractItemView, QAction, QApplication,
							QFileDialog, QGridLayout, QInputDialog, QLineEdit,
							QMainWindow, QPushButton, QTableView,
							QTableWidget, QTableWidgetItem, QVBoxLayout,
							QWidget)

class	NewTorrent(Thread):

	def		__init__(self, data):
		Thread.__init__(self)
		self.data = data
		self.statupd = False
		self.state = True
		self.pause = False
		self.nrow = 0

	def run(self):
		nameFile = self.data['src'].split('/')
		self.file = nameFile[len(nameFile) - 1].split('.')[0]
		self.initVal()
		self.connected()

	def		AddTorrent(self):
		self.ses = lt.session({'listen_interfaces': '0.0.0.0:8080'})
		self.info = lt.torrent_info(self.data['src'])
		self.h = self.ses.add_torrent({'ti': self.info, 'save_path': self.data['dest']})
		self.status = self.h.status()
		self.data['model'].item(self.nrow, 8).setText(
			self.formatByte(self.info.total_size(), "Gb"))
		self.sizeData = self.formatByte(self.info.total_size(), 'Kb', 0)

	def		connected(self):
		self.AddTorrent()
		self.data['model'].item(self.nrow, 1).setText(str(self.status.name))

		while (self.state == True):
			self.status = self.h.status()
			if (self.statupd == True):
				self.update()
				self.statupd = False
			if (self.pause == True):
				self.data['model'].item(self.nrow, 0).setText("Pause")
				while (self.state == True and self.pause == True):
					time.sleep(1)
			else:
				self.display()
			time.sleep(1)

	def		display(self):
		self.data['model'].item(self.nrow, 0).setText(
				str(self.status.state))
		self.data['model'].item(self.nrow, 2).setText(
			str(int(self.status.progress * 100)) + "%")
		self.data['model'].item(self.nrow, 3).setText(
			str(self.status.num_peers))
		self.data['model'].item(self.nrow, 4).setText(
			str(self.status.num_peers - self.status.num_seeds))
		self.data['model'].item(self.nrow, 6).setText(
			str(int(self.status.upload_rate / 1000)) + "kB/s")
		self.data['model'].item(self.nrow, 5).setText(
			str(int(self.status.download_rate / 1000)) + "kB/s")
		if (self.status.download_rate > 0 and not self.status.is_seeding):
			self.data['model'].item(self.nrow, 7).setText(
				str(int(
					(self.sizeData / (self.status.download_rate / 1000))
					/ 60)) + " min")

	def		initVal(self):
		values = ['Dl',self.file, '0%', '0', '0', "NAN", "NAN", "NAN", "NAN"]
		row = []
		for val in values:
			cell = QStandardItem(str(val))
			row.append(cell)
		self.data['model'].appendRow(row)
		self.nrow = self.data['model'].rowCount() - 1

	def		formatByte(self, nb, flag = -1, flag2 = -1):
		label = ['b', 'Kb', 'Mb', 'Gb', 'Tb']
		if (nb < 0):
			return (False)
		if (is_inarray(label, flag) == True):
			flag = label.index(flag)
		n = 1
		c2 = 0
		c = 10
		while ((c / 10) >= 1 and c2 <= flag):
			c = nb / n
			n = n * 1000
			c2 += 1
		if (flag2 == -1):
			return(str(int(c * 1000) / 1000) + label[c2 - 1])
		return (int((c * 1000) / 1000))

def		is_inarray(table, stri):
	for item in table:
		if (item == stri):
			return (True)
	return (False)

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