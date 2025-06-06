class Car():
    @staticmethod #does not need self parameter(parent class)
    def car_start():
        print("Car Started...")
    def car_stop():
        print("Car Stopped")

class ToyotaCar(Car): #single inheritence(child class,parent class)
    def __init__(self,brand):
        self.brand=brand

class Fortuner(ToyotaCar):
    def __init__(self,type,brand):#multi-level inheritence(child class)
        self.type=type
        super().__init__(brand)#calling value from parent class

c1=Fortuner("Diesel","Toyota")
c1.car_start()
print(c1.type)
print(c1.brand)

#______________________________________________________________________________________________________________#

class A():
    varA="Welcome to class A"

class B():
    varB="Welcome to class B"

class C(A,B):#multiple inheritance(1 child class, multiple parent classes)
    varC="Welcome to class C"

c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varC)



