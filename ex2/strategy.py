#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import cast

from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class StrategyError(Exception):
    """Raised when a BattleStrategy is applied to an invalid creature."""
    pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack)


class AggresiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError(
             f"AggressiveStrategy cannot be applied to {creature.name}:"
             " missing transform capability.")
        else:
            creature_to_transform = cast(TransformCapability, creature)
            print(f"{creature_to_transform.transform()} \n"
                  f"{creature.attack()} \n"
                  f"{creature_to_transform.revert()}")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError(
                f"DefensiveStrategy cannot be applied to {creature.name}:"
                " missing heal capability.")
        else:
            creature_to_heal = cast(HealCapability, creature)
            print(creature_to_heal.heal())
