import os
with open("practice.txt" ,"r+") as f:
    data = f.read()
newdata=   data.replace("java","python")
print(newdata)
with open("practice.txt" ,"w") as f:
    f.write(newdata)
