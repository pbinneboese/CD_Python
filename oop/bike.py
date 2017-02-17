# Bike Object Class Exercise
#
class Bike():
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):  # display the bike's attributes
        print "Bike costs $", self.price
        print "It can do ", self.max_speed
        print "And it has only ", self.miles, " miles on it."

    def ride(self): # up the total miles by 10
        self.miles += 10
        print "Riding, total miles =", self.miles

    def reverse(self):  # decrease the total miles by 5
        if self.miles >= 5:
            self.miles -= 5
        print "Reversing, total miles =", self.miles

Bike_A = Bike(200, "25mph")
Bike_B = Bike(400, "30mph")
Bike_C = Bike(100, "10mph")

print "Starting Bike A"
Bike_A.ride()
Bike_A.ride()
Bike_A.ride()
Bike_A.reverse()
Bike_A.displayinfo()

print "Starting Bike B"
Bike_B.ride()
Bike_B.ride()
Bike_B.reverse()
Bike_B.reverse()
Bike_B.displayinfo()

print "Starting Bike C"
Bike_C.reverse()
Bike_C.reverse()
Bike_C.reverse()
Bike_C.displayinfo()
