# class A:
#     a = 'klc'
#     def __init__(self):
#         self.b = 'hello'
        
#     def __del__(self):
#         self.d="world"
#         # print(self.d)
# # import pdb;pdb.set_trace()
# c = A()
# print(c.d)

# class Robot():
#     a="hello"
#     b="world"
# if __name__=='__main__':
#     x=Robot()
#     y=Robot()
#     y2=y
    
#     print(y2==y)
#     print(y2==x)
    
# class Robot1():
#     pass 
# x=Robot1()
# y=Robot1()
# print(type(x))
# x.name="marliyn"
# y.build_date=1997
# print(x.name)
# print(y.build_date)
# print(x.__dict__)
# print(y.__dict__)

# class Robot2(object):
#     pass
# x=Robot2()
# Robot2.brand="zara"
# Robot2.company_location='mumbai'
# print(x.brand)
# print(x.company_location)
# print(Robot2.__dict__)
# print(x.__dict__)

# print(x.brand)
# print(getattr(x,x.brand,1))

# def fun_1(obj):
#     print('hi i am'+obj.name+"|")
#     class Robot3():
#         pass
#     x=Robot3()
#     x.name="mrylin"
# fun_1(x)

# def hi(obj):
#         # import pdb;pdb.set_trace()
#         print("Hi, I am " + obj.name)
# class Robot:
#     say_hi = hi
# x = Robot()
# x.name = "Marvin"
# Robot.say_hi(x)

# def fun_1(obj):
#     print("hi this is"+obj)
#     class Root():
#         class_atrr=fun_1
#     x=Root
#     x.build_date="2012-11-10"
#     Root.class_atrr(x)
    
# def fun_2(obj):
#     print("this is obj"+""+obj)
# class Root_1():
#     call=fun_2
# x=Root_1
# x.name="hello world"
# Root_1.call(x.name)

# class Demo():
    
#     def __init__(self):
#         print("it is executed")
# x=Demo()
# print(x)

# class Robot():
#     def __init__(self,name=None):
#         self.name=name
        
#     def fun_1(self):
#         if self.name:
#             print("this is instance name",self.name)
#         else:
#             print("without name")
# x=Robot()
# print(x.name)
# x.fun_1()
# y=Robot('marvin')
# y.fun_1()
# x.fun_1()

# class Robot_1():
#     location="indore"
#     def __init__(self):
#         self.name="shri"
#         self.age="23"
#     def fun_1(self):
#         if self.name:
#             print("this is method and instance",self.name)
            
#         else:
#             print("this is age",self.age)
#     def set_name(self):
#         self.name="Rahul"
#     def get_name(self):
#         print(self.name)
# print(Robot_1.location)
# R1=Robot_1()
# print(R1.name)
# R1.fun_1()
# # print(R1.set_city("mp"))
# x=Robot_1
# y=Robot_1
# x.set_name(y.get_name)
# print(y.get_name())

# class Robot():
#     def __init__(self,name,build_by):
#         self.name=name
#         self.build_by=build_by
        
#     def fun_1(self):
#         if self.name:
#             print("this is instance variable",self.name)
#         else:
#             print("this is not found instance variable")
#         if self.build_by:
#             print("this is second instance",self.build_by)
#         else:
#             print("this is not found second instance",self.build_by)

#     def set_name(self,name):
#         self.name=name
        
#     def get_name(self):
#         print("this is setter objects",self.name)
        
#     def set_build_by(self,build_by):
#         self.build_by=build_by
        
#     def get_build_by(self):
#         print("this is getter  objects",self.build_by)

# a=Robot("henry",2012)
# a.fun_1()
# a.get_name()
# a.get_build_by()

# class A():
#     def __repr__(self,name,age):
#         self.name="demo"
#         self.age=23
        
#     def get_item(self):
#         print("this is gettter",self.name)       
# a=A("hello",23)
# print(repr(a))

