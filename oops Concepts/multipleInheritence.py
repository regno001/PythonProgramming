class A:
    varA="Welocme to class A"

class B:
    varB="Welocme to class B"

class C(A,B):
    varC="Welocme to class C"

c1=C()

print(c1.varC)
print(c1.varB)
print(c1.varA)
