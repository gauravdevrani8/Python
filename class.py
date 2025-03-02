#class-value 
# constructors 
# default  self
#default values like name 

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print(f'{self.name} is speaking')

#     def eat(self):
#         print(f'{self.name} is eating')




# class Student:
#     def students(self, name, age):
#         self.name = name
#         self.age = age
# student1 = Student()
# student1.students('John', 25)
# print(student1.name)
# print(student1.age)




# with constructor

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student('John', 25)
print(student1.name)
print(student1.age)




