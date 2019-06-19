#!/usr/bin/python3

# PP increment calculator v1.0 
# Author: Murmurtwins

import requests, json, math, random
url='http://akatsuki.pw/api/v1/users/scores/best?mode=0&p=1&l=200&rx=1&id=4391'
r=requests.get(url)
result=json.loads(r.text)
scores=result['scores']
pp=float(16120) # Your current pp (needs modifying)

pp_inc=float(random.uniform(0,100)) # How much pp you want to increase (free to modify it!)

pp_needed=int(0) # How much pp needed
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
	i+=0.01
	if ppafter-pp>=pp_inc:
		break
pp_needed=i
print('If you want to gain',pp_inc,'pp, you need to get a',pp_needed,'pp score.')