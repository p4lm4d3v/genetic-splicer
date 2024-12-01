from typing import List, Self

from lib.genotype import Genotype
from lib.allele import Allele


# Object that represents one individual entity (animal, human)
class Entity:
    def __init__(self: Self, genotype: Genotype) -> None:
        # The genotype of the animal
        self.genotype = genotype

    # Creates an instance of the entity by creating it's genotype with the given alleles
    @staticmethod
    def alleles(a1: Allele, a2: Allele) -> Self:
        return Entity(Genotype.splice(a1, a2))

    # Given the alleles of the two entitys determines their children and returns them
    def breed(self: Self, other: Self) -> List[Self]:
        (a1, a2) = other.genotype.split()
        (a3, a4) = self.genotype.split()

        return [
            self.alleles(a1, a3),
            self.alleles(a1, a4),
            self.alleles(a2, a3),
            self.alleles(a2, a4),
        ]

    def __eq__(self: Self, other) -> None:
        if isinstance(other, Entity):
            return self.genotype == other.genotype
        return False

    def __hash__(self: Self) -> int:
        return hash(self.genotype)

    def __repr__(self: Self) -> str:
        return f"Proto('{f"{self.genotype}".replace("Genotype.", "")}')"


# 	    AA 	        aa
#      A  A        a  a
#    AA    Aa    Aa    aa
#   (12)  (13)  (23)  (24)
#   (01)  (02)  (12)  (13)
