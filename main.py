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

from ui.main_ui import Ui_MainWindow

# from PySide6.QtUiTools import loadUiType
# form_class = loadUiType("./ui/main.ui")[0]
# class Ui_MainWindow_Override(form_class):

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
    print("dbAdd message")

  def dbDel(self):
    print("dbDel message")

  def dbFind(self):
    print("dbFind message")

class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    self.ui = Ui_MainWindow_Override()
    self.ui.setupUi(self)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())