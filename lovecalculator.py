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

3-10-25 #dictionaries
dict={
    "model":"1st model",
    "year":2021,
    "age":24
}
print(dict["model"])
