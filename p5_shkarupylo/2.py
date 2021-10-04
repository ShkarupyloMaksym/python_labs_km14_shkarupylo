item_list = list(input("Please enter objects` names ").split())
print(item_list[0], end="")
for i in range(1, len(item_list) - 1):
    print(", " + item_list[0], end="")
if len(item_list) > 1:
    print(" and " + item_list[-1])
