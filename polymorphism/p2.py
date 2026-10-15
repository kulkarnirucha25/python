class Car:
    def move(self):
        print("Car is moving")

class Boat:
    def move(self):
        print("Boat is sailing")

def start(vehicle):
    vehicle.move()

car = Car()
boat = Boat()
start(car)
start(boat)