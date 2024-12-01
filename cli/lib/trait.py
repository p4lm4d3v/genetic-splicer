from typing import Self

from lib.genotype import Genotype


# Object that is used for storing the data about the trait that we are following
class Trait:
    def __init__(self: Self, dominant: str, recesive: str) -> None:
        # The name of the dominant type of the trait
        self.dominant = dominant
        # The name of the recesive type of the trait
        self.recesive = recesive

    # Function that determines the phenotype from the genotype
    def pheno(self: Self, genotype: Genotype) -> str:
        match genotype:
            case Genotype.AA:
                return self.dominant
            case Genotype.Aa:
                return self.dominant
            case Genotype.aa:
                return self.recesive
