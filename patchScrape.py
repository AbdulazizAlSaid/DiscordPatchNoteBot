import requests
from bs4 import BeautifulSoup
import re

class dexertoPatchScraper:
  patchPath = ''

  def __init__(self):
    self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.3'}
    self.url = 'https://www.dexerto.com'

  def search(self, patchCommand):
    if patchCommand == 'lol':
      self.url = 'https://www.dexerto.com/league-of-legends/'
      patchPath = '^https://www.dexerto.com/league-of-legends/lol-patch'
    if patchCommand == 'tft':
      self.url = 'https://www.dexerto.com/league-of-legends/'
      patchPath = '^https://www.dexerto.com/league-of-legends/teamfight-tactics-tft'
    if patchCommand == 'valo':
      self.url = 'https://www.dexerto.com/valorant/'
      patchPath = '^https://www.dexerto.com/valorant/valorant-patch'
    if patchCommand == 'apex':
      self.url = 'https://www.dexerto.com/apex-legends/'
      patchPath = '^https://www.dexerto.com/apex-legends/apex-legends-season-12-patch-notes'
    base = requests.get(self.url)
    soup = BeautifulSoup(base.content, 'html.parser')
    link = soup.find('a', href=re.compile(patchPath))
    final_link = link.get('href')

    return final_link 
