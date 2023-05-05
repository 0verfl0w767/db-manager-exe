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
from PySide6.QtWidgets import QMainWindow, QMessageBox

import mysql.connector

from ui.base.dbAdd_ui import Ui_MainWindow

# from PySide6.QtUiTools import loadUiType
# form_class = loadUiType('./base/dbAdd.ui')[0]
class dbAddWindow(QMainWindow):
  def __init__(self):
    super(dbAddWindow, self).__init__()
    
    self.ui = Ui_MainWindow_Override()
    self.ui.setupUi(self)

class Ui_MainWindow_Override(Ui_MainWindow):
  def __init__(self):
    pass
  
  def setupUi(self, MainWindow):
    super().setupUi(MainWindow)
  
  def retranslateUi(self, MainWindow):
    super().retranslateUi(MainWindow)
    
    self.pushButton_1.clicked.connect(self.dbAdd)
    
  def dbAdd(self):
    if (self.lineEdit_1.text() == '' or
        self.lineEdit_2.text() == '' or
        self.lineEdit_3.text() == ''
      ):
      warning = QMessageBox()
      warning.setWindowTitle('Warning')
      warning.setText('Enter the correct value')
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
      SQL = 'INSERT INTO user (student_id, student_name, student_amount, student_note) VALUES(%s, %s, %s, %s)'
      VAL = (self.lineEdit_1.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text())
      cursor.execute(SQL, VAL)
      cnx.commit()
    except Exception as error:
      print(error)
    finally:
      cursor.close()
      cnx.close()
    self.label_5.setText(f'Added data successfully.')
    self.label_5.setStyleSheet("color: blue;")