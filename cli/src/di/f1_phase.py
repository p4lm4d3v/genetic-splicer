from src.lib.data.di_genotype import DiGenotype
from src.lib.data.di_entity import DiEntity
from src.lib.data.language import getText
from src.lib.data.trait import Trait

from typing import Counter, List


def f1Phase(t1: Trait, t2: Trait, counter: Counter, children: List[DiEntity]) -> None:
    print(f"\n{getText("f1_phase")}")
    # We print the children with different genotypes in different lines
    # n -> number of children with the same genotype
    for child, n in counter.items():
        genotype: DiGenotype = child.genotype
        print(f"-> {n}x {genotype}")
    print()
