age_hum = input("Enter the age of your dog ")
try:
    age_hum = int(age_hum)
except ValueError:
    print("You must enter a number")
    exit()
if age_hum < 0:
    print('error')
    exit()
age_dog = 0
if age_hum > 2:
    age_dog += 4 * (age_hum - 2)
    age_hum = 2
age_dog += 10.5 * age_hum
print(age_dog)
