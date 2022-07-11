#Task 1: Numbers and Variables
# 1)Create three variables in a single line and assign values to them in such a manner that each one of
#   them belongs to a different data type.

import cmath
import imaplib
from importlib import import_module
import importlib


a,b,c = 1,2.01,'string'
print(type(a))
print(type(b))
print(type(c))

# 2) Create a variable of type complex and swap it with another variable of type integer.
d = complex(2,6)
e = 1
d = e
print(type(d))

# 3) Swap two numbers using a third variable and do the same task without using any third variable.
num1 = 3
num2 = 4

num = num2
num2 = num1
num1 = num 

swap = [num1,num2]
if swap[0]==num1:
    swap[0]==num2
    swap[1]==num1
else:
    swap[1]==num2
    swap[0]==num1
print(swap)

#4) Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x Version.
name = input("What is your name? ")
#py2
print 'Hello ' + name 
#py3 
print(f'Hello {name}!')  

#5) Write a program to complete the task given below:
# Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in another variable called z. 
# Add 30 to z and store the output in variable result and print result as the final output.
f = int(input('Enter a number between 1-10'))
g = int(input('Enter another number between 1-10'))
z = f + g
result = z + 30
print(result)

#6) Write a program to check the data type of the entered values.
# HINT: Printed output should say - The data type of the input value is : int/float/string/etc
h = input('Enter a value')
try:
  if int(h):
    h_int = int(h)
    print(type(h_int)) 
except: 
  try:
    h_float = float(h)
    print(type(h_float)) 
  except (ValueError):
    print(type(h)) 



#7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and UPPERCASE.
pythonTest = 1  #lower camelcase
PythonTest = 2  #upper camelcase
python_test = 3 #snake case
PYTHONTEST = 4  #Uppercase

#8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’again. 
# Will it change the value? If Yes then Why?

a = 1
print(a,type(a))
a = 'string'
print(a,type(a))

#Ans: Yes because python executes code line by line and the variable values can be changed along with type except for constants
#which are declared by all capital letters.

#Task 2: OPERATORS AND DECISION MAKING STATEMENT

#1. Write a program in Python to perform the following operation:
#If a number is divisible by 3 it should print “Consultadd” as a string
#If a number is divisible by 5 it should print “Python Training” as a string
#If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a string

number = int(input('Enter a number: '))
if number%3==0 and number%5==0:
    print('Consultadd - Python Training')
elif number%3==0:
    print('Consultadd')
elif number%5==0:
    print('Python Training')    

#2. Write a program in Python to perform the following operator based task:
#Ask user to choose the following option first:
#If User Enter 1 - Addition
#If User Enter 2 - Subtraction
#If User Enter 3 - Division
#If User Enter 4 - Multiplication
#If User Enter 5 - Average
#Ask user to enter two numbers and keep those numbers in variables num1 and num2
#respectively for the first 4 options mentioned above.
#Ask the user to enter two more numbers as first and second for calculating the average as
#soon as the user chooses an option 5.
#At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
#At a time a user can only perform one action.

n1 = int(input('Enter n1: '))
n2 = int(input('Enter n2: '))
operation = input('''Type an operation to perform one of the following actions: 
                Addition , Subtraction , Division , Multiplication , Average: ''')
if operation == 'Addition':
    print(n1+n2) if n1+n2>=0 else print('NEGATIVE')
elif operation == 'Subtraction':
    print(n1-n2) if n1>=n2 else print('NEGATIVE')
elif operation == 'Division' or operation == 'division':
    print(n1/n2) if n1/n2>=0 else print('NEGATIVE')
elif operation == 'Multiplication':
    print(n1*n2) if n1*n2>=0 else print('NEGATIVE')
elif operation ==  'Average':
    n3 = int(input('Enter n3: '))
    n4 = int(input('Enter n4: '))
    print((n1+n2+n3+n4)/4) if (n1+n2+n3+n4)/4>=0 else print('NEGATIVE')
else:
    print('Operation not recognized')    

