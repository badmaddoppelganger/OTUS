"""
создайте класс `Car`, наследник `Vehicle`
"""
from homewor02.base import Vehicle
from homework02.engine import Engine


class Car(Vehicle):
    def __init__(self):
        self.engine = Engine()

    def set_engine(self, engine):
        self.engine = engine