# li=[12,3232,4,43,4,24,23]
# s=repr(li)
# print(eval(str(s)))

# class Robot():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
#     def __repr__(self):
#         return ("this is"+self.name+"it is age will"+self.age)
# if __name__=="__main__":
#     a=Robot('marvin',"1979")
#     a_str=str(a)
#     print(a_str)
#     print(type(a_str))
#     a_eval=eval(a)
#     print(type(a_eval(a_str)))
    

# class Robot_2():
#     name="marliyn"
#     def __init__(self,age,location):
#         self.age=age
#         self.location=location
        
#     def __repr__(self):
#         return ("my name is"+" "+self.name+"and age will be"+self.age)

#     def __str__(self):
#         return ("this is my location"+" "+self.location)

# if __name__=='__main__':
#     a=Robot_2('24','indore')
#     print(a)
#     a_str=str(a)
#     print(type(a_str))
    
# class Robot_3():
#     def __init__(self,id,request):
#         self.id=id
#         self.request=request
#         print("this both the objects in created"+self.id+"  "+self)

#     def __del__(self):
#         print("this is deleted in both objects"+self.id+self.request)
# if __name__=="__main__":
#     a=Robot_3("12","get")
#     b=Robot_3("34","post")
#     x=a
#     y=b
#     del b
    
# class Robot_4():
#     counter=0
#     def __init__(self):
#         self.counter+=1
        
#     def __del__(self):
#         self.counter-=1
        
# if __name__=="__main__":
#     a=Robot_4()
#     print("Number of instance"+str(a.counter))
#     b=Robot_4()
#     print("Number of instance"+str(b.counter))
    
    
# class Robot5():
#     counter=0
#     def __init__(self):
#         self.counter+=1
#     def add(self):
#         return Robot5.counter
        
# if __name__=="__main__":
#     a=Robot5()
#     print(a.add())
    
# class Robot6():
#     counter=1
#     def __init__(self):
#         self.counter+=1
#     @staticmethod
#     def RobotInstance():
#         return Robot6.counter
# if __name__=="__main__":
#     r=Robot6()
#     print(r.RobotInstance())
    
# class Robot7():
#     counter=2
#     def __init__(self,counter):
#         type(self).counter+2
#     @staticmethod
#     def RobotInstance():
#         return Robot7.counter
# if __name__=="__main__":
#     R7=Robot7()
#     print(R7.RobotInstance())

# class Robot():
#     counter=10
#     sum=100
#     def __init__(self):
#         self.counter+=10
#     @classmethod
#     def Robotinstance(cls):
#         return cls,Robot.counter,Robot.sum
# if __name__=="__main__":
#     R=Robot
#     print(R.Robotinstance())
    
# class P():
#     def __init__(self,x):
#         self.x=x
#     def get_item(self):
#         return self.x
#     def set_item_1(self,y):
#         self.y=y
#     def get_item_1(self):
#         return self.y
# if __name__=="__main__":
#     p1=P(43)
#     print(p1.get_item_1())
    
# class P1():
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     @property
#     def get_item(self):
#         return self.x
#     @get_item.setter
#     def set_item(self,x):
#         if x<0:
#             self.x=0
#         elif x>1000:
#             self.x=1000
#         else:
#             self.x=x
# if __name__=="__main__":
#     p=P1(100,500)
    # print(p.get_item())
    # print(p.set_item(699))
    
# class P2():
#     def __init__(self,x):
#         self.x=x
#     def get_item(self):
#         return self.x
#     def set_item(self,x):
#         if x<0:
#             self.x=0
#         elif x>1000:
#             self.x=1000
#         else:
#             self.x=x
#     x=property(get_item,set_item)

# class Robot():
#     def __init__(self,name,build_year,lk=0.5,lp=0.5):
#         self.name=name
#         self.build_year=build_year
#         self.physical=lk
#         self.psynic=lp

