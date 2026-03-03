student = {
    "Name" :"Ankita",
    "Subject": {
    "math" : "math",
    "eng" : "english"
    },
    "Age" :33,
    "School" : "America"
}

print(list(student.keys()))
print(student.values())
print(student.items())
print(student.get("Name"))
print(student.update({"city" : "Delhi"}))
print(student)