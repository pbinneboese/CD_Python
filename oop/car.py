# Car Object Class Exercise
#
class Car():
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()

    def display_all(self):  # display the Car's attributes
        stats = "Price: {} \nSpeed: {} \nFuel: {} \nMileage: {} \nTax: {}".format(self.price, self.speed, self.fuel, self.mileage, self.tax)
        # stats = "Price: ", self.price, "\nSpeed: ", self.speed, "\nFuel: ", self.fuel, "\nMileage: ", self.mileage, "\nTax: ", self.tax
        print stats

print "Car A stats"
Car_A = Car(2000, "35mph", "Full", "15mpg")
print "\nCar B stats"
Car_B = Car(2000, "5mph", "Not Full", "105mpg")
print "\nCar C stats"
Car_C = Car(2000, "15mph", "Kind of Full", "95mpg")
print "\nCar D stats"
Car_D = Car(2000, "25mph", "Full", "25mpg")
print "\nCar E stats"
Car_E = Car(2000, "45mph", "Empty", "25mpg")
print "\nCar F stats"
Car_F = Car(20000000, "35mph", "Empty", "15mpg")