#     def condition(self):
#         s=self.physical+self.psynic
#         if s<=-1:
#             return "I feel miserable"
#         elif s<=0:
#             return "i feel Bad"
#         elif s<=0.5:
#             return "could be worse"
#         elif s<=1:
#             return "seems to be okay"
#         else:
#             return "Great"        
# if __name__=="__main__":
#     R=Robot('marvin',"1979",0.3,0.2)
#     R1=Robot('caliban',"1957",-0.4,2.0)
#     print(R1.condition)
#     print(R.condition)
    
# class Robot_1():
#     def __init__(self,name,build_year):
#         self.name=name
#         self.build_year=build_year
#     def get_item(self):
#         return self.name
#     def set_item(self,build_year):
#         if build_year>1900:
#             self.build_year=1900
#         else:
#             self.build_year=2000
#     x=property(get_item,set_item)
#     print(x)
    
# class Robot_2():
#     def __init__(self,city):
#         self.city=city
#     @property
#     def city_1(self):
#         return self.city
# if __name__=="__main__":
#     r1=Robot_2("indore")
#     print(type(r1.city_1))

# class Robot():
#     cls_a="this is class attribute of class Robot"
#     def __init__(self):
#         self.ins_a="this is instance attribute in class Robot"
# class Robot_1(Robot):
#     cls_b="this is class attribute of class Robot_1"
#     def __init__(self):
#         ins_b="this is instance attribute of class Robot_1"
#         super().__init__()
#         self.ins_b="this is attribute in class Robot"
# y=Robot_1()
# # print(y.cls_a)
# # print(y.cls_b)
# print(y.ins_a)
# # print(y.ins_b)

# class Blog():
#     b1="this is blog class attribute"
#     def __init__(self):
#         self.b1_ins="this is blog instance attribute"
# class Author(Blog):
#     a1="this is author class attribute"
#     def __init__(self):
#         super().__init__
#         self.a1_ins="this is author instance attribute"
# A1=Author()
# print(A1.a1_ins)

# class Author():
#     A1="this is author class attribute"
#     def __init__(self):
#         self.a1_ins="this is instance author attribute"
# class Entry(Author):
#     e1="this is Entry class attribute"
#     def __init__(self):
#         super().__init__()
#         self.e1_ins="this is instance in entry class"
# class Blog(Entry):
#     b1="this is blog class attribute"
#     def __init__(self):
#         super().__init__()
#         self.b1_ins="this is blog instance in blog class"
# b1=Blog()
# print(b1.b1_ins)

# class Robot():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age   
#     def get_item(self):
#         return ("this is name"+self.name+"and age"+self.age)
# class PhysicianRobot(Robot):
#     pass
# R=Robot("joe","23")
# PR=PhysicianRobot("james","23")
# print(R)
# print(R,type(R))
# print(type(PR))
# print(PR.age)
# print(isinstance(R,PhysicianRobot))

# class A():
#     pass
# class B(A):
#     pass
# class C(B):
#     pass
# x=C()
# print(isinstance(x,A))

# class Robot:
#     def __init__(self, name):
#         self.name = name
#     def say_hi(self):
#         print("Hi, I am " + self.name)
# class PhysicianRobot(Robot):
#     def say_hi(self):
#         print("Everything will be okay! ") 
#         print(self.name + " takes care of you!")
# y = PhysicianRobot("James")
# y.say_hi()

# class Robot:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def get_item(self):
#         return self.name+self.age
# class Demo(Robot):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
#     def get_item(self):
#         return self.name+self.age
# R=Robot("joe","23")
# D=Demo("john","34")
# print(D.get_item)
# print(R.get_item)

# class Robot():
#     names="this is class attribute for Robot"

#     def __init__(self,location,city):
#         self.location=location
#         self.city=city
        
#     def get_item(self):
#         return self.location+self.city
    
# class NurshingRobot():
#     Nr="this is second class attribute"
#     def __init__(self):

