__builtins__.end = None

'''
adj="lovely"
name="Rabbits"
print("{} are {} animal".format(name,adj))

print("{0:.3f}".format(1.0/3))

print("{0:*^11}".format("Hello"))

print("{name:*^10} is best in the {where}".format(name='PHP',where='world'))
'''

'''print("a",end='')
print("b",end='')
print("c\n")
'''

'''
print('What\'s your name?')
print('The file is in D\\')
print("This is first line\nThis is second line")
print("The line will\
not the end") #this line == print("The line will not the end")
print(r"The \" is \\ a \t row \n line")
'''

'''
����='Hello'
print(����)
_1ver="World"
print(_1ver)
'''

'''
s="This is a long string.\
This continues the string.\
This is called ��ʾ������\
(Explict Line Joining)"
print(s)
'''

'''
str_1='a'
str_2='b'
num_1=3
num_2=6
num_3=0
num_4=1
print(str_1+str_2)
#print(str_1-str_2) has no meaning
print(str_1*3+str_2*3)
print(num_1**3)
print(num_3>>2)
print(num_4<<2)
print(not 0)
print(1 or 0)
'''

'''
a=3
a**=3
print(a)
'''

'''
print("Please Enter The Interger:")
right_number=23
guess=int(input())
    if guess==right_number:
        print("Congratulations! You guess right!")
    elif guess>right_number:
        print("No, its a little higher than it!")
    else:
        print("No, its a little lower than it!")
print("{string:*^10}".format(string="END"))
'''

'''
import sys
print("The command line arguments are:")
for i in sys.argv:
    print(i)

print("\n\nThe PythonPath is",sys.path,"\n")
'''

'''
import math
print("Enter num:")
num=int(input())
print("The square root is:",math.sqrt(num))

import os
print(os.getcwd)
'''

'''
from math import sqrt
print("Enter num:")
num=int(input())
print("The square root is\
{number:*^99}:".format(number=sqrt(num)))
'''

'''
import math
print("---Enter age and number---")
age=int(input("Age:"))
number=int(input("Number:"))
print("\nWhen its INT")
print("Number is {1:*^10}\nAge    is {0:*^10} \
".format(math.sqrt(age),math.sqrt(number)))
print("\nWhen its Float")
age=float(age)
number=float(number)
print("Number is {1:*^10}\nAge    is {0:*^10} \
".format(math.sqrt(age),math.sqrt(number)))
print("\nWhen its Complex")
'''

'''
import math
from math import sqrt
print("Enter what you want:")
judge=bool(input())
if judge:
    print("The square is {0:*^20}".format(sqrt(judge)))
'''

'''
import math
complex_number=complex(input())
print("{0:*^20}".format(math.sqrt(complex_number)))
'''

'''
import cmath
a=2
print(cmath.sqrt(a))
'''

'''
这是和同一文件夹下的test2.py文件一起的main测试程序1
import test0
test0.main()
'''

'''
import math as mt
print("{0}".format(mt.sqrt(16)))
'''

'''
animal=["cat","dog","rabbit","monkey","Godzilla"]
print("Enter the uncommon animals:")
rkey=5
while(1):
    animal_add=input()
    key=1
    for i in range(0,rkey):   #== for(i；i<rkey;i++)
        if animal_add==animal[i]:
            print("Its common!")
            key=0
            break
    print("\nThe final list is :")
    if key:
        animal.insert(rkey,animal_add)
        rkey=rkey+1
        for i in range(0,rkey):
            print(animal[i],end=" ")
    else:
        for i in range(0,rkey):
            print(animal[i],end=" ")
    print("\nEnter the uncommon animals:")
#animal[rkey]=animal_add 不能直接对界外位置的列表元素赋值,要用方法
'''

'''
animal_0=["cat","dog","rabbit","monkey","Godzilla"]
animal_1=["shark","lion","elephant","kangaroo","bird"]
#animal_0.extend(animal_1)
animal_0.extend(animal_1)
for i in range(0,10):
    print(animal_0[i])
'''

