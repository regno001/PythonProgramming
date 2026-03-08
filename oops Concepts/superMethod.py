class car:
    def __init__(self, type):
        self.type= type

    @staticmethod
    def start():
      print("starting")

    @staticmethod
    def stop():
        print("stopping")

class toyotaCar(car):
        def __init__(self, name,type):
            self.name = name
            super().__init__(type)
            super().start()

car1 =toyotaCar("fortuner" ,"electric ")

print(car1.type)
car1.start()