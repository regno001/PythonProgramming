# i=0
# while (i<5):
#     print("hello")
#     i+=1

# i=1
# while i<=100:
#     print(i)
#     i+=1

# i=100
# while i>0:
#     print(i)
#     i-=1

# a =int(input('enter a number'))
# i=1
# while i<=10:
#     print(a ," * " , i, " = ",a*i)
#     i+=1

# list = [1,2,3,4,5]
# i=0
# while i<len(list):
#     print(list[i])
#     i+=1
#
tup = (1,2,3,4,5)
x=5
i=0
while i < len(tup):
    if(tup[i]==x):
        print(tup[i] ," found at index ",i)
        break
    else:
        i+=1
