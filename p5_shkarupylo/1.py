salary_list = [7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]
salary_list_new=[round(i*1.3, 2) for i in salary_list]
salary_list_index=[round(i*0.3, 2) for i in salary_list]
print("Salary table:")
for i in range(len(salary_list)):
    print(str(salary_list[i]).ljust(5),str(salary_list_new[i]).ljust(5),salary_list_index[i])