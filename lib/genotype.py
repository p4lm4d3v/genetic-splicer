from enum import Enum
from typing import List, Self

from lib.allele import Allele


# An enum the represents the genotype of an entity
class Genotype(Enum):
    AA = 1
    Aa = 2
    aa = 3

    # Creates an instance of the enum depending on the textual input
    @staticmethod
    def txt(str: str) -> Self:
        match str:
            case "AA":
                return Genotype.AA
            case "Aa":
                return Genotype.Aa
            case "aa":
                return Genotype.aa

    # Creates an instance of the enum depending on what allels are given
    @staticmethod
    def splice(a1: Allele, a2: Allele) -> Self:
        if a1 == Allele.A and a2 == Allele.A:
            return Genotype.AA
        elif a1 == Allele.a and a2 == Allele.a:
            return Genotype.aa
        else:
            return Genotype.Aa

    # Determines if the genotype represents a dominant type of a trait
    def is_dominant(self: Self) -> bool:
        match self:
            case Genotype.AA:
                return True
            case Genotype.Aa:
                return True
            case Genotype.aa:
                return False

    # Splits the genotype into two alleles
    # Depending on what allele pair it contains
    def split(self: Self) -> List[Allele]:
        match self:
            case Genotype.AA:
                return [Allele.A, Allele.A]
            case Genotype.Aa:
                return [Allele.A, Allele.a]
            case Genotype.aa:
                return [Allele.a, Allele.a]

    def __str__(self: Self) -> str:
        match self:
            case Genotype.AA:
                return "AA"
            case Genotype.Aa:
                return "Aa"
            case Genotype.aa:
                return "aa"

    def __repr__(self: Self) -> str:
        match self:
            case Genotype.AA:
                return "AA"
            case Genotype.Aa:
                return "Aa"
            case Genotype.aa:
                return "aa"
