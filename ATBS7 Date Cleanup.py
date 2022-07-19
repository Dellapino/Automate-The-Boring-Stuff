# Detects valid dates and changes them to a standard format

# Import libraries
import pyperclip, re

# Regular expression to detect dates
dateRegex = re.compile(r'''(
(\d{1,2})                         # day
([,/.-])                         # separator
(\d{1,2})                         # month
([,/.-])                         # separator
(\d{4})                         # year
)''', re.VERBOSE)

# Define expected days per month
daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
daysInMonthLeap = [31,29,31,30,31,30,31,31,30,31,30,31]

# Find dates on clipboard
text = str(pyperclip.paste())
dates = []
for date in dateRegex.findall(text):
    
    day = int(date[1])
    month = int(date[3])
    year = int(date[5])
    
    # Check for leap year
    if (year % 4 == 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0): # leap year
        leap = True
    if (year % 4 != 0) or (year % 100 == 0 and year % 4 == 0): # not leap year
        leap = False
    
    # Check for valid date
    valid = False
    if leap:
        if month <=12 and day <= daysInMonthLeap[month-1]:
            valid = True
    else:
        if month <=12 and day <= daysInMonth[month-1]:
            valid = True
    
    # Standardise form of dates
    if valid:
        dates.append(dateRegex.sub(r'\2/\4/\6',date[0]))

# Copying back to clipboard
if len(dates) > 0:
    toClipboard = '\n'.join(dates)
    pyperclip.copy(toClipboard)
    print('Dates found:')
    print(toClipboard)
else:
    print('No khajoor :(')
    pyperclip.copy('')