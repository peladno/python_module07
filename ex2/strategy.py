#!/usr/bin/env python3
from abc import ABC, abstractmethod

from ex0.creature import Creature
from ex1.capability import TransformCapability


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass
    
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

class NormalStrategy(BattleStrategy):
    pass
        

class AggresiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        else:
            False
        
    def act(self, creature):
        return super().act(creature)

class DefensiveStrategy:
    pass


