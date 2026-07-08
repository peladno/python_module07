from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self) -> str:
        return f"{self} uses something"

    @abstractmethod
    def describe(self) -> str:
        return f"{self.name} is a {self.type} {type(self).__name__}"

    #  Creature: Flameling, Pyrodon, Aquabub, and Torragon.
