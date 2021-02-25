from datetime import datetime

odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,
31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]

right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print("This Minute seems a little odd.")
else:
    print("Not an odd minute")


import sys
sys.platform
print(sys.version)

import os
os.getcwd()
os.environ


import datetime   # datetime 이란 것을 import 를 통하여 불러 왔다.
datetime.date.today()

datetime.date.today().year
datetime.date.today().month
datetime.date.today().day

datetime.date.isoformat(datetime.date.today())


import time # time 에 관련된 것을 import 로 불러옴
time.strftime("%H:%M") # 시간을 나타낸다.

time.strftime("%A %p")



from datetime import datetime

odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,
31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]

right_this_minute = datetime.today().minute

if right_this_minute in odds: # 만약 현재 시간이 홀수 분이면 
    print("This Minute seems a little odd.") # 홀수 분입니다.
else:
    print("Not an odd minute") # 홀수 분이 아닙니다.


print('Hello Mum!')
21 + 21
ultimate_answer = (21+21)
ultimate_answer

for ch in 'Hi!':
    print(ch)


for num in range(5):
    print('head fist Rocks!')


from datetime import datetime

odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,
31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]

right_this_minute = datetime.today().minute

for unm in range(5):
    right_this_minute = date.today().Minute

if right_this_minute in odds: # 만약 현재 시간이 홀수 분이면 
    print("This Minute seems a little odd.") # 홀수 분입니다.
else:
    print("Not an odd minute") # 홀수 분이 아닙니다.

import time
time.sleep(5) # pulse 기능

help(random.ranint)

