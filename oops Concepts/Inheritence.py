class car:
    @staticmethod
    def start():
        print("Starting the car")

    @staticmethod
    def stop():
        print("Car Stopped")

class toyotaCar(car):
    def __init__(self,name):
        self.name = name

class fortuner(toyotaCar):
    def __init__(self,type):
        self.type=type


car1 = toyotaCar("Fortuner")
car2 = toyotaCar("pirus")
car3 = fortuner("petrol")
print(car1.name)
car1.start()
car1.stop()

print(car2.name)
car2.start()
car2.stop()
print(car3.type)