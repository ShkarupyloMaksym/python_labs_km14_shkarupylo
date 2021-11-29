import string

f = open('gadsby.txt', 'r')
arr_let_num_let = []
num_of_let = 0
for i in range(len(string.ascii_lowercase)):
    arr_let_num_let.append([0, string.ascii_lowercase[i]])
line = f.readline().lower()
print(string.ascii_lowercase)  # It was one of the tasks
while line:
    for i in line:
        if i in string.ascii_lowercase:
            arr_let_num_let[string.ascii_lowercase.index(i)][0] += 1
            num_of_let += 1
    line = f.readline().lower()
arr_let_num_let.sort()
arr_let_num_let.reverse()
print('The oftenest letters')
for i in range(5):
    print(arr_let_num_let[i][1], round(arr_let_num_let[i][0] / num_of_let * 100, 3))
print('\nThe rarest:')
for i in range(5):
    print(arr_let_num_let[-5 + i][1], round(arr_let_num_let[-5 + i][0] / num_of_let * 100, 3))
f.close()
