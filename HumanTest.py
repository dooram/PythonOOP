class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.iq = 1

class Auto:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.passangers = []

    def add_passanger(self, *args):
        for passenger in args:
            self.passangers.append(passenger)

    def print_passangers(self, ):
        if self.passangers == []:
            print("There're no peopole in the car")
        else:
            print("There're: ", end="")
            for passanger in self.passangers:
                print(passanger.name, end = ", ")
            print("in the car")

nazar = Human("Nazar Sigma", 61)
maksym = Human("Maksym", 1)
artem = Human("Artem", 15)

lanos = Auto("Daewoo", "Matiz", "Pink")

lanos.add_passanger(nazar, maksym, artem)
lanos.print_passangers()
