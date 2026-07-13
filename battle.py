#!/usr/bin/env python3
from ex0 import CreatureFactory, FlameFactory, AquaFactory


def single(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolve = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolve.describe())
    print(evolve.attack())


def fight(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    base1 = factory1.create_base()
    print(base1.describe())
    print("vs")
    base2 = factory2.create_base()
    print(base2.describe())
    print("fight")
    print(base1.attack())
    print(base2.attack())


def battle() -> None:
    flame = FlameFactory()
    single(flame)
    print()

    aqua = AquaFactory()
    single(aqua)
    print()

    fight(flame, aqua)


if __name__ == "__main__":
    battle()
