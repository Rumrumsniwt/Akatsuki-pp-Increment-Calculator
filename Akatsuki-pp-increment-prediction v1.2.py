#!/usr/bin/python3

# PP increment calculator v1.2
# Author: Murmurtwins

import requests, json, math
url='http://akatsuki.pw/api/v1/users/scores/best?mode=0&p=1&l=200&rx=1&id=4391'
url2='https://akatsuki.pw/api/v1/users/rxfull?id=4391'
r=requests.get(url)
r2=requests.get(url2)
result=json.loads(r.text)
result2=json.loads(r2.text)
scores=result['scores']
pp=result2['std']['pp']

pp_inc=float(79) # For single score calculation

pp_inc2=float(79) # For multiple score calculation

pp_bonus=float(850) # Bonus pp score

pp_needed=int(0) # How much pp needed

bonusscore_count=int(0) # How many scores with the given bonus pp needed

pplist=[]

def rawpp(amount):
	item, raw_pp=0,0
	while item<amount:
		raw_pp+=scores[item]['pp']*pow(0.95,item)
		pplist.append(scores[item]['pp'])
		item+=1
	return raw_pp

def actualpp(amount):
	item, raw_pp=0,0
	while item<amount:
		raw_pp+=pplist[item]*pow(0.95,item)
		item+=1
	return raw_pp

res_pp=pp-rawpp(99)

i=0
while i<=3000:
	ppafter=pp
	pplist.append(i)
	pplist.sort(reverse=True)
	rawpp2=actualpp(99)
	ppafter=rawpp2+res_pp
	pplist.remove(i)
	i+=0.1
	if ppafter-pp>=pp_inc:
		break
pp_needed=i

num=0
while num<=5000:
	ppafter=pp
	pplist.append(pp_bonus)
	pplist.sort(reverse=True)
	rawpp3=actualpp(99)
	ppafter=rawpp3+res_pp
	num+=1
	if ppafter-pp>=pp_inc2:
		break
bonusscore_count=num

print('You have',pp,'pp in total.')
print('If you want to gain',pp_inc,'pp, you need to get a',pp_needed,'pp score.')

if num>=5000:
	print('If you want to gain',pp_inc2,'pp by getting multiple',pp_bonus,'pp scores, that is impossible.')
	print('The maximum bonus pp obtained is:',ppafter-pp,'pp.')
else:
	print('If you want to gain',pp_inc2,'pp by getting multiple',pp_bonus,'pp scores, you need at least',bonusscore_count,'.')