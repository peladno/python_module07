#!/usr/bin/env python3
from ex0.creature_factory import CreatureFactory
from ex1.creatures import Bloomelle, Morphagon, Shifling, Sproutling


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling("Sproutling", "Grass")

    def create_evolved(self) -> Bloomelle:
        return Bloomelle("Bloomelle", "Grass/Fairy")


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shifling:
        return Shifling("Shiftling", "Normal")

    def create_evolved(self) -> Morphagon:
        return Morphagon("Morphagon", "Normal/Dragon")
