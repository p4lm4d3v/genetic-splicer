from typing import Counter, List, Set

from prettytable import PrettyTable

from lib.entity import Entity
from lib.trait import Trait


def gpercent_table(trait: Trait, children: List[Entity]) -> None:
    t: PrettyTable = PrettyTable(["Genotype", "Percent"])
    genotypes = [c.genotype for c in children]

    counter: Counter = Counter(genotypes)
    for genotype, n in counter.items():
        percentage: int = int(n / len(genotypes) * 100)
        t.add_row([genotype, f"{percentage}%"])

    print(f"{t}")
