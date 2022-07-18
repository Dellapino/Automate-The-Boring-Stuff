# Automate the boring stuff - chapter 7

#%% Finding Patterns of Text Without Regular Expressions

def isPhoneNumber(text): # checks if text has the format of a phone number
    
    if len(text) != 12:
        return False
    
    for i in range(0,5):
        if not text[i].isdecimal(): # using the not statement as we want to return False if not a phone number
            return False
    
    if text[5] !=  ' ':
        return False

    for i in range(6,12):
        if not text[i].isdecimal():
            return False

    return True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

print('Is 07906 645257 a phone number?')
print(isPhoneNumber('07906 645257'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))
print('\n')

message = 'Call me at 07506 620651 tomorrow. 07951 393794 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
          print('Phone number found: ' + chunk)
print('Done')
print('\n')

# NEW: .isdecimal() is a method checking for numbers in a string

#%% Finding Patterns of Text with Regular Expressions

import re

phoneNumRegex = re.compile(r'\d{5} \d{6}')
mo = phoneNumRegex.search('His number is 07951 393794.') # .search returns a match object
print('Phone number found: ' + mo.group())

# NEW: r before string keeps any \ in string and characters after \ are kept as is
# NEW: re module to define and search for regular expressions within strings
# NEW: \d{5} == \d\d\d\d\d when defining regular expressions with re

#%% More Pattern Matching with Regular Expressions

import re

phoneNumRegex = re.compile(r'(\d{5}) (\d{6})') # brackets make subgroups
mo = phoneNumRegex.search('His number is 07951 393794.')
for i in range(3):
    print(mo.group(i)) # group(0) and group() gives all groups together
print('\n')

first, second = mo.groups() # groups() returns tuple of all groups
print(first)
print(second)
print('\n')

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)') # use \ to escape special characters
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))
print('\n')

siblingRegex = re.compile(r'Ali|Haider|Zahra') # regex using pipes gives OR structure
mo1 = siblingRegex.search('Haider and Ali went to the park.') # matches first occurance
print(mo1.group())
print('\n')

batRegex = re.compile(r'Bat(man|mobile|copter|bat)') # regex with subgroups and pipes
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1)) # returns text matched from 1st bracket
print('\n')

batRegex = re.compile(r'Bat(wo)?man') # ? after group tries to match 0 or 1 times
batRegex = re.compile(r'Bat(wo)*man') # * after group tries to match 0 or more times
batRegex = re.compile(r'Bat(wo)+man') # + after group tries to matche 1 or more times

haRegex = re.compile(r'(Ha){3}') # matches HaHaHa, built by 3 groups

#%% Greedy and Non-greedy Matching

greedyHaRegex = re.compile(r'(Ha){3,5}') # matches 3 to 5 Ha's but will return longest suitable match
mo1 = greedyHaRegex.search('HaHaHaHaHa')
nongreedyHaRegex = re.compile(r'(Ha){3,5}?') # use of ? after curly braces will return shortest of suitable matches
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
print(mo2.group())
print('\n')

# %% Looks like better strategy is to read through the chapter and then attempt the projects