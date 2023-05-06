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
import json
import os

class Config:
  def __init__(self):
    pass
  
  def getData(self, path):
    DATA_PATH = "../"
    REAL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), DATA_PATH + path))
    
    if not os.path.exists(REAL_PATH):
      print('File not found, ' + REAL_PATH)
      return
    
    with open(REAL_PATH, 'r', encoding="utf-8") as file:
      JSON_DATA = json.load(file)
      return JSON_DATA
  
  def setData(self, path, data, overwrite=True):
    DATA_PATH = "../"
    REAL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), DATA_PATH + path))
    
    if not overwrite and os.path.exists(REAL_PATH):
      print('Could not overwrite file, ' + REAL_PATH)
      return
    
    with open(REAL_PATH, 'w', encoding='utf-8') as file:
      json.dump(data, file, ensure_ascii=False, indent=2)