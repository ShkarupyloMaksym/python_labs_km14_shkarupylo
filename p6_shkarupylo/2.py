index = input(("Enter the post index ").upper()).upper()
if len(index) != 3 or not index[0].isalpha() or not index[-1].isalpha() or not index[1].isdigit():
    print(("error").upper())
    exit()
index_letters = {
    'Newfoundland': 'A',
    'Nova Scotia': 'B',
    'Prince Edward Island': 'C',
    'New Brunswick': 'E',
    'Quebec': ('G', 'H', 'J'),
    'Ontario': ('K', 'L', 'M', 'N', 'P'),
    'Manitoba': 'R',
    'Saskatchewan': 'S',
    'Alberta': 'T',
    'British Columbia': 'V',
    'Nunavut': 'X',
    'Northwest Territories': 'X',
    'Yukon': 'Y'}
a = ''
for i in index_letters.keys():
    if isinstance(index_letters[i], str):
        if index_letters[i] == index[0]:
            a += i + " "
    else:
        if index[0] in index_letters[i]:
            a += i + " "
if a == '':
    print(("We haven`t the same index in our data base").upper())
    exit()
print(("The name of the province(s): " + a).upper())
if index[1] == 0:
    print(('village').upper())
else:
    print(('city').upper())
