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

for line in infile:
	line.strip()
	if not (line.find("|2014")==-1):
		
		splitIndex = line.find("|2014") #find out where to split the damn string
		
		dateArrayIndex_date = line[splitIndex+1:] #copy date into a var
		dateArrayIndex_url = line[0:splitIndex]	#copy url into a var
		
		#append both url and date vars into one 'dates' obj  
		dates.append(dateArrayIndex_date)
		dates.append(dateArrayIndex_url)


		#'dateArray' is an array of 'dates' objects
		dateArray.append(dates)

for data in dateArray:
	print data, '\n'




'''for dat in dateArray:
	print dateArray
	print '\n'
		#dateArray is where all your dates and URLs are stored in the format ['date','url']
'''

