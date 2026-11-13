class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

vehicles = [Car(), Boat(), Drone()]

for vehicle in vehicles:
    start_trip(vehicle)