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

from ui.base.dbMain_ui import Ui_MainWindow
from ui.window.dbAddWindow import dbAddWindow
from ui.window.dbDelWindow import dbDelWindow
from ui.window.dbFindWindow import dbFindWindow

# from PySide6.QtUiTools import loadUiType
# form_class = loadUiType('./base/dbMain.ui')[0]
class dbMainWindow(QMainWindow):
  def __init__(self):
    super(dbMainWindow, self).__init__()
    
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
    self.pushButton_2.clicked.connect(self.dbDel)
    self.pushButton_3.clicked.connect(self.dbFind)
    
  def dbAdd(self):
    self.AddWindow = dbAddWindow()
    self.AddWindow.show()

  def dbDel(self):
    self.DelWindow = dbDelWindow()
    self.DelWindow.show()

  def dbFind(self):
    self.findWindow = dbFindWindow()
    self.findWindow.show()