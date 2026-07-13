from ex1.factory import HealingCreatureFactory, TransformCreatureFactory


def capacitor() -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    heal_creature = HealingCreatureFactory().create_base()
    print(heal_creature.describe())
    print(heal_creature.attack())
    print(heal_creature.heal())
    print(" evolved:")
    heal_creature_evo = HealingCreatureFactory().create_evolved()
    print(heal_creature_evo.describe())
    print(heal_creature_evo.attack())
    print(heal_creature_evo.heal())

    print("Testing Creature with transform capability")
    print(" base:")
    trans_base = TransformCreatureFactory().create_base()
    print(trans_base.describe())
    print(trans_base.attack())
    print(trans_base.transform())
    print(trans_base.attack())
    print(trans_base.revert())
    print(" evolved:")
    trans_base_evo = TransformCreatureFactory().create_evolved()
    print(trans_base_evo.describe())
    print(trans_base_evo.attack())
    print(trans_base_evo.transform())
    print(trans_base_evo.attack())
    print(trans_base_evo.revert())


if __name__ == "__main__":
    capacitor()
