from dateutil.parser import parse

day1 = parse('2017-01-25')
print (type(day1))
print (day1)
print ("-------------\n")

day2 = parse('Jan 01, 2017 10:30 AM')
print (type(day2))
print (day2)
print ("-------------\n")

day3 = parse('01/01/2017', dayfirst=True)
print (type(day3))
print (day3)
print ("-------------\n")

