import os

print(os.getcwd())
os.chdir('archive')
names_m = []
names_f = []
for i in list(os.listdir()):
    if i.startswith('yob'):
        f = open(i, 'r')
        M, F = True, True
        line = f.readline()
        while line:
            line = line.split(',')
            if line[1] == 'M':
                if M:
                    names_m.append(line[0])
                    M = False
            elif line[1] == 'F':
                if F:
                    names_f.append(line[0])
                    F = False
            line = f.readline()
        f.close()
names_m_set = []
for i in set(names_m):
    names_m_set.append([names_m.count(i), i])
names_m_set.sort()
names_m_set.reverse()
for i in names_m_set:
    print(i[1], i[0])
print()
names_f_set = []
for i in set(names_f):
    names_f_set.append([names_f.count(i), i])
names_f_set.sort()
names_f_set.reverse()
for i in names_f_set:
    print(i[1], i[0])
