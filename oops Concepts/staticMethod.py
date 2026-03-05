class student():
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height\

    @staticmethod
    def hello():
        print('Hello')

s1=student('John',10,20,30)
print(s1.name,s1.age,s1.height,s1.hello())