import requests
from bs4 import BeautifulSoup
import time
from openpyxl import Workbook, load_workbook



url ="https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo="

req = requests.get(url)

req.encoding="euc-kr"

bs = BeautifulSoup(req.text,"html.parser")

turn =bs.select("#article > div:nth-child(2) > div > div.win_result > h4 > strong")
numbers= bs.select("#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span")
bonus= bs.select("#article > div:nth-child(2) > div > div.win_result > div > div.num.bonus > p > span")
potmoney = bs.select("#article > div:nth-child(2) > div > table > tbody > tr> td:nth-child(4)")
date = bs.select('#article > div:nth-child(2) > div > div.win_result > p')
howmany = bs.select('#article > div:nth-child(2) > div > table > tbody > tr:nth-child(1) > td:nth-child(6)')

potmoneyAll =[]

for i in potmoney:
    potmoneyAll += [i.get_text()]

potmoneyAll