# Python Module 07: Advanced OOP & Design Patterns

Welcome to **Python Module 07** of the 42 Tokyo Python curriculum. This module dives into software design patterns, polymorphic creature behaviors, capability composition, and tournament combat engines.

## 🎯 Objectives

- Apply advanced Object-Oriented principles and polymorphic design.
- Implement the **Factory Pattern** for dynamic object creation.
- Understand and utilize **Composition vs. Inheritance** through capabilities.
- Implement the **Strategy Pattern** for dynamic battle and decision-making logic.
- Build coordinated simulations and tournaments using decoupled class hierarchies.

---

## 📁 Directory Structure & Exercises

| Component / Exercise              | Directory / File                                      | Description                                                                           |
| :-------------------------------- | :---------------------------------------------------- | :------------------------------------------------------------------------------------ |
| **ex0: Creature Factory**         | `ex0/` (`creature.py`, `creature_factory.py`)         | Abstract `Creature` base class and factory creation logic for various creature types. |
| **ex1: Capability & Composition** | `ex1/` (`capability.py`, `creature.py`, `factory.py`) | Decoupling abilities into reusable capabilities and dynamic creature composition.     |
| **ex2: Strategy Pattern**         | `ex2/` (`strategy.py`)                                | Implementing algorithmic strategies for choosing combat actions.                      |
| **Battle System**                 | `battle.py`                                           | Turn-based battle runner pitting creatures and strategies against one another.        |
| **Capacitor**                     | `capacitor.py`                                        | Energy, resource management, and state tracking during battles.                       |
| **Tournament**                    | `tournament.py`                                       | Full tournament simulation coordinating multiple creatures and brackets.              |

---

## 🚀 How to Run

Execute exercise scripts or run the tournament simulation:

```bash
python tournament.py
python battle.py
python ex0/creature_factory.py
```
