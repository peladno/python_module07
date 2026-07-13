#!/usr/bin/env python3

from ex1 import TransformCreatureFactory
from ex2 import AggresiveStrategy


def tournament() -> None:
    creaturessss = TransformCreatureFactory().create_base()
    test = AggresiveStrategy()
    print(test.is_valid(creaturessss))

if __name__ == "__main__":
    tournament()