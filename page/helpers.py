
# helper files for generate_collection.py
import re
from datetime import datetime

# helper class
class ReleaseItem:
  def __init__(self, id = "", title = "", artist = "", im_url = ""):
    self.id = id
    self.title = title
    self.artist = artist
    self.im_url = im_url

# get rid of 'an', 'a', 'the' in artist names
def removeArticles(text):
  return re.sub('(?i)(?:(the |a |an ))', '', text)

# get current date
def getDate(): 
    return datetime.today().strftime('%d-%m-%Y')
  
# read token from file 
def getToken():
    fo = open("token.txt", "r")
    return fo.readline()