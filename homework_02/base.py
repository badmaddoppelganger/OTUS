from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight: float = 0, fuel: float = 0, fuel_consumption: float = 0, started=False):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        if self.fuel >=  self.fuel_consumption * distance:
            self.fuel -= self.fuel_consumption * distance
            raise NotEnoughFuel
        else:
            raise NotEnoughFuel