'''
animal_0=["cat","dog","rabbit","monkey","Godzilla"]
animal_0.extend(["lion"])
for i in range(0,6):
    print(animal_0[i])
'''

'''
animal=["cat","dog","rabbit"]
del animal[0]
print(animal)
'''

'''
animal=["cat","dog","rabbit"]
delete_animal=animal.pop(0)
print(delete_animal)
'''

'''
animal=["cat","dog","rabbit"]
delete_animal=animal.remove("cat")
print(delete_animal)
'''

'''
animal=["a","c","b"]
print("Original list:",animal)
animal.sort()
print("Using .sort()")
print(animal)
animal.sort(reverse=True)
print("Using .sort(reserve=True)")
print(animal)
print("Using sorted()")
print(sorted(animal))
print(len(animal))
print(animal.index("b"))
'''

'''
old_zoo=("dog","cat","monkey")
new_zoo=("python","penguin","elephant",old_zoo)
print("The old zoo list ",old_zoo)
print("The new zoo list ",new_zoo)
print("The old zoo\'s last animal is ",new_zoo[3][2])
for i in range(0,3):
    print("The old zoo has {animal}".format(animal=new_zoo[3][i]).title())
'''

'''
dictionary1={
"animal0":"cat",
"animal1":"dog",
"animal2":"lion",
"animal3":"monkey"
}
max_dic=4
#key_dic="animal0"
for i in range(0,max_dic):
    if i<max_dic:
        key_dic="animal"+str(i)
    print("The {0}th animal\'s name is:{1}".format(i,dictionary1[key_dic]))
    print(key_dic)
#为什么animal1键值反倒能调用字典里key为animal0的值？
'''

'''
dictionary1={
"animal0":"cat",
"animal1":"dog",
"animal2":"lion",
"animal3":"monkey"
}
max_dic=4
key_dic="animal0"
for i in range(0,max_dic):
    print("The {0}th animal\'s name is:{1}".format(i,dictionary1[key_dic]))
    print(key_dic)
    if i<max_dic:
        key_dic="animal"+str(i+1)
'''

'''
dictionary1={
"animal0":"cat",
"animal1":"dog",
"animal2":"lion",
"animal3":"monkey"
}
dictionary1["animal4"]=dictionary1
print(dictionary1["animal4"])
dictionary1[1+2j]="tiger"
print(dictionary1[1+2j])
dictionary1[("nihao")]="Hello"
print(dictionary1[("nihao")])
#dictionary1[["nihao"]]="Hello" #列表不可用做键值
#print(dictionary1[["nihao"]])
'''

'''
a=int(input())
print("The type is :",type(a))
'''

'''
string_test=0
print(str(string_test))
'''

'''
#It's wrong
dictionary1={
"animal0":"cat",
"animal1":"dog",
"animal2":"lion",
"animal3":"monkey"
}
for i in range(0,5):
    print(dictionary1[i])
'''

'''
list_section_test=["cat","dog","python","shark","monkey","Godzilla"]
print(list_section_test[0:6:2])
print(list_section_test[-2::-1])
print(list_section_test[:6:2])
print(list_section_test[::-2])
print(list_section_test[:])
list_section_test2=list_section_test[:]
print(list_section_test2)
'''

'''
list_set_test=['a','c','b']
list_set_test=set(list_set_test)
print(list_set_test)
'''

'''
list_set_test=['a','c','b']
list_set_test2=list_set_test
print(list_set_test)
del(list_set_test[0])
print(list_set_test2)
'''

'''
list_set_test=['a','c','b']
list_set_test2=list_set_test[:]
print(list_set_test)
del(list_set_test[0])
print(list_set_test2)
'''

'''
x=100
def fun():
    global x
    x=1
    print(x)
fun()
print(x)
'''

'''
def Outer():
    a=10
    def Inder():
        a=1
        print(a)
        def Inder2():
            nonlocal a
            a=10086
        Inder2()
        print(a)
    Inder()
    print(a)
Outer()
'''

'''
def fun ():
    print("Hello")
dic1={"key0":fun()}
dic1["key0"]
'''

