a = input("Enter the first phrase ")
fp = set()  # fp = first phrase
for i in a:
    if i.isalpha():
        fp.add(i.lower())
b = input("Enter the second phrase ")
sp = set()
for i in b:
    if i.isalpha():
        sp.add(i.lower())
print("Letters of first phrase: "+str(fp))
print("Letters of second phrase: "+str(sp))
if len(sp - fp) == 0:
    print("You can make second phrase")
else:
    print("You can`t make second phrase")
