from __future__ import annotations
from typing import Type, Union
from abc import ABC, abstractmethod
import functools


@functools.total_ordering
class Currency(ABC):
    """
    1 EUR = 2 USD = 100 RUB

    1 EUR = 2 USD    ;  1 EUR = 100 RUB
    1 USD = 0.5 EUR  ;  1 USD = 50 RUB
    1 RUB = 0.02 USD ;  1 RUB = 0.01 EUR
    """

    def __init__(self, value: Union[float, int]):
        self.value = value

    @property
    @abstractmethod
    def name_valuta(self):
        pass

    @property
    @abstractmethod
    def rating(self):
        pass

    @property
    def _money_value(self) -> Union[float, int]:
        return self.value * self.rating

    def __add__(self, other):
        new_value = self.value + other.to_currency(self.__class__).value
        return self.__class__(new_value)

    def __radd__(self, other):
        new_value = self.value + other.value
        return self.__class__(new_value)

    def __lt__(self, other):
        return self._money_value < other._money_value

    def __eq__(self, other):
        return self._money_value == other._money_value

    def __str__(self):
        return f"{self.value} {self.name_valuta}"

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> Currency:
        return f'{cls(1).to_currency(other_cls)} for 1 {cls.name_valuta}'

    def to_currency(self, other_cls: Type[Currency]):
        new_currency = self._money_value / other_cls.rating
        return other_cls(new_currency)


class Euro(Currency):
    name_valuta = "EUR"
    rating = 2


class Dollar(Currency):
    name_valuta = "USD"
    rating = 1


class Rubble(Currency):
    name_valuta = "RUB"
    rating = 0.02

print(
    f"Euro.course(Rubble)   ==> {Euro.course(Rubble)}\n"
    f"Dollar.course(Rubble) ==> {Dollar.course(Rubble)}\n"
    f"Rubble.course(Euro)   ==> {Rubble.course(Euro)}\n"
    )