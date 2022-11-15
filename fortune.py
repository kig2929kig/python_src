# 네이버 오늘의 운세

import requests, shutil
from bs4 import BeautifulSoup

class Stdout_Font:
    Reset      = '\033[0m'
    Bold       = '\033[1m'
    Italic     = '\033[3m'
    Underline  = '\033[4m'

    Red        = '\033[91m'
    Green      = '\033[92m'
    Yellow     = '\033[93m'
    Blue       = '\033[94m'
    Purple     = '\033[95m'
    Cyan       = '\033[96m'

    BG_Red     = '\033[101m'
    BG_Green   = '\033[102m'
    BG_Yellow  = '\033[103m'
    BG_Blue    = '\033[104m'
    BG_Purple  = '\033[105m'
    BG_Cyan    = '\033[106m'

born_line = """\
        (\\w/)
        (..  \\
       _/  )  \______
      (oo /'\        )`,
       `--' (v  __( / ||
             |||  ||| ||
            //_| //_|    
"""

lst = list()
year = list()
fortune_today = list()
htmls = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EB%A7%90%EB%9D%A0%20%EC%9A%B4%EC%84%B8')

if htmls.status_code == 200 : # <response [200]> - connected to the Internet! 
    #print(htmls)
    #print(htmls.text)
    bs = BeautifulSoup(htmls.content, 'html.parser')

    for meta in bs.find_all('dd'):
        lst.append(meta.get_text())
    for meta in bs.find_all('dt'):
        year.append(meta.get_text())
    for meta in bs.find_all('p', class_="text _cs_fortune_text"):
        fortune_today.append(meta.get_text())

else :
    print("Not connected to Internet!")

print()
print(born_line)
title = Stdout_Font.Underline + year[2] + Stdout_Font.Reset
print(title.center(shutil.get_terminal_size().columns) + '\n')
print(Stdout_Font.Green + fortune_today[0] + Stdout_Font.Reset) #오늘 0 : 내일 1 등
print(Stdout_Font.Purple + lst[2] + Stdout_Font.Reset)
