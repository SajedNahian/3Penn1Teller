import json
from urllib import request

#read us.json
f = open("us.json",'r')
fContent= f.read()
f.close()
d=json.loads(fContent)

#get states information from us.json
states=d['objects']['usStates']['geometries']

#states-abbreviation
url='https://gist.githubusercontent.com/mshafrir/2646763/raw/8b0dbb93521f5d6889502305335104218454c2bf/states_hash.json'
resp = request.urlopen(url)
abbrNm = json.loads(resp.read())

#our data
"""--------------------------modify date=--------------------"""
date='01012015'

url='https://raw.githubusercontent.com/frankbi/price-of-weed/master/data/weedprices'+date+'.csv'

#url='https://raw.githubusercontent.com/frankbi/price-of-weed/master/data/weedprices01012015.csv'
canaPfileLines=request.urlopen(url)

canaPfileLines=str(canaPfileLines.read())
#print(canaPfileLines)
canaPfileLines=canaPfileLines.split('\\r\\n')
#print(canaPfileLines)
cana={}
for line in canaPfileLines:
    line = line.split(',')
    cana[line[0]]=line[1:]

    #print(line[0])
#print(cana.keys())
#print(cana['"Hawaii"'])

#provide content to new us.json
for state in states:
    stNM='"'+abbrNm[state['properties']['STATE_ABBR']]+'"'
    if stNM != '"District Of Columbia"':
        state['WEED_PRICE']=cana[stNM][0]
        #------------------------may add more information here------------------


#print(d)


fo = open("data/us2.json",'w')
fo.write(str(d))
fo.close()
