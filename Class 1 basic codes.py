#!/usr/bin/env python
# coding: utf-8

# In[3]:


a="hello, world!"
print(a.replace("h","j"))


# In[4]:


a="hello world!"
print(a.split(","))#returns['hello','world!']


# In[5]:


a="hello world"
print(a)


# In[53]:


a="hello ,world!"
print(a.strip())# returns "hello,world"


# In[8]:


a="hello world"
print(len(a))


# In[9]:


a=(10,20,30,40)
print(len(a))


# In[15]:


for i in range(10,50,5):
  print(i)


# In[32]:


a=input("enter your first name:")
b=input ("enter your last name:")
print("USERS FIRST NAME IS",a)
print("USERS LAST NAME IS",b)


# In[33]:


a=int(input("enter the first number:"))
b=int(input("enter the second number"))
sum=a+b
print("SUM:",sum)
diff=a-b
print("DIFFERENCE:",diff)
mul=a*b
print("PRODUCT:",mul)
div=a/b
print("DIVISION:",div)


# In[44]:


a=int(input("enter the 1st no."))
b=int(input("enter the 2nd no."))
c=a & b
d=a | b
e=a ^ b
print("AND",c)
print("OR",d)
9print("xOR",e)


# In[6]:


a=int(input("enter the 1st no."))
b=int(input("enter the 2nd no."))
print("1:-add,2:-sub,3:-mul,4:-div")
c=int(input("enter the option"))
if (c==1):
 sum=a+b
 print("SUM:",sum) 
elif (c==2):
 diff=a-b
 print("DIFFERENCE:",diff)
elif (c==3):
 mul=a*b
 print("PRODUCT:",mul)
elif (c==4):
 div=a/b
 print("DIVISION:",div)
else:
 print("invalid")


# In[1]:


#createlist
fruits=["apple","mango","grapes",]
print(fruits)


# In[5]:


fruits=["apple","mango","grapes",]
print(fruits[2])


# In[8]:


list1=["trees","sky","birds"]
list2=["beautiful","23","34","blue","45"]
list3=[]
print(list1[-2],list2[3])
print(list2[1:])
print(list2[1:3])
print(list3)


# In[31]:


#append operation
number=["12","34","45","5","67"]
rate=["1","2","3","5"]
number.append(32)
print("after append:",number)
print(len(number))
#extent operation
number.extend(rate)
print("after extend:",number)
print(len(number))
#insert operation
number.insert(2,77)
print("after insertion:",number)
print(len(number))


# In[24]:


#replace element
number=["12","34","45","5","67"]
print("previous list:")
print (number)
number[2]=88;
print("new list")
print (number)


# In[33]:


list=[]
n=int(input("enter the elements"))
for i in range(0,n):
 list2=int(input())
 list.append(list2)
 print(list2)


# 
# ##### 

# In[28]:


emp=["john",102,"usa"]
dep1=["cs",10]
dep2=["it",11]
hod_cs=[10,"mr.holding"]
hod_it=[11,"mr.bewon"]
print("EMPLOYEE DATA:")
print("name:-",emp[0],"id:-",emp[1],"Place:-",emp[2])
print("DEPARTMENT 1")
print("name:-",dep1[0],"id:-",dep1[1])
print("DEPARTMENT 2")
print("name:-",dep2[0],"id:-",dep2[1])
print("HOD DETAILS")
print("name:-",hod_cs[1],"id:-",hod_cs[0])
print("name:-",hod_it[1],"id:-",hod_it[0])
print(type(emp),type(dep1),type(dep2),type(hod_cs))


# 

# In[46]:


#truple
truple=(1,2,3,4,5,6,"apple","mango","grape")
print(truple)


# In[3]:


#sets
set={"rose","sunflower","jasmine","marygold"}
print(set)


# In[5]:


#add and update a element from a set
set={"rose","sunflower","jasmine","marygold"}
set2={"cat","dog","tiger","lion"}
set.add("lotus")
print(set)
set.update(set2)
print(set)


# In[6]:


#discrd a element from a set
set={"rose","sunflower","jasmine","marygold"}
set.discard("rose")
print(set)


# In[14]:


#sets
set={"rose","sunflower","jasmine","marygold"}
print(set)


# In[12]:


#union operation
set={"rose","sunflower","jasmine","marygold"}
set2={"cat","dog","tiger","lion","rose","jasmine"}
set.union(set2)



# In[13]:


#intersection operation
set={"rose","sunflower","jasmine","marygold"}
set2={"cat","dog","tiger","lion","rose","jasmine"}
set.intersection(set2)


# In[16]:


#difference operation
set={"rose","sunflower","jasmine","marygold"}
set2={"cat","dog","tiger","lion","rose","jasmine"}
set.difference(set2)


# In[24]:


#Accesses the elements of set
set={"rose","sunflower","jasmine","marygold"}
set1=list(set)
print(set1)
print(set1[2:])


# In[31]:


dist={"hi","hello","bye"}
print(dist)


# In[11]:


#equality of a array
array1=[3,2,1,4,5,6]
array2=[3,4,1,5,6,2]
a=sorted(array1)
b=sorted(array2)
print(a)
print(b)
if a == b:
    print(" equal")
else:
    print("not equal")


# In[10]:


l1 = [10, 20, 30, 40, 50]
l2 = [20, 30, 50, 40, 10]
l3 = [50, 10, 30, 20, 40]

l1_sorted = sorted(l1)
l2_sorted = sorted(l2)
l3_sorted = sorted(l3)

if l1_sorted == l2_sorted:
    print ("The lists l1 and l2 are the same")
else:
    print ("The lists l1 and l2 are not the same")

if l1_sorted == l3_sorted:
    print ("The lists l1 and l3 are the same")
else:
    print ("The lists l1 and l3 are not the same")
    


# In[7]:


list=["cat","mat","hen","men"]
n=len(list)
for i in list:
    if(i=="hen"):
        break
    print(i)       


# In[ ]:




