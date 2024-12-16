from src.lib.data.language import getText
from src.lib.data.mono_entity import MonoEntity
from src.lib.data.trait import Trait


def pPhase(trait: Trait, female: MonoEntity, male: MonoEntity) -> None:
    print(f"\n{getText("p_phase")}")
    # We print the genotypes and phenotypes of the two parents in the P phases
    print(
        f"-> {female.genotype} x {male.genotype} ({trait.pheno(female.genotype)} x {trait.pheno(male.genotype)})"
    )
