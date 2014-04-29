import json
import urllib2
import itertools

infile = open('urls.txt', 'r')
print("the file has succesfully opened")

'''i = 1
j = 1'''

dates = []
dateArray = []

dateObject = ['','']


file2 = open('myJson.json', 'w')
for line in infile:
	line.strip()
	if not (line.find("|2014-")==-1):
		
		splitIndex = line.find("|2014") #find out where to split the damn string
		splitIndex2 = line.find("|")
		
		dateArrayIndex_date = line[splitIndex+1:splitIndex+20] #copy date into a var
		dateArrayIndex_url = line[0:splitIndex2]	#copy url into a var
		
		#append both url and date vars into one 'dates' obj  
		dates2 = dateArrayIndex_date, dateArrayIndex_url
		dateArray.append(dates2)
		#print '\n'


for dates2 in dateArray:
	print dates2

		#'dateArray' is an array of 'dates' objects
	
	#print dateArray
	#for data in dateArray:
	#	print data
for dates2 in dateArray:

	x  = json.dumps(dates2)
	file2.write(x)


'''for data in dateArray:
	print dateArray
	print '\n'
		#dateArray is where all your dates and URLs are stored in the format ['date','url']
'''

