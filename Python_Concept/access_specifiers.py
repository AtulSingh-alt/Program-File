class Student:
    def __init__(self,name,roll_no,age):
        self.name=name      #public instance variable
        self._roll_no=roll_no   #protected instance variable
        self.__age=age      #Private instance variable
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>35:
            print("Invalid age given..Age should be less then 35.")
        else:
            self.__age=age
#
#     def display(self):
#         print(f"Hi Myself {self.name} from Student class")
# class Branch(Student):
#     pass

s1=Student("Atul",23,45)
print(s1.get_age())
s1.set_age(28)
print(s1.get_age())
# print(s1.name)
# s1.display()
# b1=Branch("Atul",22,25)
# print(b1.name)
# print(b1._roll_no)
# print(b1.__age)