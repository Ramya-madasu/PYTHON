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
