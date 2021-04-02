def add(*args):
    return sum(args)


def calculate(n, **kwargs):

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


print(add(1, 2, 3, 4, 5))

calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Nissan")
print(my_car.model)
