#switch case
switch case:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    default:
        print(" there no relevant case")


#slicing
list=[1,2,3,4,5,6,7,8,9]
print(list[1::3])                  #  :: is used to skip vales here  in slicing or lists.


#Booliuns
if False:
    print("valid")
else:
    print("invalid")

#exceptional handing
try:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    result=a+b
    print("sum:",result)
except ValueError:
    print("invalid input! enter numerical values only. ")

#complex datatype
x=2+3i
print(x.real)
print(x.imag)
print(type(x))

#function
def summ(a,b):
    return a+b
def diff(a,b):
    return a-b
def prod(


## Akhil sir class##

    class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        def __str__(self):
         return f"{self.name},{self.age} years old"
         
person=Person("Akhil",23)
print(person)

class Dog:
    
    def __init__(Dog,name,age):
        Dog.name = name
        Dog.age = age
        
    def __str__(Dog):
         return f"{Dog.name},{Dog.age} years old"
         
Dog=Dog("june",6)
print(Dog)

[08-10-2025]
## Game loop ##

import random

options = ["rock","paper","scissors"]

while True:
    user = input("Enter rock, paper or scissors(or 'Exit to stop):").lower()
    if user =="Exit":
        print("Thanks for playing!")
        break
    
    computer = random.choice(options)
    print("computer chose"+ computer)
    
    if user == computer:
        print ("it's a tie!")
    elif( user =="rock"and computer =="scissors")or\
        ( user =="paper"and computer =="rock")or\
        ( user =="scissors"and computer =="paper"):
        print("You win!")
    else:
        print("You lose!")
    
 ##strong password loop ##
    
password = input("Enter password: ")

has_letter = False    
has_digit = False
has_special =False

for ch in password:
    if ch.isalpha():
        has_letter = True
    elif ch.isdigit():
        has_digit = True
    else:
        has_special = True
        
if has_letter and has_digit and has_special:
    print("Strong Password")
else:
    print("Weak Password.use letters,number,and symbols.")
      
   ## ALARM ## 
import time

alarm_time = input("Enter alarm time (HH:MM:SS): ")
print("Alarm set for "+alarm_time)
print("Waiting for alarm...")

while True:
    current_time = time.strftime("%H:%M:%S")
    if current_time == alarm_time:
        for i in rande(5):
            print("\a WAKE UP!")
    break
time.sleep(1)
     





























