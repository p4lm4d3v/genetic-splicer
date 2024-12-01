from typing import Counter, List, Set

from prettytable import PrettyTable

from lib.entity import Entity
from lib.trait import Trait


def ppercent_table(trait: Trait, phenos: List[Entity]) -> None:
    t: PrettyTable = PrettyTable(["Phenotype", "Percent"])
    phenotypes = [trait.pheno(c.genotype) for c in phenos]

    counter: Counter = Counter(phenotypes)
    for phenotype, n in counter.items():
        percentage: int = int(n / len(phenotypes) * 100)
        t.add_row([phenotype, f"{percentage}%"])

    print(f"{t}")
