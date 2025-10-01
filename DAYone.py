  Flower=[]
  for i in  range(1,11):
    Flower.append(i)
  print(Flower[i]
for i in range(1,11):
   print(i)



# for i in range(51,101):
#     print(i)
# i=0
# while(i<51):
 #    print(i)
  #   i=i+1
   
#while(i<51):
  #   print(i)
   #  i+=i
     
# n=int(input("enter a number:")) 
 #if n/2==0:
  #   print("it is an")

    
# name1=input("enter your name:")
# name2=input("enter your partner name:")
# Bothnames=name1+name2
# print(Bothnames)
# c_letters=Bothnames.upper()
# print(c_letters)

# name1=input("enter your name:")
# name2=input("enter your partner name:")
# Bothnames=name1+name2
# print(Bothnames)
# Small_letters=Bothnames.lower()
# print(small_letters)

# name1=input("enter your name:")
# name2=input("enter your partner name:")
# Bothnames=name1+name2
# print(Bothnames)
# Small_letters=Bothnames.lower()
# t=small_letters.count('t')
# r=small_letters.count('r')
# u=small_letters.count('u')
# e=small_letters.count('e')
# l=small_letters.count('l')
# o=small_letters.count('o')
# v=small_letters.count('v')
# e=small_letters.count('e')
# allcount=t+r+u+e+l+o+v+e

name1=input("enter your name:")
name2=input("enter your partner name:")
Bothnames=name1+name2
print(Bothnames)
small_letters=Bothnames.lower()
t=small_letters.count('t')
r=small_letters.count('r')
u=small_letters.count('u')
e=small_letters.count('e')
true=t+r+u+e
l=small_letters.count('l')
o=small_letters.count('o')
v=small_letters.count('v')
e=small_letters.count('e')
love=l+o+v+e

lovescore=int(str(true)+str(love))
if lovescore<10 or lovescore>90:
    print("You are made for each other")
elif lovescore<=40 or lovescore>=50:
    print("Your are very lucky to have your partner")
else:
    print("You are the unique couple in the wolrd")
