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
from PySide6.QtWidgets import QMainWindow

import mysql.connector

from ui.base.dbDel_ui import Ui_MainWindow

# from PySide6.QtUiTools import loadUiType
# form_class = loadUiType('./base/dbDel.ui')[0]
class dbDelWindow(QMainWindow):
  def __init__(self):
    super(dbDelWindow, self).__init__()
    
    self.ui = Ui_MainWindow_Override()
    self.ui.setupUi(self)

class Ui_MainWindow_Override(Ui_MainWindow):
  def __init__(self):
    pass
  
  def setupUi(self, MainWindow):
    super().setupUi(MainWindow)
  
  def retranslateUi(self, MainWindow):
    super().retranslateUi(MainWindow)