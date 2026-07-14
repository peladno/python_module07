#!/usr/bin/env python3

from ex0.creature_factory import AquaFactory, CreatureFactory, FlameFactory
from ex1 import TransformCreatureFactory
from ex2 import AggresiveStrategy
from ex2.strategy import BattleStrategy, DefensiveStrategy, NormalStrategy


def single() -> None:
    flame_competitor: tuple[CreatureFactory, BattleStrategy] = (
        FlameFactory(),
        NormalStrategy(),
    )
    aqua_competitor: tuple[CreatureFactory, BattleStrategy] = (
        AquaFactory(),
        DefensiveStrategy(),
    )
    tournament_list: list[tuple[CreatureFactory, BattleStrategy]] = [
        flame_competitor,
        aqua_competitor,
    ]


def tournament() -> None:
    creature = TransformCreatureFactory().create_base()
    test = AggresiveStrategy()
    test.act(creature)


if __name__ == "__main__":
    tournament()
