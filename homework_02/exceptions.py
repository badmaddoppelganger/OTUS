"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    # Init with def val
    def __init__(self, message="Low Fuel!"):
        super().__init__(message)


class NotEnoughFuel(Exception):
    def __init__(self, message="Not enough fuel!"):
        super().__init__(message)


class CargoOverload(Exception):
    def __init__(self, message="Cargo overload!"):
        super().__init__(message)
