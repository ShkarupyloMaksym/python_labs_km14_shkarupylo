speed = input("Enter the speed of wind in km/h ")
try:
    speed = int(speed)
except ValueError:
    print("You must enter a number")
    exit()
if speed < 0:
    print('error')
elif speed < 137:
    print('Minor')
elif speed < 177:
    print('Moderate')
elif speed < 217:
    print('Considerable')
elif speed < 266:
    print('Severe')
elif speed < 322:
    print('Devastating')
else:
    print('Incredible')
