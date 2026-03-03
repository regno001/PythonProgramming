from numpy.testing.print_coercion_tables import print_new_cast_table

student = {"Rahul" , "Amit" , "Sumit" , "Regno"}
std1= {1,2,3,4,7,8,9}
std2={2,3,4,5,6}
print(student)
student.add("Aman")
print(student)
student.remove("Rahul")
print(student)
student.pop()
print(student)
student.clear()
print(student)

std3 = std1.union(std2)
print(std3)
std4 = std1.intersection(std2)
print(std4)
std5 = std1.difference(std2)
print(std5)