# class Length():
#     c_attr={"mm":0.0001,"cm":0.01,"m":1,"km":1000,"in":0.0254,"ft":0.3048}
#     def init(self,unit,value):
#         self.unit=unit
#         self.value=value
        
#     def Converse(self):
#         return self.value*Length.c_attr[self.unit]
    
#     def __str__(self):
#         return str(self.Converse)
#     def __repr__(self):
#         return self.value+self.unit
    
# if __name__=="__main__":
#     x=Length()
#     print(x)

# class Robot():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
#     def __call__(self,):
#         return self.name+self.age
# a=Robot("shri","23")
# print(a())
# import random
# class FoodSupply():
#     def __init__(self,ingredients):
#         self.ingredients=ingredients
#     def __call__(self):
#         return "".join(self.ingredients)+"deliscios"
# f=FoodSupply('salad')
# print(f())

# class FuzzyTraingle():
#     # import pdb;pdb.set_trace()
#     def __init__(self,p=0.8,v=0.1):
#         self.p,self.v=p,v
        
#     def __call__(self,a,b,c):
#         s=(a+b+c)/2
#         result=(self.p*(self.p-a)-(self.p-b)-(self.p-c))**0.5
        
#         if random.random<=self.p:
#             return result
#         else:
#             return random.uniform(result-self.v,result+self.p)
# obj1=FuzzyTraingle()
# print(obj1())

# class Clock():
#     def __init__(self,hour=0,minute=0,second=0):
#         self.hour=hour
#         self.minute=minute
#         self.second=second
        
#     def set(self,hour,minute,second):
#         self.hour=hour
#         self.minute=minute
#         self.second=second
        
#     def tick(self):
#         if self.second==59:
#             self.second=0
#         else:
#             self.second+=1
#         if self.minute==59:
#             self.minute=0
#         else:
#             self.minute+=1
#         if self.hour==23:
#             self.hour=0
#         else:
#             self.hour+=1
            
#     def display(self):
#         print ("%d:%d:%d",(self.hour,self.minute,self.second))
#     def __str__(self):
#         return '{} {} {}'.format(self.hour, self.minute, self.second)   
# X=Clock()
# for i in range(1000):
#     X.tick()
# print(X)

# class A():
#     pass
# obj1=A()
# obj1.name="shri123"
# obj1.age="24"
# print(obj1.__dict__)
# print(obj1.__dir__)

# x=[4,5,9]
# y='hello'
# print(type(x))
# print(type(y))
# print(type(list))
# print(type(str))

# s={"first":1,"second":2,"third":3}
# s1=(1,23,4,5,5,6)
# print(type(s))
# print(type(s1))
# print(type(type(s)))
# print(type(type(s1)))

# class A():
#     pass
# x=A()
# print(type(x))

# def fun_1(n):
#     if n==0:
#         return 0
#     else:
#         return n*(n-1)
# print(fun_1(5))   

# def fun_2(n):
#     for i in range(n):
#         if n==1:
#             return 1
#         else:
#             return n*(n-1)      
# print(fun_2(5))

# def fun_3(n):
#     res=1
#     for i in range(2,n+1):
#         res=res*i
#         return res
# for i in range(5):
#     print(i,fun_3(5))
    
# def fun_4(n):
#     f1=0
#     f2=1
#     if n==0:
#         return f1
#     elif n==1:
#         return f2
#     else:
#         return (fun_4(n-1)+fun_4(n-1))
# print(fun_4(3))

# def fun_5(n):
#     old,new=0,1
#     if n==0:
#         return 0
#     for i in range(n-1):
#         old,new=new,old+new
#     print(fun_5(5))

# def fib(n):
#     """ recursive version of the Fibonacci function """
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(5))

# def fun_6(n):
#     # import pdb;pdb.set_trace()
#     if n==1:
#         return 3
#     else:
#         return fun_6(n-1)-3
# for i in range(1,10):
#     print(fun_6(i))

# from math import factorial
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(end="")
        
