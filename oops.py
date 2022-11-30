from abc import ABC


class Car:
    car_type = 'Electric car'  # Class attribute

    def __init__(self, name, color, model, fuel_capacity):
        self.__name = name
        self._color = color  # Instance attribute
        self.model = model
        self.fuel_capacity = fuel_capacity

    def __get__(self, instance, owner):
        return self.__name

    def discription(self):
        return f'The {self.__name} car is a {self.car_type}, it model is {self.model}'

    def pricing(self, price):
        return f'The car {self.car_type} cost around {price}'


class Properties(Car):

    def __init__(self, name, color, model, fuel_capacity, seat_capacity):
        super().__init__(name, color, model, fuel_capacity)
        self.seat_capacity = seat_capacity

    # def capacity(self):
    #     return f'The car {self.name} is a {self.seat_capacity}'


first_car = Car('Tesla', 'black', 'Ev-5', '200km')
print(first_car.discription())
print(first_car.pricing('40L'))
print('2', first_car._Car__name)

audi = Properties('Audi', 'black', 'a-5', '300km', '2-seater')
# print('1', audi.capacity()


class Validity(ABC):
    pass