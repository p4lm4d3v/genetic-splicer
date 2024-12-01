from typing import List, Set

from prettytable import PrettyTable

from lib.entity import Entity
from lib.trait import Trait


def pg_table(trait: Trait, children: List[Entity]) -> None:
    dom_gtypes: Set = set(
        [str(c.genotype) for c in children if c.genotype.is_dominant()]
    )
    rec_gtypes: Set = set(
        [str(c.genotype) for c in children if not c.genotype.is_dominant()]
    )

    dom_str: str = "/" if len(dom_gtypes) == 0 else ",".join(dom_gtypes)
    rec_str: str = "/" if len(rec_gtypes) == 0 else ",".join(rec_gtypes)

    t: PrettyTable = PrettyTable(["Phenotype", "Genotype"])
    t.add_row([trait.dominant, dom_str])
    t.add_row([trait.recesive, rec_str])
    print(f"{t}")
