from src.lib.data.di_entity import DiEntity
from src.lib.data.language import getText
from src.lib.data.trait import Trait

from typing import Counter, List


def f2Phase(t1: Trait, t2: Trait, children: List[DiEntity]) -> None:
    # The new parents are the children from the f1 generation
    # This f2 phase can also be looked at as p2 phase
    male: DiEntity = children[0]
    female: DiEntity = children[0]
    # We again get the children by breading the parents
    children2: List[DiEntity] = male.breed(female)
    # and the same as before with the Counter object
    counter2: Counter = Counter(children2)

    # Print f2 phase
    print(f"\n{getText("f2_phase")}")
    # We, again, print the children with different genotypes in different lines
    # But this time these are the children from the f2 phase
    for child, n in counter2.items():
        print(f"-> {n}x {child.genotype}")
    print()
