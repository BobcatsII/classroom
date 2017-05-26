#!/usr/bin/python

class Car:
    speed = 0
    def drive(self, distance):
        time = distance / self.speed
        print time

car = Car()
car.speed = 60.0
car.drive(100.0)
car.drive(200.0)

