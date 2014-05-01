import json
import urllib2
import itertools
from datetime import datetime
import dateutil.parser
import time

infile = open('urls.txt', 'r')
print("the file has succesfully opened")

'''i = 1
j = 1'''

dates = []
dateArray = []

dateObject = ['','']
myDict = {}

file2 = open('data.json', 'w')
for line in infile:
    line.strip()
    if not (line.find("|2014-")==-1):
        splitIndex = line.find("|2014-") #find out where to split the damn string
        splitIndex2 = line.find("|")
        
        dateArrayIndex_dateTime = line[splitIndex+1:splitIndex+20] #copy date into a var
        dateArrayIndex_url = line[0:splitIndex2]    #copy url into a var
        dateArrayIndex_justDate = line[splitIndex+1:splitIndex+11]
        dateArrayIndex_justTime = line[splitIndex+12:splitIndex+20]

        myTuple = (dateArrayIndex_justTime, dateArrayIndex_url)
        text_date = dateArrayIndex_justDate + " " + dateArrayIndex_justTime
        test = dateutil.parser.parse(text_date)
        unix_time = time.mktime(test.timetuple())+1e-6*test.microsecond
        
        myDict[unix_time] = dateArrayIndex_url


d  = json.dumps(myDict, indent=2)
file2.write(d)
file2.close()
print d

'''for data in dateArray:
    print dateArray
    print '\n'
        #dateArray is where all your dates and URLs are stored in the format ['date','url']
'''

