"""
создайте класс `Car`, наследник `Vehicle`
"""
from homewor02.base import Vehicle
from homework02.engine import Engine


class Car(Vehicle):
    engine = Engine()

    def set_engine(self, engine):
        self.engine = engine
