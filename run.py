#-*- coding:utf-8 -*
## 작업 스케줄로 11시50분마다 실행시키기
from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime
import os

response = urlopen('https://github.com/taehyundev')
soup = BeautifulSoup(response, 'html.parser')
now = datetime.datetime.now()
date = now.strftime('%Y-%m-%d')
print(date)
for commit_Data in soup.find_all(class_='day'):
    if commit_Data["data-date"] == date :
        now_commitData = int(commit_Data["data-count"])


if now_commitData == 0:
    os.system('autoPush.sh')
