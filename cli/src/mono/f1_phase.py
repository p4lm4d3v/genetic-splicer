from src.mono.geno_percent_table import genoPercentTable
from src.mono.pheno_geno_table import phenoGenoTable
from src.mono.pheno_percent_table import phenoPercentTable
from src.lib.data.mono_genotype import MonoGenotype
from src.lib.data.mono_entity import MonoEntity
from src.lib.data.language import getText
from src.lib.data.trait import Trait

from typing import Counter, List


def f1Phase(trait: Trait, counter: Counter, children: List[MonoEntity]) -> None:
    print(f"\n{getText("f1_phase")}")
    # We print the children with different genotypes in different lines
    # n -> number of children with the same genotype
    for child, n in counter.items():
        genotype: MonoGenotype = child.genotype
        phenotype: str = trait.pheno(child.genotype)
        print(f"-> {n}x {genotype} ({phenotype})")
    print()

    # We print the "pg", "gpercent", "ppercent" tables
    # with the pg_table(), gpercent_table() and ppercent_table() methods
    phenoGenoTable(trait, children)
    genoPercentTable(trait, children)
    phenoPercentTable(trait, children)
