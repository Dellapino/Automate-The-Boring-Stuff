import pyperclip, re

# Regex which matches a number with commas for every three digits
numRegex = re.compile(r'''(
(\s)                    # separator
(\d{1,3})               # first part of num
(\,\d{3})*              # other parts of num
(\s)                    # separator
)''', re.VERBOSE)

# Finds and copies any matches to clipboard
text = str(pyperclip.paste())
text = ' ' + text + ' '

matches = []
for num in numRegex.findall(text):
    matches.append(num[0].strip())

if len(matches) > 0:
    toClipboard = '\n'.join(matches)
    pyperclip.copy(toClipboard)
    print('Matches found:')
    print(toClipboard)
else:
    print('No matches :(')