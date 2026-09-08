'''
concatination
-------------
--> the + will behave two ways for numeric it works normally and for other data types like string, list, tuple it concatenation


operators
--------

--> The operators are used to perform operations in variables and the values..

1. Arthematic operator
-----------------------
+,-,*,/,//,%

eg:
+ --> to add the values 
num = 5
num_2 = 6
print(num + num_2)

eg:
-- sub
a=9
b=7
print(a-b)

eg:
-- multiply
num = 2
num_2 = 4
print(num*num_2)

eg:
--division
num = 4
num_2 = 5
print(num/num_2) -> output will comes in decimal 
print (num//num_2)-> output will comes in non decimal 


2. Assignment operator
----------------------
=,+=,-=,*=,/=,%=

+= --> is increment operator
eg:
a=0
print(a)
a += 1
print(a)

-= --> is decrement operator
eg:
b = 15
b -= 5
print(b)

*= -->
eg:
c = 7
c *= 2
print(c)

/= -->
eg:
v = 2
v /= 4
print(v)

3. Comparison operator
---------------------

==,>=,<=,!=

==
num = 15
num_2 = 5
print(num == num_2)
output: True

>=
num = 5
num_2 = 4
print(num >= num_2)

<=
num = 2
num_2 = 5
print(num <= num_2)

!=
num = 4
num_2 = 4
print(num != num_2)


4. logical operator
----------------------

num = 9
num_2 = 13
print(num >= num_2 and num <= 10)
output: false


5.identify operator
----------------------
is
a = [1,2]
b = [1,2]
print (a == b)
print (a is b )
output: true
         false

is not --> location will change
a = [1,2]
b = [1,2]
print(id(a))
print(id(b))
123456789
123456564


6 Membership operator
---------------------------
 whether the given term is available in or not

nums = 'python is programming language'
print ('y' in nums)
print ('i' not in nums)


7. Bitwise operator


input formatting
------------------
integer -->

name = (input('what is your name: '))
print(name)

a = int(input("enter an integer:"))

b = float(input("enter any decimal:"))
print(b + 4)

a = input("enter a string:")
print(type(a))

list --> 1 2 3 --> [1,2,3]

num = list(map(int,input().split()))
print(num)

tuple -->1 2 3 --> (1,2,3)

num = tuple(map(int,input().split()))
print(num)

types
------
data_ = eval(input('enter: '))
print(type(data_))

name = 'sam'
age = 23

print('my name is ',name,'age is',age)
print('hello!',name)

print(f'my name is {name} and i am {age} years old')

name = 'sam'
age = 23

print('my name is %s and im %d years old' %(name,age))

Indexing
---------

1. positive indexing
---------------------

positive indexing starts with "0"



2. Negative indexing
---------------------
negative indexing starts with "-1"

3.len()

it is built to count no of variables
name = 'sampath'
print(len(name))

slicing
-------
--> slicing is used to access the particular part of the string

txt = 'python is a programming language'
print(txt[0:6])
print(txt[:15])
print(txt[3:19])

output;python
python is a pro
hon is a program

upper()
-------
--> used to convert all small char to capital

txt = 'python is a programming language'
print(txt.upper())

lower()
-------
--> used to convert all cap into small

txt = 'PYTHON'
print(txt.lower())

index()
-------
--> used to know the index position of an char
syntax --> varaible_name.index('substring',start,end)

replace()
---------
--> used to replace old substring with new substring
syntax --> variable_name.replace(old,new)
eg

txt = 'my name is sam'
print(txt.replace('sam','sampath'))

split()
-------
--> this is a method is used to seperate the string based on given substring
syntax--> variable_name.split(substring)

txt = 'python is a programming language'
print(txt.split(''))

count()
-------
--> used to count number of occurences of a substring

txt = 'python is a programming language'
print(txt.count('a',1,30))

a = [1,2,3,4,"sam"]
print(a[-1])
all = [12,[1,32,"sam",2],[32,"sampath"],[21,2005,7(4,[2005,4])]]



pop()
------
--> pop() is used to remove items from the list and it will delete based on the index position

syntax--> variable_name.pop(index_position)

eg
--
m = [5,1,2,3,4,'python']
m.pop(4)
print(m)

remove()
--> but in this remove we can directly remove the value or object

eg
--

n = [22,18,1,'sam',999]
n.remove(1)
print(n)


min()
----

--> used to find out the least value from the tuple
eg
--
so = (67,5,89,45)
print(min(so))

Accessing
----------
-->dict can access by calling key we will gwt value from that key
syntax --> dict['key']

--> get() method is also used to get the value from that key

data_ = {'name':'sam',
         'balance':7000,
         'Adr':1234567891234,
         'panc':'RJRPS2795G',
         2:[22,44]}

print(data_.get('name'))
print(data_['Adr'])
data_['AC'] = 123456789567
print(data_)
update()
--------
--> method is used update a key , incase if the key is not present inside dict then it add that key

--> there is another way to update a key


keys()
------
--> keys()method is used get all the key from the dict
syntax -->dict.keys

data_ = {'name':'sam',
         'balance':7000,
         'Adr':1234567891234,
         'panc':'RJRPS2795G',
         }
print(data_.keys())

items()
-------
--> the method will get the key:value seperated from the dict
syntax--> dict.items()

clear()
-------
--> clear()method is used to del all data from dict
syntax --> dict.clear()

eg
--
data_ = {'name':'sam',
         'balance':7000,
         'Adr':1234567891234,
         'panc':'RJRPS2795G',
         }
print(data_)
del data_['Adr']
print(data_)
data_.clear()
print(data_)

if statement
------------
--> if condition become true , then it will execute inside block of code
--> incase it become false , then it will never entry inside block

age = 18
if age>=18:
    print('Eligible to vote')
    
if-else
-------



age = 16
if age>=18:
    print('Eligible to vote')
else:
print('you are not eligible to vote')

elif
----
--> elif statement is used to check more possible

a = 90
b = 780
c = 670
if a>b and a>c:# 90 > 780 and 90 > 67
    print(a)
elif b>a and b>c:# 780 > 67
    print(b)
else:
        print(c)

eg:

a = 90
b = 780
c = 670
if a>b and a>c:# 90 > 780 and 90 > 67
    print(a)
elif b>a and b>c:# 780 > 67
    print(b)
else:
        print(c)

 output : 780

 nested if
 ----------
  --> if inside an if statement is called nested if


app_details = {'pin':1234}
import random
user_pass = int(input("enter your app password: "))
otp = random.randint(1000,9999)
if user_pass == app_details['pin']:
    print('password is correct')
    print(otp)
    user_otp = int(input("enter 4 digit OTP:"))

    if user_otp == otp:
        print('welcome to the app')
    else:
        print('incorrect OTP')

else:
    print('password is incorrect')
                        
eg:
----

a = int(input("enter a number:"))
if a%2 == 0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')
    
elif:
-----

marks = int(input("enter your marks:"))
if marks>90:
    print('A+')
elif marks>=80:
    print('A')
elif marks>=70:
    print('B+')
elif marks>=60:
    print('B')
elif marks>=50:
    print('C')


star;
----
num = int(input("enter a number:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print('$',end = " ")
    print()

eg
--
num = int(input("enter a number:"))
count = 1
for i in range(1,num+1):
    for j in range(1,i+1):
        print(count,end = " ")
        count+= 1
    print()
    
output:
-------
enter a number:5
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15

eg:
---
num = int(input("enter a number:"))
count = 1
for i in range(1,num+1):
    for j in range(1,i+1):
        print(count,end = " ")
        count+= 1
    print()

vowels
-------
words = input("Enter a word:")
vowels = 'aeiouAEIOU'
count = 0
for i in words:
    if i in vowels:
        count +=1
        print(f'{i} is vowel')
print(count)

duplicates
----------

digits = [1,2,2,3,3,6,7,9]
empty = []
for i in digits:
    if i not in empty:
        empty.append(i)
print(empty)
o/p:
[1, 2, 3, 6, 7, 9]
eg:
---
digits = (1,2,3,3,7,9)
duplicate = []

for i in digits:
    if digits.count(i) > 1 and i not in duplicate :
        duplicate.append(i)
print(duplicate)

Fibonacci series
----------------
num = 0
num_2 = 1
print(num,num_2,end=' ')
for i in range(1,20):
    num_3 = num + num_2
    num = num_2
    num_2 = num_3
    print(num_3,end=' ')
o/p:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765

Function
--------
--> A function start with def keyword and the line called as defination line,where we can define a function name
--> And if we want to execute the program in the function,need to call with function name define at def line
syntax
------
def fun_name(parameters):
    pass
fun_name(arguments)
eg:
---
def add_(a,b):
    print(a+b)
add_(5,6)

Arguments
----------
positional Arguments
--------------------
--> The arguments should be same at def line and calling,incase if they are not same number will raise an error
default arguments
-----------------
--> The default arguments where the function will only consider the data at calling,even though data present at def line
eg
--
def data(a=5,b=10):
    print(a+b)
data(1,9)
eg:
10

def may(num,num_2):
    print(num + num_2)
may([1,7],[1,9])
o/p:
[1, 7, 1, 9]
keyword argument
----------------
def data_(age,name,batch,location):
    print(name)
    print(age)
    print(batch)
    print(location)
data_(batch = 6,age = 21,location = 'vizag',name = 'sam')
o/p:
sam
21
6
vizag

variable length argument
------------------------
-->adding a (*call it as args)before a variable at parameters we can pass tuple of arguments and can be access with indexing
eg:
def all(*Name):
    print(Name)
all('sam','vantaku','munna','sai')
o/p:
('sam', 'vantaku', 'munna', 'sai')
keyword length argument
-----------------------
def all(**Name):
    print(Name)
all(name = 'sam',age = 23,location = 'vizag')
o/p:
{'name': 'sam', 'age': 23, 'location': 'vizag'}
keys
----
def all(**Name):
    print(Name.keys()
all(name = 'sam',age = 23,location = 'vizag')

scope of variables
----------------
1. Local variable
-----------------
--> A variable is define inside the function  call it as local varaiable,where the variable can only access with in that function

eg:
def display():
    name = 'sam'
    print(name)
display()
o/p:
sam

2. Global variable
------------------
--> A Variable that is defined outside the function call and it can be access any where through out program.
eg:

a = 18
def display():
    print(a)
display()
print(a)
o/p:
18
18

global keyword:
---------------
--> global is a keyword used to reacess new values to variable that was already define outside the function call.
eg:
--
a = 18
print(a)
def display():
    global a
    a = 21
display()
print(a)
o/p:
18
21

Recursive function:
-------------------
--> The function call itself until the base condition met
wg:
num = int(input('enter the number'))
def even_odd(num):
    if num%2 ==0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
even_odd(num)



lambda function
---------------
--> lamda function is small anonymous function
--> lamda can take n number of arguments,but only with one expression
--> the function is defined by using lamda keyword
syntax:

eg:
add = lambda a,b,c,d : a+b+c+d
print(add(10,20,30,40))
o/p:
100
eg:
even = lambda num : num%2==0
print(even(5))
o/p:
false

eg:
a = lambda a,b: a if a>b else b
print(a(10,20))
o/p:
20

filter()
--------
--> filter() function will perform only on selected elements of iterables
syntax -->filter(funtion,iterable)
eg:

a = [2,5,7,8]
data = filter(lambda a: a%2==0,a)
print(tuple(data))

map()
-----
--> map() function will perform on all elements of a iterable
syntax-->map(lambda arguments: expressions,iterable)
eg:
a = [2,5,7,8]
data = map(lambda a: a%2==0,a)
print(tuple(data))

reduce()
--------

eg:
from functools import reduce
a = [2,5,7,9,11]
data = reduce(lambda a,b:a+b,a)
print(data)

list comprehension:
-------------------
--> list comprehension is the short form of syntax to create a list.
syntax 1--> [expression loop condition]
syntax 2--> [expression condition else loop]
Eg:
old_ = [2,4,6,8,9]
new_ = [i for i in old_ if i%2==0]
print(new_)

o/p:
[2, 4, 6, 8,]

eg:

any_ = [[i*j for i in range(1,6)]for j in range(1,10)]
print(any_)



eg:
of = [[1,2,3],
      [4,5,6],
      [7,8,9]]
data = [num for i in of for num in i]
print(data)
o/p:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
      
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


2.user-defined modules:
----------------------





'''
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
       
        


















