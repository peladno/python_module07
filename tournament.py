#!/usr/bin/env python3
from ex0.creature_factory import AquaFactory, CreatureFactory, FlameFactory
from ex1 import TransformCreatureFactory, HealingCreatureFactory
from ex2.strategy import BattleStrategy, \
                            DefensiveStrategy, \
                            NormalStrategy, \
                            StrategyError, \
                            AggresiveStrategy


def single(fighters: list[tuple[CreatureFactory, BattleStrategy]],) -> None:
    print("** Tournament **")
    items = []
    for factory, strategy in fighters:
        creature = factory.create_base()
        items.append(f"({creature.name}+{strategy.__class__.__name__})")
    print(", ".join(items))
    print(f"{len(fighters)} opponets involved")
    print()

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
            try:
                print(strategy_a.act(c_a))
                print(strategy_b.act(c_b))
            except StrategyError as e:
                print("Battle error, aborting tournament:", e)
            print()


def tournament() -> None:
    print("Tournament 0 (basic)")
    fighters_list = [(FlameFactory(), NormalStrategy()),
                     (HealingCreatureFactory(), DefensiveStrategy())]
    single(fighters_list)

    print("Tournament 1 (error)")
    fighters_list2 = [(FlameFactory(), AggresiveStrategy()),
                      (HealingCreatureFactory(), DefensiveStrategy())]
    single(fighters_list2)

    print("Tournament 2 (multiple)")
    fighters_list3 = [(AquaFactory(), NormalStrategy()),
                      (HealingCreatureFactory(), DefensiveStrategy()),
                      (TransformCreatureFactory(), AggresiveStrategy())]
    single(fighters_list3)


if __name__ == "__main__":
    tournament()
