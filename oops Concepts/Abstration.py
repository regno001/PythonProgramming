class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluth= False
    def start(self):
        self.acc = True
        self.cluth = True
        print("Car Started")
car1 = car()
car1.start()
car2 =car()
car2.start()
