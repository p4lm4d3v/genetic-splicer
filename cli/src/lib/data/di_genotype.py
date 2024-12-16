from enum import Enum
from typing import List, Self

from src.lib.data.allele import AlleleA
from src.lib.data.allele import AlleleB


# An enum the represents the genotype of an entity
class DiGenotype(Enum):
    AABB = 1
    AaBB = 2
    aaBB = 3
    AABb = 4
    AaBb = 5
    aaBb = 6
    AAbb = 7
    Aabb = 8
    aabb = 9

    # Creates an instance of the enum depending on the textual input
    @staticmethod
    def txt(s: str) -> Self:
        s = DiGenotype.sortAllelesStr(s)
        match s:
            case "AABB":
                return DiGenotype.AABB
            case "AaBB":
                return DiGenotype.AaBB
            case "aaBB":
                return DiGenotype.aaBB
            case "AABb":
                return DiGenotype.AABb
            case "AaBb":
                return DiGenotype.AaBb
            case "aaBb":
                return DiGenotype.aaBb
            case "AAbb":
                return DiGenotype.AAbb
            case "Aabb":
                return DiGenotype.Aabb
            case "aabb":
                return DiGenotype.aabb

    @staticmethod
    def sortAllelesStr(alleles: str) -> str:
        (a1, a2, b1, b2) = ["", "", "", ""]
        for allele in list(alleles):
            match allele:
                case "A":
                    a1 += allele
                case "a":
                    a2 += allele
                case "B":
                    b1 += allele
                case "b":
                    b2 += allele
        return a1 + a2 + b1 + b2

    @staticmethod
    def sortAlleles(
        alleles: List[AlleleA | AlleleB],
    ) -> List[AlleleA | AlleleB]:
        (a1, a2, b1, b2) = [[], [], [], []]
        for allele in alleles:
            match allele:
                case "A":
                    a1.append(allele)
                case "a":
                    a2.append(allele)
                case "B":
                    b1.append(allele)
                case "b":
                    b2.append(allele)
        return a1 + a2 + b1 + b2

    # Creates an instance of the enum depending on what allels are given
    @staticmethod
    def fromAlleles(a1: AlleleA, a2: AlleleA, b1: AlleleB, b2: AlleleB) -> Self:
        return DiGenotype.txt(DiGenotype.sortAlleles(f"{a1}{a2}{b1}{b2}"))

    # Splits the genotype into two AlleleAs
    # Depending on what AlleleA pair it contains
    def toAlleles(self: Self) -> List[AlleleA | AlleleB]:
        match self:
            case DiGenotype.AABB:
                return [AlleleA.A, AlleleA.A, AlleleB.B, AlleleB.B]
            case DiGenotype.AaBB:
                return [AlleleA.A, AlleleA.a, AlleleB.B, AlleleB.B]
            case DiGenotype.aaBB:
                return [AlleleA.a, AlleleA.a, AlleleB.B, AlleleB.B]
            case DiGenotype.AABb:
                return [AlleleA.A, AlleleA.A, AlleleB.B, AlleleB.b]
            case DiGenotype.AaBb:
                return [AlleleA.A, AlleleA.a, AlleleB.B, AlleleB.b]
            case DiGenotype.aaBb:
                return [AlleleA.a, AlleleA.a, AlleleB.B, AlleleB.b]
            case DiGenotype.AAbb:
                return [AlleleA.A, AlleleA.A, AlleleB.b, AlleleB.b]
            case DiGenotype.Aabb:
                return [AlleleA.A, AlleleA.a, AlleleB.b, AlleleB.b]
            case DiGenotype.aabb:
                return [AlleleA.a, AlleleA.a, AlleleB.b, AlleleB.b]

    def __str__(self: Self) -> str:
        match self:
            case DiGenotype.AABB:
                return "AABB"
            case DiGenotype.AaBB:
                return "AaBB"
            case DiGenotype.aaBB:
                return "aaBB"
            case DiGenotype.AABb:
                return "AABb"
            case DiGenotype.AaBb:
                return "AaBb"
            case DiGenotype.aaBb:
                return "aaBb"
            case DiGenotype.AAbb:
                return "AAbb"
            case DiGenotype.Aabb:
                return "Aabb"
            case DiGenotype.aabb:
                return "aabb"

    def __repr__(self: Self) -> str:
        return self.__str__()
