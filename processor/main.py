import sqlite3
from openpyxl import load_workbook
from datetime import datetime



# constants
currentYear = '2015'
months = ['january','february','march','april','may','june','july','august','september','october','november','december']



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
		raw = str(row[0].value).replace('-', '')
		if (raw.isdigit()):
			return True
	return False

def getInsertRow(year, month, crimeIndex, streetNumber, streetName, howMany):
	# datetime:
	dt = datetime.strptime(month + ' 1 ' + year, '%B %d %Y')

	# address numbers
	splitAddress = str(streetNumber).split("-")
	streetNumber1 = splitAddress[0]
	streetNumber2 = None
	if(len(splitAddress) > 1):
		streetNumber2 = splitAddress[1]

	retList = []
	for i in list(xrange(howMany)):
		retList.append((unix_time_millis(dt), crimeForIndex(crimeIndex), streetNumber1, streetNumber2, streetName))
	return retList

def addWorkbookData(fn):
	conn = sqlite3.connect('../data.sqlite')
	print('Working on ' + fn + ' ----------------------')
	wb = load_workbook(filename=fn, read_only=True)
	for ws in wb:
		if(ws.title.lower() in months):
			currentMonth = ws.title.lower()
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
								conn.executemany('INSERT INTO crimes VALUES (?,?,?,?,?,null,null,null,null,null)', listOfTuples)
	conn.commit()
	conn.close()

def main():
	for file in [
		'../original_data/2015/North Central Crime Report 2015.xlsx',
		'../original_data/2015/North East Crime Report 2015.xlsx',
		'../original_data/2015/North West Crime Report 2015.xlsx',
		'../original_data/2015/South Central Crime Report 2015.xlsx',
		'../original_data/2015/South East Crime Report 2015.xlsx',
		'../original_data/2015/South West Crime Report 2015.xlsx'
	]:
		addWorkbookData(file)

main()
