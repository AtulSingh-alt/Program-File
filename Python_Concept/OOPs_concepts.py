# class Instructor:
#    # defining the init function
#     def __init__(self,instructor_name,address):
#         self.name=instructor_name
#         self.address=address
#
# # defining the methods
#     def display(self):
#        print("Hi")
#
# instructor_1=Instructor("Atul","Noida")
# print(instructor_1.name)
# instructor_1.display()
# # instructor_2=Instructor("Sunny","NEW YORK")
# # print(instructor_2.address)


#Inheritance
#
# class Human:
#     def __init__(self):
#         self.num_eyes=2
#         self.num_nose=1
#     def eat(self):
#         print("I can eat")
#     def work(self):
#         print("I can work")
# class Male(Human):
#     def __init__(self,name):
#         super().__init__()
#         self.name=name
#     def flirt(self):
#         print("I can flirt")
#     def work(self):
#         super().work()
#         print("I can code")
#
# male_1=Male("Arjun")
# # male_1.eat()
# # male_1.work()
# # male_1.flirt()
# print(male_1.num_eyes)

# Multiple Inheritance
#
# class Human:
#     def __init__(self):
#         print("Calling func from Human")
#         self.num_eyes=2
#         self.num_nose=1
#     def eat(self):
#         print("I can eat")
#     def work(self):
#         print("I can work")
#
# class Male:
#     def __init__(self,name):
#         print("Calling func from Male")
#         self.name=name
#     def flirt(self):
#         print("I can flirt")
#     def work(self):
#         print("I can code")
#
# class Boy(Human,Male):
#     def __init__(self,name):
#         Human.__init__(self)
#         Male.__init__(self,name)
#     def sleep(self):
#         print("I can sleep")
#     def work(self):
#         print("I can test")
#
# boy_1=Boy("Atul")
# # boy_1.work()
# # print(Boy.mro())
# print(boy_1.num_nose)
#
# # multilevel inheritance
# class Human:
#     can_breath = True
#     def __init__(self,num_heart):
#         print("Calling init from Human class")
#         self.eyes=2
#         self.heart=num_heart
#     def eat(self):
#         print("I can eat")
#     def work(self):
#         print("I can work")
# class Male(Human):
#     def __init__(self,name):
#         print("Calling init from male class")
#         self.name=name
#     def sleep(self):
#         print("I can sleep whole day")
# class Boy(Male):
#     def __init__(self,heart,name,can_dance):
#         Human.__init__(self,heart)
#         Male.__init__(self,name)
#         self.know_dancing=can_dance
#     def work(self):
#         # Human.work(self)
#         super().work()
#         print("I can code")
# boy_1=Boy(2,"Atul",True)
# print(boy_1.name)
# print(boy_1.know_dancing)
# print(boy_1.can_breath)
# boy_1.work()


# # Hybrid Inheritance
# class A:
#     def display(self):
#         print("Display from A class")
# class B(A):
#     def display(self):
#         print("Display from B class")
# class C:
#     def show(self):
#         print("HI from C class")
# class D(B,C):
#     def display(self):
#         print("Display from D class")
#
# d1=D()
# d1.display()
# print(D.mro())

# Abstract Class
from abstract_class import Vehicle
class Bike(Vehicle):
    def __init__(self,n,color):
        super().__init__(n)
        self.color=color
    def start(self):
        print("Start with Kick")
class Scooty(Vehicle):
    def __init__(self,n):
        super().__init__(n)
    def start(self):
        print("self start")
class Car(Vehicle):
    def __init__(self,n,x):
        super().__init__(n)
        self.no_of_grears=6
    def start(self):
        print("start with key")
