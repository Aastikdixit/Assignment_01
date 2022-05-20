import re
string = input('Enter any string: ')
special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
if(special_char.search(string) == None):
    print('String is accepted.')
else:
    print(' string is not accepted.')