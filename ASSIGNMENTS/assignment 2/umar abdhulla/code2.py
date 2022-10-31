import random
import time
a=random.random()
while True:
    temperature=random.randint(0, 100 )
    if(temperature > 50):
        print("high temperature alarm is on")
    else:
        print("Normal temperature alarm is off")
    humidity =random.randint(10, 100)
    if(humidity > 50):
        print("high humidity alarm is on")
    else:
        print("Normal humidity alarm is off")
    time.sleep(6.5)
