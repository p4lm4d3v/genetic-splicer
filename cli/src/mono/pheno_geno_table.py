from typing import List, Set

from prettytable import PrettyTable

from src.lib.data.mono_entity import MonoEntity
from src.lib.data.trait import Trait


def phenoGenoTable(trait: Trait, children: List[MonoEntity]) -> None:
    dom_gtypes: Set = set(
        [str(c.genotype) for c in children if c.genotype.isDominant()]
    )
    rec_gtypes: Set = set(
        [str(c.genotype) for c in children if not c.genotype.isDominant()]
    )

    dom_str: str = "/" if len(dom_gtypes) == 0 else ",".join(dom_gtypes)
    rec_str: str = "/" if len(rec_gtypes) == 0 else ",".join(rec_gtypes)

    t: PrettyTable = PrettyTable(["Fenotip", "Genotip"])
    t.add_row([trait.dominant, dom_str])
    t.add_row([trait.recesive, rec_str])
    print(f"{t}")
