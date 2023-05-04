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
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
# from PySide6.QtUiTools import loadUiType

from ui.main_ui import Ui_MainWindow as Main
from ui.dbAdd_ui import Ui_MainWindow as Add
from ui.dbDel_ui import Ui_MainWindow as Del
from ui.dbFind_ui import Ui_MainWindow as Find

# Main = loadUiType("./ui/main.ui")[0]
# Add = loadUiType("./ui/dbAdd.ui")[0]
# Del = loadUiType("./ui/dbDel.ui")[0]
# Find = loadUiType("./ui/dbFind.ui")[0]

class Ui_MainWindow_Override(Main):
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
    print("dbAdd message")

  def dbDel(self):
    print("dbDel message")

  def dbFind(self):
    self.window = dbFindWindow()
    self.window.show()

class Ui_dbAddWindow_Override(Add):
  def __init__(self):
    pass
  
  def setupUi(self, MainWindow):
    super().setupUi(MainWindow)
  
  def retranslateUi(self, MainWindow):
    super().retranslateUi(MainWindow)

class Ui_dbDelWindow_Override(Del):
  def __init__(self):
    pass
  
  def setupUi(self, MainWindow):
    super().setupUi(MainWindow)
  
  def retranslateUi(self, MainWindow):
    super().retranslateUi(MainWindow)

class Ui_dbFindWindow_Override(Find):
  def __init__(self):
    pass
  
  def setupUi(self, MainWindow):
    super().setupUi(MainWindow)
  
  def retranslateUi(self, MainWindow):
    super().retranslateUi(MainWindow)

class dbMainWindow(QMainWindow):
  def __init__(self):
    super(dbMainWindow, self).__init__()
    self.ui = Ui_MainWindow_Override()
    self.ui.setupUi(self)

class dbAddWindow(QMainWindow):
  def __init__(self):
    super(dbAddWindow, self).__init__()
    self.ui = Ui_dbAddWindow_Override()
    self.ui.setupUi(self)

class dbDelWindow(QMainWindow):
  def __init__(self):
    super(dbDelWindow, self).__init__()
    self.ui = Ui_dbDelWindow_Override()
    self.ui.setupUi(self)

class dbFindWindow(QMainWindow):
  def __init__(self):
    super(dbFindWindow, self).__init__()
    self.ui = Ui_dbFindWindow_Override()
    self.ui.setupUi(self)

app = QApplication(sys.argv)

window = dbMainWindow()
window.show()

sys.exit(app.exec())