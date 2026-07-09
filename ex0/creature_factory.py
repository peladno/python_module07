#!/usr/bin/env python3
from abc import ABC, abstractmethod
from .creature import Flameling, Torragon, Pyrodon, Aquabub, Creature


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass
    
    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        return Flameling("Flameling", "Fire")

    def create_evolved(self) -> Pyrodon:
        return Pyrodon("Pyrodon", "Fire/Flying")


class AquaFactory(CreatureFactory):
    def create_base(self) -> Aquabub:
        return Aquabub("Aquabub", "Water")

    def create_evolved(self) -> Torragon:
        return Torragon("Torragon", "Water")
