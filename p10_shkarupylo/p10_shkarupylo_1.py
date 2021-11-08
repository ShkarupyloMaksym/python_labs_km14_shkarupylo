# this method was my need to nice print, but I think that max(max(lengs)) is bad funk
# I don`t know how I should write it normal(
def good_print(*our_list):
    lengs = []
    for i in our_list:
        lengs.append(list(map(lambda a: len(str(a)), i)))
    return max(max(lengs))


salary_list = [7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]
salary_list_new = list(map(lambda a: round(a * 1.3, 2), salary_list))
salary_list_increase = list(map(lambda a, b: round(a - b, 2), salary_list_new, salary_list))
print('Salary table:')
nice_len = good_print(salary_list, salary_list_new, salary_list_increase)
for i in range(len(salary_list)):
    print(str(salary_list[i]).ljust(nice_len), str(salary_list_new[i]).ljust(nice_len),
          str(salary_list_increase[i]).ljust(nice_len))
