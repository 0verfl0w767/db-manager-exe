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

import mysql.connector

from ui.base.dbFind_ui import Ui_MainWindow

# from PySide6.QtUiTools import loadUiType
# form_class = loadUiType('./base/dbFind.ui')[0]
class dbFindWindow(QMainWindow):
  def __init__(self):
    super(dbFindWindow, self).__init__()
    
    self.ui = Ui_MainWindow_Override()
    self.ui.setupUi(self)

class Ui_MainWindow_Override(Ui_MainWindow):
  def __init__(self):
    pass
  
  def setupUi(self, MainWindow):
    super().setupUi(MainWindow)
  
  def retranslateUi(self, MainWindow):
    super().retranslateUi(MainWindow)
    
    self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
    
    self.pushButton_1.clicked.connect(self.dbFind_1)
    self.pushButton_2.clicked.connect(self.dbFind_2)
  
  def dbFind_1(self):
    DATA = []
    if self.lineEdit_1.text() == '':
      warning = QMessageBox()
      warning.setWindowTitle('Warning')
      warning.setText('Enter the student number')
      button = warning.exec()
      return
    try:
      cnx = mysql.connector.connect(
        user='root',
        password='test1234',
        host='160.251.7.140',
        port='3306',
        database='cs'
      )
      cursor = cnx.cursor()
      cursor.execute('use cs')
      cursor.execute('select * from user')
      row = cursor.fetchone()
      while row is not None:
        DATA.append(row)
        row = cursor.fetchone()
    except Exception as e:
      print(e)
    finally:
      cursor.close()
      cnx.close()
    self.tableWidget.setRowCount(0)
    self.tableWidget.setRowCount(100)
    count = 0
    for row in DATA:
      self.tableWidget.setItem(count, 0, QTableWidgetItem(row[1]))
      self.tableWidget.setItem(count, 1, QTableWidgetItem(row[2]))
      self.tableWidget.setItem(count, 2, QTableWidgetItem(row[3]))
      self.tableWidget.setItem(count, 3, QTableWidgetItem(row[4]))
      count += 1
    self.label_3.setText(f'{count} results in datas.')
    self.label_3.setStyleSheet("color: blue;")

  def dbFind_2(self):
    pass