#     for j in range(i+1):
#         print(factorial(i)//factorial(j)*factorial(i-j),end=" ")
# print(factorial(n))

# def fun_1(n):
#     # import pdb;pdb.set_trace()
#     if n==1:
#         return 3
#     else:
#         return fun_1(n-1)+3
# for i in range(1,10):
#     print(fun_1(i))
    
# def fn_2(n):
#     if n==0:
#         return 0
#     else:
#         return n+fn_2(n-1)
# for i in range(1,10):
#     print(fn_2(i))

# cities=["berlin","new  york","america"]
# for i in cities:
#     print(type(i))
# "if list is iterable but list is not iterator"
# iter_obj=iter(cities)
# print(iter_obj)
# print(next(iter_obj))

# def iterable(obj):
#     try:
#         iter(obj)
#         return True
#     except TypeError:
#         return False
# print(iterable(34))
# print(iterable([10,20,40]))
# print(iterable((10,20,30,40)))
# print(iterable({"val_1":10,"val_2":29,"val_3":30}))
# print(iterable({1,2,4,"e434",5,45,45,4}))

# class Reverse():
#     def __init__(self,data):
#         self.data=data
#         self.index=len(data)
        
#     def __iter__(self):
#         self
#     def __next__(self):
#         if self.index==0:
#             raise StopIteration
#         self.data=self.index+3
#         return self.data[self.index]
# obj1=[10,20,330,4040] 
# class_variable=Reverse(obj1)
# for i in class_variable:
#     print(i)
    
# class Reverse:
#     """
#     Creates Iterators for looping over a sequence backwards.
#     """
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]
# lst = [34, 978, 42]
# lst_backwards = Reverse(lst)
# for el in lst_backwards:
#     print(el)
    
# citites=['paris','berlin','hamburg','frankfurt','london','viena']
# for location in cities:
#     print('location',location)    
# iter_cities=iter(cities)

# print(iter_cities)
# print(next(iter_cities))
# print(next(iter_cities))
# print(next(iter_cities))
# print(next(iter_cities))
# print(next(iter_cities))
# print(next(iter_cities))

# while iter_cities:
#     try:
#         cities_1=next(iter_cities)
#         print(cities_1)
#     except StopIteration:
#         break
    
# class Cycle():
    
#     def __init__(self,iterable):
#         self.iterable=iterable
#         self.iterable_1=iter(self.iterable)
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         while self.iterable_1:
#             try:
#                 next_obj=next(self.iterable_1)
#                 print(next_obj)
                
#             except StopIteration:
#                 break
# obj=Cycle("abc")
# for i in range(1,10):
#     print(next(obj),end="")

# def generator():
#     yield "hello"
#     yield "world"
#     yield "1"
#     yield "10"
#     yield "100"
    
# fun_1=generator()
# print(next(fun_1))
# print(next(fun_1))
# print(next(fun_1))
# print(next(fun_1))
# print(next(fun_1))
# print(next(fun_1))

# def Values(first_val=0,last_val=1):
#     x=first_val
#     while True:
#         yield x
#         x=x+first_val
#         print(x)    
# for i in range(1,10):
#     print(next(Values(i)),end=" ")
      
# def fibonacci(n):
#     a,b,counter=0,1,0
#     while True:
#         if (counter<n):
#             yield a
#             a,b=b,a+b
#             counter+=1
# f=fibonacci(5)
# for i in f:
#     print(i,end="")

# def fibonacci(n):
#     a,b=0,1
#     while True:
#         yield a,b
#         a,b=b,a+b
# f=fibonacci(5)
# counter=0
# for i in f:
#    print(i,end="")
#    counter+=1
#    if counter>10:
#        break

# def fun_1():
#     a=10
#     b=20
#     return a+b
# print(fun_1())

# sum=lambda a,b:a+b
# print(sum(3,6))

# def fun_2():
#     l=[]
#     l1=[10,20,30,40]
#     for i in l1:
#         if i%3!=0:
#             print(0)
#         else:
#             if i%2==0:
#                 l.append(i)
#                 return l
# print(fun_2())