'''
dic2={"key0":"index0","key1":"index1","key2":"index2"}
for i in range(0,3):
    print(dic2["key"+str(i)])
'''

'''
def fun_animal_print():
    animals=["cat","tiger","dog","shark","godzilla"]
    for animal in animals:
        print(animal.title())
        print("I like {0} so much".format(animal))
        print("But {0} is\' not my favourite\n".format(animal.title()))
        if __name__ == "__main__":
            print("I like python so much!")
fun_animal_print()
'''

'''
import test0
test0.fun_animal_print()
'''

'''
squares=[]
for value in range(1,11,1):
    square=value**2
    squares.append(square)
for i in range(0,len(squares)):
    print(squares[i],end=" ")
    if i==(len(squares)-1):
        print("\n")
#The first way
list=list(range(1,11,1))
for i in range(0,len(list)):
    print(list[i]**2,end=" ")
    if i==len(list)-1:
        print("\n")
#The second way
list_analysis=[value**2 for value in range(1,11,1)]
for i in range(0,len(list_analysis)):
    print(list_analysis[i],end=" ")
#The third way (列表解析)
'''

#以下为列表解析的练习
'''
list_even_numb=[even_numb for even_numb in range(1,101) if even_numb%2==0]
for i in range(0,len(list_even_numb)):
    print(list_even_numb[i],end="_")
'''
#normal code 1:
'''
text="My favourite language is Python"
list_first_chart=[]
for word in text.split():
    list_first_chart.append(word[0])
for i in range(0,len(list_first_chart)):
    print(list_first_chart[i],end=" ")
    if i == len(list_first_chart)-1:
        print("\n")
#list list analysis 1:
text="My favourite language is Python"
list_first_chart_2=[word[0] for word in text.split()]
for i in range(0,len(list_first_chart_2)):
    print(list_first_chart_2[i],end=" ")
    if i == len(list_first_chart_2):
        print("\n")
'''
#list analysis 2:
'''
a=[1,2,3,4]
b=[5,6,7,8]
list_combine=[i*j for i,j in zip(a,b)]
print(list_combine)
#for i in range(0,len(list_combine)):
#    print(list_combine[i],end=" ")
'''

'''
a=[1,2,3,4]
b=[5,6,7,8]
c=['a','b','c','d']
print(zip(a,b,c))
for i in zip(a,b,c):
    print(i)
'''

'''
a=[1,2,3,4]
b=['a','b','c','d','d','e']
c=["Nihao","Hello","Bonjour"] #此为最短序列
print(list(zip(a,b,c)))
'''

'''
list_2=[[1,2,3],[4,5,6],[7,8,9]]
print([[j[i] for j in list_2] for i in range(len(list_2[0]))])
print(list(zip[*list_2]))
'''

'''
days=['Monday','Tuesday','Wednesday']
fruits=['Apple','Banana','Pear']
drinks=['Tea','Juice','Coke']
list_diet=list(zip(days,fruits,drinks))
print(list_diet)
'''
'''
for day,fruit,drink in zip(days,fruits,drinks):
    print("{0:*^10}  Eat{1:*^10}  Drink{2:*^10}".format(day,fruit,drink))
'''

'''
list_ifelse=['1','2','3','4','5','o','6']
list_ifelse2=[int(i) if str(i).isdigit() else None for i in list_ifelse]
print(list_ifelse2)
'''

'''
import test0
a=int(input("Pleas intput a&b\n"))
b=int(input())
print("The value of a add b is:{:*^10}".format(test0.fun_add(a,b)))
'''


'''
import sys
list_iter=['a',2,"Helllo","___"]
it=iter(list_iter)
for value in it:
    print(value,end=" ")
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
'''

'''
a=3
b=4
a,b=b,a+b
print(a,b)
'''

'''
list_inter2=[1,2,3,4]
print(iter(list_inter2))
it=iter(list_inter2)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it)) #此行输出时会遇到StopIterration异常而结束
'''

'''
import sys
list_inter3=[1,2,3,4,5]
it0=list_inter3
for date0 in it0:
    print("{:>8}".format(date0))
it1=iter(list_inter3)
print("----------------")
for date1 in it1:
    print("{:>8}".format(date1))
'''

