from abc import ABC, abstractmethod

class Property(ABC):

    @abstractmethod
    def get_number():
        pass

class Car:
    
    def plate():
        return "CA0000AA"

class CarAdapter(Property):

    _car = ...

    def get_number():
        return _car.plate()