# str_1="hello world"
# rev=lambda string:string.upper()[::-1]
# print(rev(str_1))

# li=["hello","world",1,2,3,4,5]
# rev=(lambda num:f"{num}" if isinstance(num,int) else f"{num}")
# print(rev(10))

# def fun_2(y):
#     return y*y*y
# print(fun_2(5))
# y=5
# fun_2=lambda num:(y*y*y)
# print(fun_2(6))
# print(type(fun_2))

# def addition(n):
#     return n+n
# number=(1,2,3,4,4,4)
# m=map(addition,number)
# print(list(m))

# number={1,2,3,4,5,5,6,7,7,88,99}
# l1=map(lambda num:f"{num}" if isinstance(num,int) else f"{num}",number)
# print(list(l1))

# list_1=[1,2,3,4,5,5]
# list_2=[10,20,30.40]

# a=map(lambda x,y:x+y,list_1,list_2)
# print(list(a))

# # a list contains both even and odd numbers. 
# seq = [0, 1, 2, 3, 5, 8, 13]
  
# # result contains odd numbers of the list
# result = filter(lambda x: x % 2 != 0, seq)
# print(list(result))
  
# # result contains even numbers of the list
# result = filter(lambda x: x % 2 == 0, seq)
# print(list(result))

# fibonacci=[0,1,1,2,3,5,8,13,21,34]
# odd_num=list(filter(lambda x:x%2!=0,fibonacci))
# print(odd_num)
# even_num=list(filter(lambda x:x%2==0,fibonacci))
# print(even_num)

# from functools import * 
# li=[1,2,3,4,5,5,7]
# a=lambda a,b:a if(a<b) else b
# b=reduce(a,[1,2,3,5])
# print(b)

# list_1=[10,20,30,40,50,70]
# tuple_1=(832832,2,32,323,32,32,3)
# Z=zip(list_1,tuple_1)
# print(Z)

# for i in zip(list_1,tuple_1):
#     print(i)
    
# list_1=[1,2,3,4,5,6,7,8,9,10]
# tuple_1=("hello","world","this","is")
# float_1={23.23,3243.45,656.6,67676.76}
# Z=zip(list_1,tuple_1,float_1)
# for i in Z:
#     print(i)  
    
# for i in zip():
#     print(i)
    
# # cities_and_population = [("Zurich", 415367),
# #                          ("Geneva", 201818),
# #                          ("Basel", 177654),
# #                          ("Lausanne", 139111),
# #                          ("Bern", 133883),
# #                          ("Winterthur", 111851)]

# # cities,population=zip(cities_and_population)
# # print(cities)
            
# str_1="hello world"
# dict={"value1":100,"value2":200,"value3":300}
# a=zip(str_1,dict)

# def sucee(x):
#     return x+1
# fun_1=sucee
# print(fun_1(10))

# del sucee(x):
# sucessur=sucee
# print(sucessur(10))

def F(a,b):
    
    def G(a,b):
        print("this is whole world is most beautiful")
        print(a*b)
    print("this is outer function")
    print(a+b)
    G(10,20)
F(10,20)

def temperature(t):
    def celsius(c):
        return 9 * c / 5 + 32
    print("this is temperature convert to celsius")
    print(celsius(50))
temperature(37)

def factorial(n):
    if n==0:
        return 0
    else:
        return n*factorial(n-1)
print(factorial(5)) 

def factorial_1(n):
    if type(n)==int and n>=0:
        if n==0:
            return 1
    else:
        return n-factorial_1(n-1)
print(factorial_1(5))

def g():
    print('this none parameter function')
def fun_1(name):
    print("this is name parameter",name)
g()
fun_1("hello")

def fun_1(x):
    def fun_2(y):
        return y+10
    return fun_2(20)
f1=fun_1(10)
print(f1)





    



    


            