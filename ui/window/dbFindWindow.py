#
#     ____                  __________
#    / __ \_   _____  _____/ __/ / __ \_      __
#   / / / / | / / _ \/ ___/ /_/ / / / / | /| / /
#  / /_/ /| |/ /  __/ /  / __/ / /_/ /| |/ |/ /
#  \____/ |___/\___/_/  /_/ /_/\____/ |__/|__/
# 
#  The copyright indication and this authorization indication shall be
#  recorded in all copies or in important parts of the Software.
# 
#  @author 0verfl0w767
#  @link https://github.com/0verfl0w767
#  @license MIT LICENSE
#
from PySide6.QtWidgets import QMainWindow, QTableWidget, QMessageBox, QTableWidgetItem
from PySide6.QtTest import QTest

import asyncio
import aiomysql

import mysql.connector

from ui.base.dbFind_ui import Ui_MainWindow
from utils.Config import Config

# from PySide6.QtUiTools import loadUiType
# form_class = loadUiType('./base/dbFind.ui')[0]
class dbFindWindow(QMainWindow):
  def __init__(self):
    super(dbFindWindow, self).__init__()
    
    self.ui = Ui_MainWindow_Override()
    self.ui.setupUi(self)

class Ui_MainWindow_Override(Ui_MainWindow):
  def __init__(self):
    self.config = Config()
    self.data = []
  
  def setupUi(self, MainWindow):
    super().setupUi(MainWindow)
  
  def retranslateUi(self, MainWindow):
    super().retranslateUi(MainWindow)
    
    self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
    
    self.pushButton_1.clicked.connect(self.dbFind_1)
    self.pushButton_2.clicked.connect(self.dbFind_2)
    self.pushButton_3.clicked.connect(self.dbFind_3)
    self.pushButton_4.clicked.connect(self.dbFind_4)
    self.pushButton_5.clicked.connect(self.dbFind_5)

  async def getData(self, loop, sql, var):
    mysql_config = self.config.getData('mysql_config.json')
    pool = await aiomysql.create_pool(
      loop=loop,
      host=mysql_config['host'],
      port=mysql_config['port'],
      user=mysql_config['user'],
      password=mysql_config['password'],
      db=mysql_config['database']
    )
    async with pool.acquire() as connection:
      async with connection.cursor() as cursor:
        SQL = 'select * from user where ' + sql + ' like CONCAT(\'%%\', %s, \'%%\')'
        VAR = (var, )
        await cursor.execute(SQL, VAR)
        self.data = await cursor.fetchall()
        # row = await cursor.fetchone()
        # while row is not None:
        #   self.DATA.append(row)
        #   row = await cursor.fetchone()
    pool.close()
    await pool.wait_closed()
  
  async def getAllData(self, loop):
    mysql_config = self.config.getData('mysql_config.json')
    pool = await aiomysql.create_pool(
      loop=loop,
      host=mysql_config['host'],
      port=mysql_config['port'],
      user=mysql_config['user'],
      password=mysql_config['password'],
      db=mysql_config['database']
    )
    async with pool.acquire() as connection:
      async with connection.cursor() as cursor:
        await cursor.execute('select * from user')
        self.data = await cursor.fetchall()
        # row = await cursor.fetchone()
        # while row is not None:
        #   self.DATA.append(row)
        #   row = await cursor.fetchone()
    pool.close()
    await pool.wait_closed()

  def dbFind_1(self):
    if self.lineEdit_PK.text() == '':
      warning = QMessageBox()
      warning.setWindowTitle('Warning')
      warning.setText('Enter the private key.')
      warning.exec()
      return
    
    self.start()
    self.pushButton_1.setDisabled(True)
    
    QTest.qWait(1000 * 1) # 1 second delay
    
    try:
      loop = asyncio.get_event_loop()
      loop.run_until_complete(self.getData(loop, 'id', self.lineEdit_PK.text()))
    except Exception as error:
      print(error)
    
    self.tableWidget.setRowCount(len(self.data))
    
    count = 0
    for row in self.data:
      self.tableWidget.setItem(count, 0, QTableWidgetItem(str(row[0])))
      self.tableWidget.setItem(count, 1, QTableWidgetItem(row[1]))
      self.tableWidget.setItem(count, 2, QTableWidgetItem(row[2]))
      self.tableWidget.setItem(count, 3, QTableWidgetItem(row[3]))
      self.tableWidget.setItem(count, 4, QTableWidgetItem(row[4]))
      count += 1
    
    self.end(count)
    self.pushButton_1.setEnabled(True)

  def dbFind_2(self):
     
    if self.lineEdit_SN1.text() == '':
      warning = QMessageBox()
      warning.setWindowTitle('Warning')
      warning.setText('Enter the student id.')
      warning.exec()
      return
    
    self.start()
    self.pushButton_2.setDisabled(True)
    
    QTest.qWait(1000 * 1) # 1 second delay
    
    try:
      loop = asyncio.get_event_loop()
      loop.run_until_complete(self.getData(loop, 'student_id', self.lineEdit_SN1.text()))
    except Exception as error:
      print(error)
    
    self.tableWidget.setRowCount(len(self.data))
    
    count = 0
    for row in self.data:
      self.tableWidget.setItem(count, 0, QTableWidgetItem(str(row[0])))
      self.tableWidget.setItem(count, 1, QTableWidgetItem(row[1]))
      self.tableWidget.setItem(count, 2, QTableWidgetItem(row[2]))
      self.tableWidget.setItem(count, 3, QTableWidgetItem(row[3]))
      self.tableWidget.setItem(count, 4, QTableWidgetItem(row[4]))
      count += 1
    
    self.end(count)
    self.pushButton_2.setEnabled(True)

  def dbFind_3(self):
    if self.lineEdit_SN2.text() == '':
      warning = QMessageBox()
      warning.setWindowTitle('Warning')
      warning.setText('Enter the student name.')
      warning.exec()
      return
    
    self.start()
    self.pushButton_3.setDisabled(True)
    
    QTest.qWait(1000 * 1) # 1 second delay
    
    try:
      loop = asyncio.get_event_loop()
      loop.run_until_complete(self.getData(loop, 'student_name', self.lineEdit_SN2.text()))
    except Exception as error:
      print(error)
    
    self.tableWidget.setRowCount(len(self.data))
    
    count = 0
    for row in self.data:
      self.tableWidget.setItem(count, 0, QTableWidgetItem(str(row[0])))
      self.tableWidget.setItem(count, 1, QTableWidgetItem(row[1]))
      self.tableWidget.setItem(count, 2, QTableWidgetItem(row[2]))
      self.tableWidget.setItem(count, 3, QTableWidgetItem(row[3]))
      self.tableWidget.setItem(count, 4, QTableWidgetItem(row[4]))
      count += 1
    
    self.end(count)
    self.pushButton_3.setEnabled(True)
  
  def dbFind_4(self):
    if self.lineEdit_SA.text() == '':
      warning = QMessageBox()
      warning.setWindowTitle('Warning')
      warning.setText('Enter the student amount.')
      warning.exec()
      return
    
    self.start()
    self.pushButton_4.setDisabled(True)
    
    QTest.qWait(1000 * 1) # 1 second delay
    
    try:
      loop = asyncio.get_event_loop()
      loop.run_until_complete(self.getData(loop, 'student_amount', self.lineEdit_SA.text()))
    except Exception as error:
      print(error)
    
    self.tableWidget.setRowCount(len(self.data))
    
    count = 0
    for row in self.data:
      self.tableWidget.setItem(count, 0, QTableWidgetItem(str(row[0])))
      self.tableWidget.setItem(count, 1, QTableWidgetItem(row[1]))
      self.tableWidget.setItem(count, 2, QTableWidgetItem(row[2]))
      self.tableWidget.setItem(count, 3, QTableWidgetItem(row[3]))
      self.tableWidget.setItem(count, 4, QTableWidgetItem(row[4]))
      count += 1
    
    self.end(count)
    self.pushButton_4.setEnabled(True)

  def dbFind_5(self):
    self.start()
    self.pushButton_5.setDisabled(True)
    
    QTest.qWait(1000 * 1) # 1 second delay
    
    try:
      loop = asyncio.get_event_loop()
      loop.run_until_complete(self.getAllData(loop))
    except Exception as error:
      print(error)
    
    self.tableWidget.setRowCount(len(self.data))
    
    count = 0
    for row in self.data:
      self.tableWidget.setItem(count, 0, QTableWidgetItem(str(row[0])))
      self.tableWidget.setItem(count, 1, QTableWidgetItem(row[1]))
      self.tableWidget.setItem(count, 2, QTableWidgetItem(row[2]))
      self.tableWidget.setItem(count, 3, QTableWidgetItem(row[3]))
      self.tableWidget.setItem(count, 4, QTableWidgetItem(row[4]))
      count += 1
    
    self.end(count)
    self.pushButton_5.setEnabled(True)
  
  def start(self):
    self.label_1.setStyleSheet("color: red;")
    self.label_1.setText(f'Wait a few seconds.')
  
  def end(self, count):
    self.label_1.setStyleSheet("color: blue;")
    self.label_1.setText(f'{count} results in datas.')