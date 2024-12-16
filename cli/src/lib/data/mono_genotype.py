from enum import Enum
from typing import List, Self

from src.lib.data.allele import AlleleA


# An enum the represents the genotype of an entity
class MonoGenotype(Enum):
    AA = 1
    Aa = 2
    aa = 3

    # Creates an instance of the enum depending on the textual input
    @staticmethod
    def txt(s: str) -> Self:
        match s:
            case "AA":
                return MonoGenotype.AA
            case "Aa":
                return MonoGenotype.Aa
            case "aa":
                return MonoGenotype.aa

    # Creates an instance of the enum depending on what allels are given
    @staticmethod
    def fromAlleles(a1: AlleleA, a2: AlleleA) -> Self:
        return MonoGenotype.txt(f"{a1}{a2}")

    # Determines if the genotype represents a dominant type of a trait
    def isDominant(self: Self) -> bool:
        return False if self == MonoGenotype.aa else True

    # Splits the genotype into two AlleleAs
    # Depending on what AlleleA pair it contains
    def toAlleles(self: Self) -> List[AlleleA]:
        match self:
            case MonoGenotype.AA:
                return [AlleleA.A, AlleleA.A]
            case MonoGenotype.Aa:
                return [AlleleA.A, AlleleA.a]
            case MonoGenotype.aa:
                return [AlleleA.a, AlleleA.a]

    def __str__(self: Self) -> str:
        match self:
            case MonoGenotype.AA:
                return "AA"
            case MonoGenotype.Aa:
                return "Aa"
            case MonoGenotype.aa:
                return "aa"

    def __repr__(self: Self) -> str:
        return self.__str__()
