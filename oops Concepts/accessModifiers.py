class Account:
    def __init__(self, acc_no , acc_pass):
        self.__acc_no = acc_no
        self.__acc_pass = acc_pass
    def reset_pass(self):
        print(self.__acc_pass)
acc1 = Account("123456","abcdw")
print(acc1.reset_pass())

class person:
    __name = "Rahul"

    def __hello(self):
        print("Hello")
    def welcome(self):
        self.__hello()

p1=person()
print(p1.welcome())

