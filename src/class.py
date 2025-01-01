class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, num_wheels: int):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

    def started(self, message="iyeh"):
        return f"{self.make} {self.model} Vroom Vroom {message}"


honda = Car("Honda", "Civic", 2020, 4)


print(honda.started())
