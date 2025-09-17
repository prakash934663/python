
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