'''
a="test"
print("{0:>8}".format(a))
print("{0:^8}".format(a))
print("{0:*^8}".format(a))
'''

'''
a=13
print("{0:b}".format(a))
print("{0:d}".format(a))
print("{0:o}".format(a))
print("{0:x}".format(a))
'''
'''
print("{0:,}".format(123456789))
print("{0:.3f}".format(31.245567348))
'''

'''
list_temp=[1,2,3,4]
tuple_temp=('a','b','c','d')
dict_temp={"key0":"Nihao","key1":"Hello","key2":"Bonjour"}
def fun_temp():
    print("Test")
def print_info(monkey,*charts):
    print("输出part1:")
    print(monkey+'\n')
    #if charts:
    print("输出part2:")
    for date in charts:
        print("此时对象类型为：",end="")
        print(type(date))
        print(date)
list_temp_iter=iter(list_temp)
print(print_info("SRH","nihao",2018426,list_temp,tuple_temp,dict_temp,fun_temp,list_temp_iter))
'''

'''
You=True
def Love():
    if You:
        Love()
'''
'''
#x=(y=1)
x=1;y=2
print("Hello",x,y)
'''



'''
dict_traversal={
    "jen":"python",
    "jack":"ruby",
    "tom":"c",
    "outman":"c++",
    "Toky":"Python",
}
dict_traversal_2={
    'a':"nihao",
    'c':"Hello",
    'b':"Bonjour",
    'd':"Hello"
}
'''

'''
for name,language in dict_traversal.items():
    print(name.title()+
    "'s favourite language is "+
    language.title()+'!')
    print("\n{0:>8}'s favourite language is {1:*^8}\n"
    .format(name.title(),language.title()))
'''
'''
for date in set(dict_traversal_2.values()):
    print(date)
'''


'''
count=0
list_alien_first=[]
for i in range(0,30):
    dict_alien={"color":"green","point":5,"speed":"slow"}
    list_alien_first.append(dict_alien)
#以上是对包含字典的列表的创建
'''
'''
for i in range(0,30):
    print("\n")
    print(list_alien_first[i])
    count=count+1
print("\nThe total number is {0}".format(count))
'''
'''
#以上是对包含所有字典的完整列表的输出
for alien in list_alien_first[:3]:
    alien["color"]="yellow"
    alien["point"]="10"
    alien["speed"]="medium"
for alien in list_alien_first[:3]:
    print("\n")
    print(alien)
print("是否全面升级？(Y/N)")
judge=input()
if ((judge=='Y')or(judge=='y')):
    for alien in list_alien_first:
        if  "green"==alien["color"]:
            alien["color"]="yellow"
            alien["point"]="10"
            alien["speed"]="medium"
        elif "yellow"==alien["color"]:
            alien["color"]="red"
            alien["point"]="15"
            alien["speed"]="quick"
#以上是对列表中部分字典的单独修改
for i in range(0,30):
    print("\n")
    print(list_alien_first[i])
'''


'''
dic_list={
    "jake":["python","ruby"],
    "tom":["c++","java"],
    "outman":["haskell","PHP"],
    "peiqi":["html"]
}
for name,languages in dic_list.items():
    if len(languages) > 1:
        print("\n"+name.title()+"'s favourite languages are:",end=" ")
    else:
        print("\n"+name.title()+"'s favourite languages is:",end=" ")
        for language in languages:
            if language != "PHP":
                print(language.title(),end=" ")
            else:
                print(language.upper(),end=" ")
'''
#以上是对字典包含列表的练习



dic_dic={
    "toky":{
        "first":"toky",
        "last":"shi",
        "location":"jinhua",
    },
    "tom":{
        "first":"tom",
        "last":"braun",
        "location":"german",
    }
}
#for dic in dic_dic:
for user,date in dic_dic.items():
    print("\n"+"\t"+"Username:",end=" ")
    print(date["first"].title(),end=" ")
    print(date["last"].title())
    print("\t"+"Location:",end=" ")
    print(date["location"].title())
