from typing import List, Self

from src.lib.data.mono_genotype import MonoGenotype
from src.lib.data.allele import AlleleA


# Object that represents one individual entity (animal, human...)
class MonoEntity:
    def __init__(self: Self, genotype: MonoGenotype) -> None:
        # The genotype of the entity
        self.genotype = genotype

    # Creates an instance of the entity by creating it's genotype with the given alleles
    @staticmethod
    def fromAlleles(a1: AlleleA, a2: AlleleA) -> Self:
        return MonoEntity(MonoGenotype.fromAlleles(a1, a2))

    # Given the alleles of the two entitys determines their children and returns them
    def breed(self: Self, other: Self) -> List[Self]:
        (a1, a2) = other.genotype.toAlleles()
        (a3, a4) = self.genotype.toAlleles()

        return [
            self.fromAlleles(a1, a3),
            self.fromAlleles(a1, a4),
            self.fromAlleles(a2, a3),
            self.fromAlleles(a2, a4),
        ]

    def __eq__(self: Self, other) -> None:
        if isinstance(other, MonoEntity):
            return self.genotype == other.genotype
        return False

    def __hash__(self: Self) -> int:
        return hash(self.genotype)

    def __repr__(self: Self) -> str:
        return f"Entity({self.genotype})"


# 	    AA 	        aa
#      A  A        a  a
#    AA    Aa    Aa    aa
#   (12)  (13)  (23)  (24)
#   (01)  (02)  (12)  (13)
