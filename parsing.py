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
myDict = {}

file2 = open('myJson_test.json', 'w')
for line in infile:
	line.strip()
	if not (line.find("|2014-")==-1):
		
		splitIndex = line.find("|2014") #find out where to split the damn string
		splitIndex2 = line.find("|")
		
		dateArrayIndex_dateTime = line[splitIndex+1:splitIndex+20] #copy date into a var
		dateArrayIndex_url = line[0:splitIndex2]	#copy url into a var
		dateArrayIndex_justDate = line[splitIndex+1:splitIndex+11]
		dateArrayIndex_justTime = line[splitIndex+12:splitIndex+20]

		myTuple = (dateArrayIndex_justTime, dateArrayIndex_url)
		#print dateArrayIndex_justDate

		if not (dateArrayIndex_justDate in myDict):
			myDict[dateArrayIndex_justDate] = [] 

		myDict[dateArrayIndex_justDate].append(myTuple)

		#append both url and date vars into one 'dates' obj  
		#dates2 = dateArrayIndex_dateTime, dateArrayIndex_url
		#dateArray.append(dates2)
		#print '\n'
print myDict

#for x in myDict:
	#print x + str(myDict[x])

		#'dateArray' is an array of 'dates' objects
	
	#print dateArrays
	#for data in dateArray:
	#	print data

d  = json.dumps(myDict, indent=2)
file2.write(d + "\n")


'''for data in dateArray:
	print dateArray
	print '\n'
		#dateArray is where all your dates and URLs are stored in the format ['date','url']
'''

