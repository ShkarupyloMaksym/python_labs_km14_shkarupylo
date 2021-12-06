import csv

# Translated by google translator
song_year = [
    ['Heresy (Acoustics)', 1990],
    ['Stone on the head', 1996],
    ['The King and the Jester', 1997],
    ['Acoustic Album', 1998],
    ['Heroes and villains', 2000],
    ['As in an old tale', 2001],
    ['Ship riot', 2004],
    ['The Nightmare Seller', 2006],
    ['Scary Tales', 2007],
    ['Shadow of the Clown', 2008]
]

with open('King_and_Jester.csv', 'w', newline='') as csvfile:
    fieldnames = ['song', 'year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in song_year:
        writer.writerow({fieldnames[0]: i[0], fieldnames[1]: i[1]})

# one more open was added because (how I understand) while file opened it doesn't exist, so we cant read something that
with open('King_and_Jester.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for heading in reader.fieldnames:
        print(heading, end=' ')
    print('\n------------------------------')
    for row in reader:
        print(row[fieldnames[0]], row[fieldnames[1]])
print('Done')
