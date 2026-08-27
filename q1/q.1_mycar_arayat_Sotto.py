# Car game
class Car:
    def __init__(self,brand,model,battery=33):
        self.brand = brand
        self.model = model
        self.battery = battery
    def go(self, distance):
        s = distance / 25
        self.battery = self.battery - s
        print("You traveled",distance, "km")
        print("Your",self.brand,self.model,"has",self.battery, "wH left")
    def charge(self, wH):
        self.battery = self.battery + wH
        print("You charged",wH, "wH")
        print("Your",self.brand,self.model,"has",self.battery, "wH left")

brand = input("What is the brand of your car? ")
model = input("What is the model of your car? ")
myCar = Car(brand,model)
while myCar.battery>0:
    command = input("What do you want to do? (go, charge) ")
    if command == "go":
        distance = int(input("How far? "))
        myCar.go(distance)
    elif command == "charge":
        wH = int(input("How much? "))
        myCar.charge(wH)
    else:
        print("Invalid command")
print("Your car ran out of battery !")
