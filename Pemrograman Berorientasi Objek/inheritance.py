class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age




class Student(Person):
    def __init__(self, name , age):
        super().__init__(self,name,age)
        self.graduationyear = 2019


x = Student("Mike", 19)
print(x.graduationyear)

