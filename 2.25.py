import random
help(random.randint)
random.randint(1,60)
# from time import sleep 

from datetime import datetime
import time
import random

odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,
    41,43,45,47,49,51,53,55,57,59]

for i in range(5):
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")
    wait_time = (random.randint(1,60))
    time.sleep(wait_time)
    # sleep(wait_time)


prices = []
temps = [32.0, 212.0, 0.0, 81.6, 100.0, 45.3]
words = ['hello', 'world']
car_details = ['Toyota', ' RAV4', 2.2, 60807]
everything = [prices, temps, words, car_details]
odds_and_ends = [[1,2,3], ['a','b','c'],['One','Two','Three']]
vowels = ['a','e','i','o','u']