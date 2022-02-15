import requests
from bs4 import BeautifulSoup
import re

class htmlScraper:
  def __init__(self):
    self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.3'}
    self.url = 'https://www.dexerto.com/league-of-legends/'

  def search(self):
    base = requests.get(self.url)
    soup = BeautifulSoup(base.content, 'html.parser')
    link = soup.find('a', href=re.compile('^https://www.dexerto.com/league-of-legends/lol-patch-'))
    final_link = link.get('href')

    return final_link 
