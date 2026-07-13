#!/usr/bin/end python3
from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str | None) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        self._transformed = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
