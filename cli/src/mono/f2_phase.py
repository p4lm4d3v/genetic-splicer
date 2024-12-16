from src.mono.geno_percent_table import genoPercentTable
from src.mono.pheno_percent_table import phenoPercentTable
from src.mono.pheno_geno_table import phenoGenoTable
from src.lib.data.language import getText
from src.lib.data.mono_entity import MonoEntity
from src.lib.data.trait import Trait

from typing import Counter, List


def f2Phase(trait: Trait, children: List[MonoEntity]) -> None:
    # The new parents are the children from the f1 generation
    # This f2 phase can also be looked at as p2 phase
    male2: MonoEntity = children[0]
    female2: MonoEntity = children[0]
    # We again get the children by breading the parents
    children2: List[MonoEntity] = male2.breed(female2)
    # and the same as before with the Counter object
    counter2: Counter = Counter(children2)

    # Print f2 phase
    print(f"\n{getText("f2_phase")}")
    # We, again, print the children with different genotypes in different lines
    # But this time these are the children from the f2 phase
    for child, n in counter2.items():
        print(f"-> {n}x {child.genotype} ({trait.pheno(child.genotype)})")
    print()

    # We print the "pg", "gpercent", "ppercent" tables
    # with the pg_table(), gpercent_table() and ppercent_table() methods
    phenoGenoTable(trait, children2)
    genoPercentTable(trait, children2)
    phenoPercentTable(trait, children2)
