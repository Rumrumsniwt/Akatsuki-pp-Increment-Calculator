#!/usr/bin/python3

# Me and EmertxE
# Author: Murmurtwins

import requests, json, math
url='https://akatsuki.pw/api/v1/users/rxfull?id=21769'
url2='https://akatsuki.pw/api/v1/users/rxfull?id=4391'
url3='http://akatsuki.pw/api/v1/users/scores/recent?mode=0&p=1&l=100&rx=1&id=21769'
r=requests.get(url)
r2=requests.get(url2)
r3=requests.get(url3)
result=json.loads(r.text)
result2=json.loads(r2.text)
result3=json.loads(r3.text)
pp1=result['std']['pp']
pp2=result2['std']['pp']
name=result['username']
scores=result3['scores']
ppdiff=pp2-pp1


print('The difference between you and',name,'is',ppdiff,'pp at present')

item=0
count=1
max_combomap=0
max_comboyou=0
misscount=0
ppobtained=0
while item<100:
	misscount=scores[item]['count_miss']
	max_combomap=scores[item]['beatmap']['max_combo']
	max_comboyou=scores[item]['max_combo']
	ppobtained=scores[item]['pp']
	information=scores[item]['beatmap']['song_name']
	print(count,':',information,'|',misscount,'miss',max_comboyou,'/',max_combomap,'|',ppobtained,'pp')
	item+=1
	count+=1
