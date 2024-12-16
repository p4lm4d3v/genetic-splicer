from typing import Counter, List, Set

from prettytable import PrettyTable

from src.lib.data.mono_entity import MonoEntity
from src.lib.data.trait import Trait


def phenoPercentTable(trait: Trait, phenos: List[MonoEntity]) -> None:
    t: PrettyTable = PrettyTable(["Fenotip", "Procenat"])
    phenotypes = [trait.pheno(c.genotype) for c in phenos]

    counter: Counter = Counter(phenotypes)
    for phenotype, n in counter.items():
        percentage: int = int(n / len(phenotypes) * 100)
        t.add_row([phenotype, f"{percentage}%"])

    print(f"{t}")
