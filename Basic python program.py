
#python program to print your name
n="G.satyaprakash"
print(n)

#get the input from the user and print
name = input("enter your name")  
print(name)     

#get the input from userand print it
num1=input("enter your first number")
num2=input("enter your second number")
print("first number:",num1)
print("second number:",num2)

#get the input from user add two number
num3=int(input("enter your third number"))
num4=int(input("enter your fourth number"))
sum=num3+num4
print("sum of two values:",sum)

#genrate first name and last name
a=input("enter the first name")
b=input("enter the second name")
c=a+b
print("your full name:",c)

#Write a python  programee get a input from user swap 2 numbers withour 3rd variable
a=10
b=20
a=a+b
b=a-b
print("a",a)
print("b",b)

#Write a python  programee get a input from user swap 2 numbers withour 3rd variable
a=10
b=20
temp=a
a=b
b=temp
print("after swapping:",a)
print("after swapping:",b)

#write a python program print the primitive data type
a=10
b=2.13
c=True
print("interger is :",a)
print("float is :",b)
print("Boolean is ",c)

#write a python program print the non primitive data type
a=(10,20,30)
b=[10,10,20,30]
c={10,20,20,30}
dict_1={"one":1,"two":2}
print(a)
print(b)
print(c)
print(dict_1)

#write a python to square of a number
a=int(input("Enter a number:"))
Square=a*a
print("Square of a number:",Square)

#find the avg of 3 number you have to get input from the user
a=float(input("Enter First Number:"))
b=float(input("Enter Second Number:"))
c=float(input("Enter Third Number:"))
avg=(a+b+c)/3
print("Average is:",avg)

#write a python program to take a num as any user and multiplied by 10
a=int(input("Enter a number:"))
b=a*10
print("After multipying with 10:",b)

#write a python program to covert min into sec
a=int(input("Enter Minutes"))
sec=a*60
print("Seconds=",sec)

#write a python program to floating points
a=float(input("Enter First Number:"))
b=float(input("Enter Second Number:"))
Product=a*b
print("Product=",Product)

#largest of three numbers
a=float(input("Enter First Number:"))
b=float(input("Enter Second Number:"))
c=float(input("Enter Third Number:"))
largest_number=max(a,b,c)
print("Largest number is:",largest_number)

#sum of first n natural number
n=(int(input("Enter input=")))
sum=n*(n+1)
print("Sum=",sum)

#arthimatic
a=10
b=20
print("addition=",a+b)
print("Subtration=",a-b)
print("Multiplication=",a*b)
prinBasic python program.py
￼
t("Module division=",a%b)

#logical operator
a=10
b=12
print(a>0 and b>15)
print(a>15 or b>5)
print(not(a==10))


#write a python program to print positive and negitive and zero
a=int(input("enter the number"))
if a>0:
    print("positive")
elif a<0:
    print("negitive")
else:
    print("zero")        

#write a python program even and odd
a=int(input("enter the number"))
if (a%2==0):
    print("number is even")
else:
    print("number is odd")    


#write a python program to check the number is divisible by 5 and 11
a=int(input("enter the number"))
if (a%5==0 and a%11==0):
    print("the number is divisible by 5 and 11")
else:
    print("the number is not dividible")    
    #age
age=int(input("enter:"))
if(age<13):
  print("child")
elif(age>13 and age <=19):
  print("teenage")
else:
  print("adult")
    #grading
m=int(input("enter marks"))
if m>=90:
  print("grade is A excellent")
elif (m>=70 and m<90):
  print("grade is B nice")
elif (m>=50 and m<70):
  print("grade is C average")
elif(m>=40 and m<50):
  print("grade is D below average")
else:
  print("fail")
#days(1-7)
a = int(input("choose a number (1-7):"))
if a==1:
  print("sunday")
elif a==2:
  print("monday")
elif a==3:
  print("tuesday")
elif a==4:
  print("wednesday")
elif a==5:
  print("thursday")
elif a==6:
  print("friday")
elif a==7:
  print("saturday")
else:
  print("invalid input")
    #check user name and possword
username = "bunny"
psd = 6457

while True:
    user = input("enter username: ")
    if username == user:
        break
    else:
        print("Incorrect username. Please try again.")

while True:
    possword = int(input("enter password: "))
    if psd == possword:
        break
    else:
        print("Incorrect password. Please try again.")

print("login success")
#calculator
a=int(input("enter a number"))
b=int(input("enter a number"))
cal=int(input("enter 1 for add,2 for sub,3 for mul,4 for div"))
if cal==1:
  print(a+b)
elif cal==2:
  print(a-b)
elif cal==3:
  print(a*b)
elif cal==4:
  print(a/b)
else:
  print("invalid choice")
#body temperature
temp=float(input("enter body temperature"))
if temp==98.6:
  print("normal")
elif temp<98.6:
  print("cold")
else:
  print("fever")
#n is multiply by 10
n=int(input("enter a number"))
s=n%10
print(s)
m=int(input())
n=int(input())
total=0
if (m>n):
  print(0)
else :
  for i in range(m,n+1) :
    total+=i**3
  print(total)
#student pass in theory,practicals and toatal
a=int(input("enter theory marks"))
b=int(input("enter practical marks"))
c=int(input("enter total marks"))
if(a>=35 and b>=15 or c>=60):
  print("pass")
else:
  print("fail")

#atm access
cardinserted=True
correct_pin="2324"
enteredpin=input("enter pin")
accountblocked=False
if (cardinserted and not accountblocked and enteredpin==correct_pin):
  print("access granted")
else:
  print("access denied")
#binary search
def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1  
    return -1
arr=[1,2,3,4,5]
target=3
result=binary_search(arr,target)
if result != -1:
    print(f"element found at index {result}")
else:
  print(f"element not found")               
#linear search
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=[1,2,3,4,54,6,4,885]
target=4
result=linear_search(arr,target)
if result != -1:
    print(f"element found at index {result}")
else:
  print(f"element not found")
#m,n range cubes sum
m=int(input())
n=int(input())
total=0
if (m>n):
  print(0)
else :
  for i in range(m,n+1) :
    total+=i**3
  print(total)
#
