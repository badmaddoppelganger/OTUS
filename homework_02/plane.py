"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homewor02.base import Vehicle
from homework_02 import exceptions


class Plane(Vehicle):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0, started=False, max_cargo=0):
        super().__init__(eight=0, fuel=0, fuel_consumption=0, started=False)
        self.max_cargo = max_cargo
        self.cargo = max_cargo

    def load_cargo(self, value):
        if self.cargo + value <= self.max_cargo:
            self.cargo += value
        else:
            raise exceptions.CargoOverload
