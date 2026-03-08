class person:
    name="Anonymous"

    @classmethod
    def changeName(cls,name):
        cls.name=name

p1 = person()
p1.changeName("Rahul")
print(p1.name)
print(person.name)

