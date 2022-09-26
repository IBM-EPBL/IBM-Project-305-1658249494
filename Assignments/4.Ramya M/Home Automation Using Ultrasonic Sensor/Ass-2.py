import random
a=random.randint(1,190)  #temperature
b=random.randint(1,150)   #humiditY
print(a)
print(b)
if a>80:
    if b>80:
        print("Alarm ON")
        print ("hazard predicted")
    else:
        print("Alarm ON")
        print ("high temp")
else:
    print ("Alarm OFF")
