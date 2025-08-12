import re
dateRegex = re.compile(r'(\d{2})/(\d{2})/(\d{4})')

query = input()
print(dateRegex.search(query))
finishedQuery = dateRegex.search(query)
day = finishedQuery.group(1)
month = finishedQuery.group(2)
year = finishedQuery.group(3)
#print(day,month,year)

def validate(day,month,year):
    day = int(day)
    month = int(month)
    year = int(year)
    print(day,month,year)
    if month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            return False
    if month == 2 and (year % 4 == 0):
        if day > 29:
            return False
    if month == 2 and (year % 4 != 0):
        if day > 28:
            return False
    if month != 4 and month != 6 and month != 9 and month != 11 and month != 2:
        if day > 31:
            return False
    else:
        return True
    

print(validate(day,month,year))
#detect dates in DD/MM/YYYY format

#store the strings into variables named month, day, and year
#then check to see if it's a valid date or not