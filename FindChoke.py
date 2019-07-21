#!/usr/bin/python3

# Find Choke
# Author: Murmurtwins

import requests, json, math
url='http://akatsuki.pw/api/v1/users/scores/best?mode=0&p='
url2='https://akatsuki.pw/api/v1/users/rxfull?id=4391'
page='2'
url3='&l=100&rx=1&id=4391'
fullurl=url+page+url3
r=requests.get(fullurl)
r2=requests.get(url2)
result=json.loads(r.text)
result2=json.loads(r2.text)
scores=result['scores']
pp=result2['std']['pp']

print('You have',pp,'pp in total.')
print('On page',page,'of API, you choked on the following maps:')

item=0
count=1
max_combomap=0
max_comboyou=0
misscount=0
information=''
while item<100:
	misscount=scores[item]['count_miss']
	max_combomap=scores[item]['beatmap']['max_combo']
	max_comboyou=scores[item]['max_combo']
	if misscount==0 & max_combomap-max_comboyou<=3:
		item+=1
	else:
		information=scores[item]['beatmap']['song_name']
		print(count,':',information,' ',misscount,'miss',max_comboyou,'/',max_combomap)
		item+=1
		count+=1