#3. Write a program in Python to implement the given flowchart:

a = 10
b = 20
c = 30 
avg = (a+b+c)/3
print(f'avg = {avg}')
if avg>a and avg>b and avg>c:
    print('avg is higher than a,b,c')
else:
    if avg>a and avg>b:
        print('avg is higher than a and b')
    elif avg>a and avg>c:
        print('avg is higher than a and c')
    elif avg>b and avg>c:
        print('avg is higher than b and c')
    elif avg>a:
        print('avg is just higher than a')
    elif avg>b:
        print('avg is just higher than b')
    elif avg>c:
        print('avg is just higher than c')


#4. Write a program in Python to break and continue if the following cases occurs:
#If user enters a negative number just break the loop and print “It’s Over”
#If user enters a positive number just continue in the loop and print “Good Going”

co = 1

while co:
    co = int(input('enter a number: '))
    if co>=0:
        print('Good going')
        continue
    else:
        print('its over')
        break
        

#5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a
#multiple of 5, between 2000 and 3200.

x = []

for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        x.append(i)
    else: 
        continue    
print(x)

#6. What is the output of the following code examples?

x=123
for i in x:
    print(i)
# int object is not iterable

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else:
        print('error')
# will print a number and 'error' for each i till i becomes 3. At i = 3 the loop breaks

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# prints numbers from 0 to 4 and breaks at count = 5


#7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
#Expected output: 0 1 2 4 5
#Note: Use ‘continue’ statement

counter = 0
while counter<6:
    if counter == 3:
        counter += 1
        continue
    else:
        print(counter)
        counter += 1

#8. Write a program that accepts a string as an input from the user and calculate the number of digits
#and letters.
#Sample input: consul72
#Expected output: Letters 6 Digits 2

digits = ['0','1','2','3','4','5','6','7','8','9']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
input_string = input('Enter a string: ')
d = 0
l = 0
for i in input_string:
    if i in digits:
        d += 1
    elif i in letters:
        l += 1
print(f'letters {l} Digits {d}')            


#9. Read the two parts of the question below:
#Write a program such that it asks users to “guess the lucky number”. If the correct number is
#guessed the program stops, otherwise it continues forever.
#Modify the program so that it asks users whether they want to guess again each time. Use two
#variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
#to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
#The program continues as long as a user has not answered “no” and has not guessed the correct
#number)

lucky_num = 1001
while True:
    answer = int(input('guess the lucky number: '))
    if answer == lucky_num:
        break
    else:
        continue 

#modified 
lucky_num = 1001
while True:
    guess = input('do you want to guess? type ''y'' or ''n''')
    if guess == 'y':
        answer = int(input('guess the lucky number: '))
        if answer == lucky_num:
            break
    elif guess == 'n':
        break

#10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
#such as

#While counter <= 5:
#print(“Type in the”, counter, “number”
#counter=counter+1
#The program asks for five guesses (no matter whether the correct number was guessed or not). If the
#correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
#After the fifth guess it stops and prints “Game over!”.

lucky_num = 1001
c = 1
while c<=5:
    answer = int(input(f'Try {c}. Guess the lucky number: '))
    if answer == lucky_num:
        print('Good Guess!')
        c += 1
    else:
        if c <= 4:
            print('Try again!')
            c += 1
            continue
        elif c==5:
            print('Game Over!')
            break

#11. In the previous question, insert break after the “Good guess!” print statement. break will terminate
#the while loop so that users do not have to continue guessing after they found the number. If the user
#does not guess the number at all, print “Sorry but that was not very successful”.        
        
lucky_num = 1001
c = 1
while c<=5:
    try: 
        answer = int(input(f'Try {c}. Guess the lucky number: '))
    except:
        print('Sorry but that was not very successful')
        continue
    if answer == lucky_num:
        print('Good Guess!')
        break
    else:
        if c <= 4:
            print('Try again!')
            c += 1
            continue
        elif c==5:
            print('Game Over!')
            break