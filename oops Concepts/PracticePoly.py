# import math
#
#
# class circle:
#     def __init__(self,radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
#     def perimeter(self):
#         return 2 * math.pi * self.radius
#
# c1= circle(2)
# print(c1.area())
# print(c1.perimeter())

class emp:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showDetail(self):
        print(self.role,self.dept,self.salary)

class engneer(emp):
    def __init__(self, name ,age):
        self.name=name
        self.age=age
        super().__init__("Engneer","iT","80000")
e1 = emp("tech","cs" ,"1000")
e2 = engneer("rahul" ,"45")
e1.showDetail()
e2.showDetail()
