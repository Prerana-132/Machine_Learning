#!/usr/bin/env python
# coding: utf-8

# In[3]:


# write a programe to get the number of occurences of a specified element in a array.
number=[1,2,3,3,3,4,5,4,5,6]
a=number.count(3)
print("no.of times 3 has occured",a)
b=number.count(4)
print("no.of times 4 has occured",b)
c=number.count(5)
print("no.of times 5 has occured",c)



# In[5]:


#Reverse a list
def reverselist(arr,start,end):
 while start < end:
  arr[start],arr[end]=arr[end],arr[start]
  start+=1
  end-=1
arr=[10,20,30,40,50,60]
reverselist(arr,0,5)
print(arr)


# In[10]:


#check the duplicate element
def check_duplicate(a):
     myset=set(a)
     if len(myset)==len(a):
        print(" false")
     else:
        print("true")
list1=[1,2,3,4,7,8,0]
print("list1 is:",list1)
check_duplicate(list1)
list2=[1,2,5,6,7,3,8,6]
print("list2 is:",list2)
check_duplicate(list2)


# In[17]:


#equality of a array
array1=[3,2,1,4,5,6]
array2=[3,4,1,5,2,6]
a=sorted(array1)
b=sorted(array2)
print(a)
print(b)
if a == b:
    print(" equal")
else:
    print("not equal")


# In[1]:


#write a program to get the current memoery address and length of a buffer used to store a element in the array
from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
print("Current memory address & length in elements of the buffer: "+str(array_num.buffer_info()))
print("Size of the memory buffer in bytes: "+str(array_num.buffer_info()[1] * array_num.itemsize))


# In[5]:


# user input of no. of elements and enter the data and print the list
list=[]
n=int(input("enter the no.of elements:"))
for i in range(n):
 list2=int(input("enter the elements:"))
 list.append(list2)
print(list)


# In[19]:


list=[]
n=int(input("enter the no.of iteration:"))
m=int(input("enter the no.:"))
for i in range(m,n,m):
    print(i)
 


# 

# In[40]:


list=["cat","mat","hen","men"]
n=len(list)
for i in list:
    if(i=="hen"):
        break
    print(i)
       


# In[45]:


list=["cat","mat","hen","men"]
n=len(list)
for i in list:
    if(i=="hen"):
        continue
    print(i)


# In[3]:


# first 10 natural numbers
for i in range(1,11):
    print(i)


# In[ ]:


# calculator using functions
a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
def add_num (a,b):
    sum=a+b
    return sum
def sub_num (a,b):
    sub=a-b
    return sub
def mul_num (a,b):
    mul=a*b
    return mul
def div_num (a,b):
    div=a/b
    return div
def fdiv_num (a,b):
    fdiv=a//b
    return fdiv
print("enter the option")
n=int(input("enter 1---sum,2--sub,3---mul,4--div,5--fdiv"))
if(n==1):
    print("addition",add_num(a,b))
    
if(n==2):
     print("subtraction",sub-num(a,b))
   
if(n==3):
    print("multiplication", mul_num(a,b))
   
if(n==4):
     print("division",div_num(a,b))
   
if(n==5):
     print("floor division",fdiv_num(a,b))
 


# In[13]:


#tables using functions
def table(x):
    for i in range(1,11,1):
        list2.append(x*i)
        print(x,"*",i,"=",list2[i-1])
list2 = []
x1 = int(input("enter the table number:"))
table(x1)



# In[4]:


# fibonacci series
n = int(input("enter the no.of series"))
num1 = 0
num2 = 1
next_number = num2
count = 1

while count <= n:
	print(next_number, end=" ")
	count += 1
	num1, num2 = num2, next_number
	next_number = num1 + num2
print()


# In[7]:


# factorial of first 10 odd numbers
fact=1
n=int(input("enter the no.of factorial series"))
for i in range(1,n,2):
      fact=fact*i
      print(fact)


# In[8]:


#print first 10 odd numbers
n=int(input("enter the no.of factorial series"))
for i in range(1,n,2):
      print(i)


# In[18]:


#print first 10 odd numbers
n=int(input("enter the no. series"))
for i in range(0,n,2):
      print(i)


# In[30]:


# first 10 even numbers in reverse order 
list2 = []
n = int(input("enter the table number:"))
for i in range(0,n,2):
    list2.append(i)
list2.reverse()
print(list2)


# In[2]:


#half ascending and half descending
list1 = []
list2 = []
n2 = int(input("Enter number of elements: "))
n3 = int(n2/2)

for i in range(0,n3):
    x = int(input("Please Enter Ascending Element: "))
    list1.append(x)
    
print()
for i in range(n3,n2):
    x = int(input("Please Enter Descending Element: "))
    list2.append(x)
    
print()
print("Original Nos:       ",list1 + list2)
print("half Ascending Nos: ",list1)
list2.reverse()
print("half Descending Nos:",list2)


# In[3]:


#separate odd and even numbers from array
evenlist = []
oddlist = []
n1 = int(input("Enter number of elements:"))
for i in range(n1):
    x = int(input("Please Enter Element:"))
    y = x%2
    if y==0 :
        evenlist.append(x)
    else :
        oddlist.append(x)
print()
print("Even Nos:",evenlist)
print("Odd Nos :",oddlist)


# In[4]:


#average of 10 numbers
average = []
y = 0
for i in range(10):
    x = int(input(" Enter the Element:"))
    y = x+y

n = (y/10)
print()
print("Average of Number:",n)


# In[10]:


#all numbers divisible by 11 but not 2 between 100 to 500
list= []

for i in range(101,500,2):
    if (((i%11)==0)):
        list.append(i)
print("Numbers:",list)


# In[9]:


#Write a program that keep on accepting numbers from the user until user enters 00. Display factorial of entered numbers
list = []
k = 1

while k!= 0:
    x=int(input("Enter Number:"))
    if (x!=00):
        list.append(x)
    else:
        print("Numbers:",list)
        break
        
print()
def fact(n: int):
       
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

length = len(list)
print()
for i in range(length):
    num = list.pop()
    ans = fact(num)
    print("Factorial of", num, "is",ans)


# In[ ]:




