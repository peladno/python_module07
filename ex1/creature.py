#!/usr/bin/env python3
from ex0.creature import Creature
from .capability import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: str | None = None) -> str:
        if target is not None:
            return f"{self.name} heals to {target}"
        else:
            return f"{self.name} heals himself for a small amount"


class Bloomelle(Creature, HealCapability):
    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: str | None = None) -> str:
        if target is not None:
            return f"{self.name} heals to {target} to 100%"
        else:
            return f"{self.name} heals himself and others for large amounts"


class Shifling(Creature, TransformCapability):
    def __init__(self, name: str, type: str):
        super().__init__(name, type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._transformed:
            return f"{self.name} performs a boosted strike!"
        else:
            return f"{self.name} attacks normally"

    def revert(self) -> str:
        if self._transformed:
            self._transformed = False
            return f"{self.name} returns to normal"
        else:
            return f"{self.name} is already normal"

    def transform(self) -> str:
        if self._transformed:
            return f"{self.name} cannot transform"
        else:
            self._transformed = True
            return f"{self.name} shifts into a sharper form!"


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, type: str):
        super().__init__(name, type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._transformed:
            return f"{self.name} unleashes a devasting morph strike!"
        else:
            return f"{self.name} attacks normally"

    def revert(self) -> str:
        if self._transformed:
            self._transformed = False
            return f"{self.name} returns to normal"
        else:
            return f"{self.name} is already normal"

    def transform(self) -> str:
        if self._transformed:
            return f"{self.name} cannot transform"
        else:
            self._transformed = True
            return f"{self.name} morphs into a dragonic battle form!"
