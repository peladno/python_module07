#!/usr/bin/env python3
from ex0.creature_factory import AquaFactory, CreatureFactory, FlameFactory
from ex1 import TransformCreatureFactory, HealingCreatureFactory
from ex2.strategy import BattleStrategy, \
                            DefensiveStrategy, \
                            NormalStrategy, \
                            StrategyError


def single(fighters: list[tuple[CreatureFactory, BattleStrategy]],) -> None:
    for i in range(len(fighters)):
        for j in range(i + 1, len(fighters)):
            creature_a, strategy_a = fighters[i]
            creature_b, strategy_b = fighters[j]

            print("* Battle *")

            c_a = creature_a.create_base()
            c_b = creature_b.create_base()
            print(c_a.describe())
            print(" vs")
            print(c_b.describe())
            print(" now fight!!!!!!")


def tournament() -> None:
    print("Tournament 0 (basic)")
    fighters_list = [(FlameFactory(), NormalStrategy()),
                     (HealingCreatureFactory(), DefensiveStrategy())]
    single(fighters_list)


if __name__ == "__main__":
    tournament()
