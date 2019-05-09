# **************************************************************************** #
#                                                                              #
#    Name :Interface.py                          :::     ::::::::      :::     #
#                                              :+:      :+:   :+:    :+:       #
#    By: karma                               +:+ +:+   +:+   +:+   +:+ +:+     #
#                                          +#+  +:+   +#+   +#+  +#+  +:+      #
#    Create:2019/05/07 20:43:22          +#+#+#+#+#+ +#+   +#+ +#+#+#+#+#+     #
#                                             #+#   #+#   #+#       #+#        #
#          by karma                         ###   #########       ###.error    #
#                                                                              #
# **************************************************************************** #
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtWidgets import QMainWindow,QTableWidget,QAbstractItemView,QTableView,QGridLayout,QVBoxLayout,QTableWidgetItem, QPushButton,QWidget, QApplication, QInputDialog, QLineEdit, QFileDialog

class	InitInterface(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("toto")
		self.window = QWidget()
		self.window.setGeometry(600, 600, 600, 490)
		self.layout = QVBoxLayout()
		self.TorrentButton()
		self.layout.addWidget(self.btn1)
		self.InitNavBar()
		self.layout.addWidget(self.tableview)
		self.window.setLayout(self.layout)
		self.window.show()

	def		InitNavBar(self):
		self.model = QStandardItemModel()
		self.model.setHorizontalHeaderLabels(['Status', 'File', 'Progress',
		'Seeder', 'Leecher', 'Time'])
		self.tableview = QTableView()
		self.tableview.setModel(self.model)
		self.tableview.setEditTriggers(QAbstractItemView.NoEditTriggers)

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
		init.initDL(src, dest, self.tableview, self.model)
		self.statusBar().showMessage(sender.text() + ' was pressed')
