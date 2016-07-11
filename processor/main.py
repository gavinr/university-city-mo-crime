import sqlite3
from openpyxl import load_workbook
from datetime import datetime
wb = load_workbook(filename='../data/2015/North Central Crime Report 2015.xlsx', read_only=True)

# db
conn = sqlite3.connect('data.db')

# constants
currentYear = '2015'
months = ['January','February','March','April','May','June','July','August','September','October','November','December']



epoch = datetime.utcfromtimestamp(0)
def unix_time_millis(dt):
    return (dt - epoch).total_seconds()

def crimeForIndex(crimeIndex):
	if(crimeIndex == 2):
		return 'homicide'
	elif(crimeIndex == 3):
		return 'ARSON'
	elif(crimeIndex == 4):
		return 'ASSAULT'
	elif(crimeIndex == 5):
		return 'LARCENY'
	elif(crimeIndex == 6):
		return 'MV THEFT'
	elif(crimeIndex == 7):
		return 'BURGLARY'
	elif(crimeIndex == 8):
		return 'ROBBERY'
	elif(crimeIndex == 9):
		return 'RAPE'

def isValidRow(row):
	if(row[0].value is not None):
		raw = row[0].value.replace('-', '')
		if (raw.isdigit()):
			return True
	return False

def getInsertRow(year, month, crimeIndex, streetNumber, streetName, howMany):
	dt = datetime.strptime(month + ' 1 ' + year, '%B %d %Y')
	retList = []
	for i in list(xrange(howMany)):
		retList.append((unix_time_millis(dt), crimeForIndex(crimeIndex), streetNumber, streetName))
	return retList


for ws in wb:
	if(ws.title in months):
		currentMonth = ws.title
		print currentMonth + '-----'
		for row in ws.rows:
			if(isValidRow(row)):
				# values = map(lambda(x): x.value, row)
				# print(values)
				for idx, cell in enumerate(row):
					if(idx != 0 and idx != 1):
						if (cell.value > 0):
							listOfTuples = getInsertRow(currentYear, currentMonth, idx, row[0].value, row[1].value, cell.value)
							print len(listOfTuples)
							conn.executemany('INSERT INTO crimes VALUES (?,?,?,?)', listOfTuples)
							
conn.commit()
conn.close()
