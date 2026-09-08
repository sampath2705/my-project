      
modules:
-------
--> A module is a python file (.py) that written using function , variables , operators , etc...

1.built-in modules
------------------
-->  the modules are developed by programmer and those comes with installaton
1.math
------
eg:
import math
print(math.pow(2,3))
o/p:8

2.os
----
import os
print(os.getcwd())

3.sys:
------
import sys
print(sys.path)
print(sys.version)

4.random
----------
import random
print(random.randint(100,999))

eg:
---
import math
print(math.pi)
print(math.ceil(4.3))
print(math.floor(5.6))
print(math.sqrt(25))
print(math.sin(2))
print(math.pow(2,3))
print(math.cos(5))

o/p:
----
3.141592653589793
5
5
5.0
0.9092974268256817
8.0
0.28366218546322625

random:
-------
import random
print(random.randint(1,100))
print(random.randrange(1,100))
color =['red','blue','green','yellow','orange']
print(random.choice(color))
print(random.shuffle(color))
print(color)

collections:
------------
import collections
data_ = ['banana','apple','banana','orange','kiwi']
print(collections.Counter(data_))
all_ = collections.Counter(data_)
print(all_.most_common())

datetime:
---------
from datetime import datetime
today = datetime.today()
now = datetime.now()
print(today.month)
print(today.day)
print(today.year)
print(today.hour)
print(today.minute)
print(today.second)

date time:
---------
from datetime import datetime
now = datetime.now()
print(now.strftime('%d-%m-%y'))
print(now.strftime('%H:%M:%S'))
print(now.strftime('%a'))
o/p:
07-09-26
14:50:46
Mon





import random
attep_ = 4
num = random.randrange(1,100)
print(num)
while attep_> 0:
    game_ = int(input('Enter a number between 1 and 100: '))
    if game_ ==num:
        print("your guess is correct")
    else:
        attep_ -=1
if attep_ == 3:
    print('price money is 500')
elif attep_ ==2:
    print('price money is 300')
elif attep_ ==1:
    print('price money is 200')
2.user-defined modules:
----------------------





'''
