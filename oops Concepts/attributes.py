class student():
    def __init__(self,name,marks1,marks2,marks3):
        self.name = name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3

    def Avg(self):
        Avg=(self.marks1+self.marks2+self.marks3)/3
        return Avg

s1 = student('John',10,20,30)
print(s1.Avg())