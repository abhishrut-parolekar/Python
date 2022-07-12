#Task 3: DATA STRUCTURES

#1. Create a list of 10 elements of four different data types like int, string, complex and float.
from heapq import merge
from random import randint
import re


l = [1,2,3,'a','b','c',complex(2,3),complex(3,4),2.5,10.2]

#2. Create a list of size 5 and execute the slicing structure
a = [i for i in range(0,5)]
b = a[1:4]
print(b)

#3. Write a program to get the sum and multiply of all the items in a given list.
items = [1,2,3,4,5,6,7,8,9]
sum = sum(items)
product = 1
for i in items:
    product *= i
print(sum,product)

#4. Find the largest and smallest number from a given list.
items = [4,5,3,2,7,1,8,9,0]
print(min(items),max(items))

#5. Create a new list which contains the specified numbers after removing the even numbers from a predefined list.
l1 = [0,1,2,3,4,5,6,7,8,9]
l2 = []
for i in l1:
    if i%2==0:
        continue
    else:
        l2.append(i)
print(l2)

#6. Create a list of elements such that it contains the squares of the first and last 5 elements between 1 and30 (both included).
elem = []
for i in range(1,31):
    if i<=5 or i>=25:
        elem.append(i*i)
    else:
        elem.append(i)
print(elem)

#7. Write a program to replace the last element in a list with another list.
#Sample input: [1,3,5,7,9,10], [2,4,6,8]
#Expected output: [1,3,5,7,9,2,4,6,8]
l1 = [1,3,5,7,9,10]
l2 = [2,4,6,8]
l1 = l1[:-1]
l1=l1+l2
print(l1)

#8. Create a new dictionary by concatenating the following two dictionaries:
#Sample input: a={1:10,2:20} b={3:30,4:40}
#Expected output: {1:10,2:20,3:30,4:40}
a = {1:10,2:20} 
b = {3:30,4:40}
c = [1,2,3,4,5]
a.update(b)
print(a)

#9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1 and n(both 1 and n included).
#Sample input: n=5
#Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}
n = int(input('Enter n: '))
d = {}
for i in range(1,n+1):
    d[i] = i*i
print(d)

#10. Write a program which accepts a sequence of comma-separated numbers from console and generates a list and a tuple which contains every number in the form of string.
#Sample input: 34,67,55,33,12,98
#Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)
sq = [i for i in input('Enter list of numbers separated by comma: ')]
for i in sq:
    if i==',':
        sq.remove(i)
tu = tuple(sq)
print(sq,tu)


#TASK FOUR: TRADITIONAL FUNCTIONS,ANONYMOUS FUNCTIONS & HIGHER ORDER FUNCTIONS

#1. Write a program to reverse a string.
#Sample input: “1234abcd”
#Expected output: “dcba4321”
s = '1234abcd'
print(s[::-1])

#2. Write a function that accepts a string and prints the number of uppercase letters and lowercase letters.
#Sample input: “abcSdefPghijQkl”
#Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12
s = input('enter a string: ')
l = 0
u = 0
for i in s:
    if i.isupper():
        u += 1
    elif i.islower():
        l += 1
    else:
        continue    
print(f'No. of Uppercase characters : {u} No of lower case characters : {l}')

#3. Create a function that takes a list and returns a new list with unique elements of the first list.
def unique_list(l):
    u = set(l)
    new_l = list(u)
    return new_l
l = [1,2,3,3,3,5,2,2,5,6,7,7,8,87,5,10]
print(unique_list(l))

#4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
sent = input('Enter a sentence separated by hyphen: ')
a = sent.split('-')
a.sort()
a = '-'.join(a)
print(a)

#5. Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
#Sample input: Hello world Practice makes man perfect
#Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT
sent = input('Enter a sentence: ')
print(sent.upper())

#6. Define a function that can receive two integral numbers in string form and compute their sum and print it in the console.
def sum(a,b):
    return int(a)+int(b)
a = input('enter number1: ')
b = input('enter number2: ')
print(sum(a,b)) 

#7. Define a function that can accept two strings as input and print the string with the maximum length
#in the console. If two strings have the same length, then the function should print both the strings line by line.
def strings(a,b):
    if len(a)==len(b):
        print(a)
        print(b)
    elif len(a)>len(b):
        print(a)
    else:
        print(b)
a = input('Enter string 1: ')
b = input('Enter string 2: ')
strings(a,b)

#8. Define a function which can generate and print a tuple where the values are square of numbers between 1 and 20 (both 1 and 20 included).
def tup():
    a = [i*i for i in range(1,21)]
    a = tuple(a)
    print(a)
tup()    

#9. Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
#Sample input: show Numbers(3) (where limit=3)
#Expected output:
#0 EVEN
#1 ODD
#2 EVEN
#3 ODD
def showNumbers(limit):
    for i in range(0,limit+1):
        if i%2==0:
            print(f'{i} EVEN')
        elif i%2!=0:
            print(f'{i} ODD')
        else:
            continue
limit = int(input('Enter a limit: '))
showNumbers(limit)


#10. Write a program which uses filter() to make a list whose elements are even numbers between 1 and 20 (both included)
l = [i for i in range(1,21)]
even = list(filter(lambda x: x%2==0 ,l))
print(even)


#11. Write a program which uses map() and filter() to make a list whose elements are squares of even numbers in [1,2,3,4,5,6,7,8,9,10].
#Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the numbers in the filtered list. 
# Use lambda() to define anonymous functions.
x = [i for i in range(1,11)]
square = list(map(lambda num: num**2,x))
print(square)

#12. Write a function to compute 5/0 and use try/except to catch the exceptions
try: 
    5/0
except Exception as e:
    print(e) 

#13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
import functools
import operator
l = [1,2,3,4,5,6,7]
l = [str(i) for i in l]
print("The concatenated product is : ", end="")
print(functools.reduce(operator.add, l))

#14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7. Make sure to use only higher order functions.
limit = int(input('Enter limit: '))

def func(limit):
    l=[]
    for i in range(limit):
        if i%3!=0 and i%7==0:
            l.append(i)
        else:
            continue
    return l

print(func(limit))

#15. Write a program in Python to multiply the elements of a list by itself using a traditional function and pass the function to map() to complete the operation.
l = [1,2,3,4,5,6]
l = list(map(lambda i: i*i, l))
print(l)

#16. What is the output of the following codes:
#(i) 
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)
#Ans: This code returns 2 everytime it is run because anything under 'finally' gets executed regardless of what is under 'except'

#(ii) 
def a():
    try:
        f(x, 4)
    finally:
        print('after f')
        print('after f?')
a()
#Ans: We only get statements under finally as output because from try block, f is not defined