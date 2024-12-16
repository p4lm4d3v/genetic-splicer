from typing import List, Self
from itertools import product

from src.lib.data.di_genotype import DiGenotype
from src.lib.data.allele import AlleleA, AlleleB


# Object that represents one individual entity (animal, human...)
class DiEntity:
    def __init__(self: Self, genotype: DiGenotype) -> None:
        # The genotype of the entity
        self.genotype = genotype

    # Creates an instance of the entity by creating it's genotype with the given alleles
    @staticmethod
    def fromAlleles(a1: AlleleA, a2: AlleleA, b1: AlleleB, b2: AlleleB) -> Self:
        return DiEntity(DiGenotype.fromAlleles(a1, a2, b1, b2))

    @staticmethod
    def splitString(string: str) -> List[str]:
        mid: int = len(string) // 2
        left: str = string[:mid]
        right: str = string[mid:]
        return [left, right]

    @staticmethod
    def variations(alleles: List[AlleleA | AlleleB]) -> List[str]:
        (a1, a2, b1, b2) = alleles

        return set(
            [
                f"{a1}{b1}",
                f"{a1}{b2}",
                f"{a2}{b1}",
                f"{a2}{b2}",
            ]
        )

    # Given the alleles of the two entitys determines their children and returns them
    def breed(self: Self, other: Self) -> List[Self]:
        aVars: List = self.variations(self.genotype.toAlleles())
        bVars: List = self.variations(other.genotype.toAlleles())

        offspring: List[DiEntity] = []
        for a in aVars:
            for b in bVars:
                offspring.append(DiEntity(DiGenotype.txt(a + b)))

        return offspring

    def __eq__(self: Self, other) -> None:
        if isinstance(other, DiEntity):
            return self.genotype == other.genotype
        return False

    def __hash__(self: Self) -> int:
        return hash(self.genotype)

    def __str__(self: Self) -> str:
        return f"Entity({self.genotype})"

    def __repr__(self: Self) -> str:
        return self.__str__()


# 	    AA 	        aa
#      A  A        a  a
#    AA    Aa    Aa    aa
#   (12)  (13)  (23)  (24)
#   (01)  (02)  (12)  (13)
