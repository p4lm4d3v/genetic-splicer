from typing import Self

from src.lib.data.mono_genotype import MonoGenotype


# Object that is used for storing the data about the trait that we are following
class Trait:
    def __init__(self: Self, dominant: str, recesive: str) -> None:
        # The name of the dominant type of the trait
        self.dominant = dominant
        # The name of the recesive type of the trait
        self.recesive = recesive

    # Function that determines the phenotype from the genotype
    def pheno(self: Self, genotype: MonoGenotype) -> str:
        match genotype:
            case MonoGenotype.AA:
                return self.dominant
            case "AA":
                return self.dominant
            case MonoGenotype.Aa:
                return self.dominant
            case "Aa":
                return self.dominant
            case MonoGenotype.aa:
                return self.recesive
            case "aa":
                return self.recesive
