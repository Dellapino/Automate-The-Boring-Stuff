#! python3
# Finds UK phone numbers and email addresses on the clipboard.

# Import libraries
import pyperclip, re

# Create phone regex
phoneRegex = re.compile(r'''(                   # note there is an overarching group!
    (0|\+44\s)                  # area code
    (\d{4})                     # first part
    (\s)                        # separator
    (\d{6})                     # last part
    )''', re.VERBOSE)

# Create email regex
emailRegex = re.compile(r'''(                   # note there is an overarching group!
    [a-zA-Z0-9._%+-]+           # username
    @                           # @ symbol
    [a-zA-Z0-9.-]+              # domain name
    )''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    print(groups)
    if groups[1] == '+44 ':
        phoneNum = ''.join(['0', groups[2], groups[3], groups[4]])
    else:
        phoneNum = groups[0]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups)

# Copy results to the clipboard
if len(matches) > 0:
    toClipboard = '\n'.join(matches)
    pyperclip.copy(toClipboard)
    print('Copied to clipboard:')
    print(toClipboard)
else:
    print('No phone numbers or email addresses found.')
