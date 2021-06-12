# **kwargs is used to allow the many type of keyword in one function for example and kwargs is a dictonary type


def secret (**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)

secret(add=6, multiple = 55)


# using own value
def secret (sk, **kwargs):
   sk += kwargs["add"]
   sk *= kwargs["multiple"]
   print(sk)
secret(5, add=6, multiple = 55)


# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
