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

from ui.base.dbAdd_ui import Ui_MainWindow
from utils.Config import Config

# from PySide6.QtUiTools import loadUiType
# form_class = loadUiType('./base/dbAdd.ui')[0]
class dbAddWindow(QMainWindow):
  def __init__(self):
    super(dbAddWindow, self).__init__()
    
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
    
    self.pushButton_1.clicked.connect(self.dbAdd)

  async def addData(self, loop):
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
        SQL = 'INSERT INTO user (student_id, student_name, student_amount, student_note) VALUES (%s, %s, %s, %s)'
        VAL = (self.lineEdit_1.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text())
        await cursor.execute(SQL, VAL)
        await connection.commit()
        self.data.append((cursor.lastrowid, self.lineEdit_1.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text()))
    pool.close()
    await pool.wait_closed()

  def dbAdd(self):
    if (self.lineEdit_1.text() == '' or
        self.lineEdit_2.text() == '' or
        self.lineEdit_3.text() == ''
      ):
      warning = QMessageBox()
      warning.setWindowTitle('Warning')
      warning.setText('Enter the correct value')
      warning.exec()
      return
    
    self.label_5.setStyleSheet("color: red;")
    self.label_5.setText(f'Wait a few seconds.')
    self.pushButton_1.setDisabled(True)
    
    QTest.qWait(1000 * 1) # 1 second delay
    
    try:
      loop = asyncio.get_event_loop()
      loop.run_until_complete(self.addData(loop))
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
    
    self.label_5.setStyleSheet("color: blue;")
    self.label_5.setText(f'Added data successfully.')
    self.pushButton_1.setEnabled(True)