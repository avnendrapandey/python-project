print("hello","i am avnendra")#string
#print(23)
#print(5+4)
#name="satyam"
#age=56
#age2=age
#price=89.9
#print(name,age2,price)
#print(type(name))
#print(type(age))
#print(type(price))
#age=56
#old=False
#a=None
#print(type(old))
#print(type(a))
#a=5
#c=7
#sum=a+c
#print(sum)
"""this is multiline comment"""
#name=input("name:")# it is used to take value from user
#age=int(input("age:"))
#price=float(input("price:"))
#print(price)
#print(type(name))
#print(type(age))
#print("my name is",name,"and i am", age)
#conditional statement
#else,elif,if
#light=input("light color :")
#if(light=="red"):
#  print("stop")
#elif(light=="yellow"):
#  print("look")
#elif(light=="green"):
#  print("go")
#else:
 # print("light is broken")  
#Marks=input("Marks:")
#if Marks >= '90':
  #  print("A")
#elif Marks >= '80' and Marks < '90':
   # print("B")
#elif Marks>= '70' and Marks < '80':
 #   print("C")
#else:
 #   print("D")
  #  print(6/3) #always give floating value while divide
#print(4**2)# means a^b
#conditiona; statement
a=50
b=60
#val1=False
#val2=True
#print("AND operator:", val1 and val2)
#print("OR oprator:",(a==b)or(b>a))
'''type conversion  in python interpretor  doing automatically AND type casting doing manually by user'''
"""a=int("5")
b=4.25
print(type(a))
print(a+b)
a=3.14
a=str(a)
print(type(a))
val=input("enter some value")
print(type(val),val)"""
#string string is a data type that srores sequence of characterstr1="this is str"
#str1="Apna collage"
#len1=len(str1)
#print(len1)
# indexing it is used to access charactrer
#str="apna collage"
#print(str[0])
#slicing accssing parts of string
#str="APNA_ COLLAGE"
#print(str[0:4])
#str="APPLE"
#print(str[-3:-1])# string function
#str="I am a coder from maharaganj UP goverment has been qualified to next class of presecption mong and javascript of a logic"
#print(str.endswith("gic"))
#print(str.replace("UP","MP"))
#print(str.find("a"))
#print(str.count("a"))
#Lists a build in data type that stores set of values it can store different type of (integer,float,string) etc
#string is immutable but lists is mutable(means we can access ands change)
#marks=[94.5,37.8,45.6,97.5,89.2]
#print(marks)
#print(type(marks))
#print(marks[2])
#print(len(marks))
#student=["mohan",67.6,19]
#student[0]="avnendra"
#print(student)
#lists methods
#list=[6,9,2,1,4,0,6,]
#list.append(3)
#print(list)
#print(list.sort())
#print(list.sort(reverse=True))
#print(list.reverse())
#print(list.insert(1,25.8))
#print(list)
#TUPLES create immutuable sequence of value
#loops in python
# count=1
# while count<=5:
#   print("hio")
#   count+=1
# no=[1,4,9,16,25,36,49,64,81,100]
# idx=3
# while idx<len(no):
#   print(no[idx])
#   idx+=1
#dictionary are used to store data values in key.values pairs
# they are unordered, mutable(changable) and don,t allow duplicate keys
# info={
#   "key":"value",
#   "name":"satyam",
#   "subjects":["python","c", "java"],#Lists
#   "topics":("dict", "set"),#Tuples
#   "learning":"coding",
#   "age":89,
#   "isadult":True,
#   "marks":76.6,
#   98:89.9
# }
# print(info)
# print(info["name"])
# print(type("name"))
#tuple is a built-in data type that lets create imutable sequences of values
# /
#user1=input("enter the name of movie")
#movies.append(input("enter movie by user2"))
#user3=input("movir name")
#movies.append(user1)
#movies.append(user3)
#print(movies)
# list1=[1,3,4]
# list2=[1,3,5]
# copy_list1=list1.copy()
# copy_list1.reverse()
# if(copy_list1==list1):
#   print("palindrome")
# else:
#   print("not palindrome")
#   grade=("c","d","a","a","b","b","a")
#   print(grade.count("a"))
#   grade.sort()
#   print(grade)
  #  info["name"]="A.K pandey"
  # print(info)#dictionary and set start
  # info["surname"]="PANDEY JI"
  # print(info)
  # student={
  #   "name":"rahul kumar",
  #   "subjects":{
  #     "phy":89,
  #     "chem":67,
  #     "maths":95

  #   }
  # }
#print(student)
# print(student["subjects"]["maths"])
# for i in range(1,100,2):
#   print(i)
#   for el in range(10):
#    pass
#   for j in range(1,99,4):
#     print(j)
# rows=5
# for i in range(1,rows+1):
#   print("* " *i)
#   rows=5
#   for i in range(rows,0,-1):
#     print("*"*i) 
# rows=5
# for i in range(1,6):
#   print(' '.join(str(x) for x in range(1,i+1) ))
#no is armstrong
# list=[2,3,4,6,7]
# list.append(9)#used for adding elements
# print(list)
# print(max(list))
# print(min(list))
# import copy
# original=[1,4,5]
# shallow_copy=copy.copy(original)
# shallow_copy[1]=99
# print(original)
# print(shallow_copy)
# L=[1,2,3,4,5,6,7,8,9]
# Result1=L[::-1][:-1]
# print(Result1)
# result2=L[2:-1]
# print(result2)
# result3=L[0::2]
# print(result3)
# middle_index=len(L)//2
# result4=L[middle_index:]
# print(result4)
# middle_index=len(L)//2
# result5=L[:middle_index+1][::-1]+L[middle_index+1:]
# print(result5)
# def makespairs(list2,list3):
#     w=len(list2)
#     c=len(list3)
#     if w==c:
#         pairlis=[(list2[i],list3[i]) for i in range(0,w)]
#         return pairlis
#     print(makespairs([1,3,5,7],[2,4,6,8]))
print("hello")
var=("hello","for","bye")
print(var)
#r+ mode 
filename="recuriment.txt"
with open(filename,"w") as file:
    file.write("this is the original content")
    with open(filename,"r+") as file:
        print("original file content ")
        print(file.read())
        file.seek(0)
        file.write("updated content")
        file.seek(0)
        print("updated content file")
        print(file.read())
        with open(filename,"r") as file:
            print("verified content from the file")
            print(file.read())
            
          




  





  

  
    

