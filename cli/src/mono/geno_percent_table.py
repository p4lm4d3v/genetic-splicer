from typing import Counter, List, Set

from prettytable import PrettyTable

from src.lib.data.mono_entity import MonoEntity
from src.lib.data.trait import Trait


def genoPercentTable(trait: Trait, children: List[MonoEntity]) -> None:
    t: PrettyTable = PrettyTable(["Genotip", "Procenat"])
    genotypes = [c.genotype for c in children]

    counter: Counter = Counter(genotypes)
    for genotype, n in counter.items():
        percentage: int = int(n / len(genotypes) * 100)
        t.add_row([genotype, f"{percentage}%"])

    print(f"{t}")
