from abc import ABC, abstractmethod

class FunctionalDuck(ABC):
    def __init__(self, functional_duck_name):
        self.functional_duck_name = functional_duck_name

    @abstractmethod
    def take_effect(self):
        pass

    def __eq__(self, other):
        if self is other:
            return True
        if other is None or self.__class__ != other.__class__:
            return False
        return self.functional_duck_name == other.functional_duck_name

    def __hash__(self):
        return hash(self.functional_duck_name)