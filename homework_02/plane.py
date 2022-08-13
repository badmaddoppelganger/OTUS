"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homewor02.base import Vehicle
from homework_02.exceptions import CargoOverLoad


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, add_weight):
        if (self.cargo + add_weight) <= self.max_cargo:
            self.cargo += add_weight
        else:
            raise CargoOverLoad

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo
