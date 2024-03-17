from random import *

listOfCars = {"BMW":{"fuel":60, "hp":350, "consumption":14},
              "Audi":{"fuel":55, "hp":250, "consumption":10},
              "Lexus":{"fuel":60, "hp":320, "consumption":12},
              "Daewoo":{"fuel":50, "hp":85, "consumption":6},
              "Toyota":{"fuel":70, "hp":200, "consumption":10}}

listOfJobs = {"Python Dev": {"sallary":70, "gladnessLess":7},
              "Teacher ITStep": {"sallary":60, "gladnessLess":5},
              "Photograph": {"sallary":50, "gladnessLess":2},
              "Video editor": {"sallary":60, "gladnessLess":3},
              "Cleaner": {"sallary":20, "gladnessLess":15}}

class Human:
    def __init__(self, name, job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

    def getHome(self):
        self.home = House()

    def getCar(self):
        self.car = Auto(listOfCars)

    def getJob(self):
        if self.car.drive():
            self.job = Work(listOfJobs)
        else:
            self.toRepair()
            return

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def cleanHome(self):
        self.home.mess = 0
        self.gladness -= 5

    def toRepair(self):
        self.car.hp = listOfCars[self.car.brand]["hp"]
        self.money -= 200

    def shopping(self, message):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def daysIndex(self, day):
        pass

    def isAlive(self):
        pass

    def live(self, day):
        pass

class Auto:
    def __init__(self, listOfCars):
        self.brand = choice(listOfCars)
        self.fuel = listOfCars[self.brand]["fuel"]
        self.hp = listOfCars[self.brand]["hp"]
        self.consumption = listOfCars[self.brand]["consumption"]

    def drive(self):
        if self.fuel >= self.consumption and self.hp > 0:
            self.fuel -= self.consumption
            self.hp -= 1
            return True
        else:
            print("The car cannot move")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Work:
    def __init__(self, listOfJobs):
        self.job = choice(listOfJobs)
        self.sallary = listOfJobs[self.job]["sallary"]
        self.gladnessLess = listOfJobs[self.job]["gladnessLess"]
