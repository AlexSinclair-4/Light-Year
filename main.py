YEAR = 365
DAY = 24
HOUR = 60
MIN = 60

RATE = 3.0e8

totalSecYear = YEAR * DAY * HOUR * MIN

lightYear = RATE * totalSecYear

print("Light travels", lightYear, "meters in a year")