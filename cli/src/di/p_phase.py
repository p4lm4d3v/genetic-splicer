from src.lib.data.language import getText
from src.lib.data.di_entity import DiEntity
from src.lib.data.trait import Trait


def pPhase(t1: Trait, t2: Trait, female: DiEntity, male: DiEntity) -> None:
    print(f"\n{getText("p_phase")}")
    # We print the genotypes and phenotypes of the two parents in the P phases
    print(f"-> {female.genotype} x {male.genotype}")
