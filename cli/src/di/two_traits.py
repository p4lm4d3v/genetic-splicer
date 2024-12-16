from src.lib.get.get_genotype import getGenotypeDi
from src.lib.data.di_genotype import DiGenotype
from src.lib.data.di_entity import DiEntity
from src.lib.get.get_trait import getTrait
from src.lib.data.language import getText
from src.lib.data.trait import Trait
from src.di.f1_phase import f1Phase
from src.di.f2_phase import f2Phase
from src.di.p_phase import pPhase
from typing import Counter, List


def twoTraits() -> None:
    # We prompt the user with the getTrait() function to get the data for out first trait
    print(getText("first_trait"))
    trait1: Trait = getTrait(indent=True)

    # We prompt the user with the getTrait() function again to get the data for out second trait
    print(getText("second_trait"))
    trait2: Trait = getTrait(indent=True)

    # We prompt the user with the correct prompts using the getGenotype() function
    # The output of the getGenotype() functions we turn into the Genotype objects
    # With the Genotype objects we make the Entity objects which represents parents
    female: DiEntity = DiEntity(
        DiGenotype.txt(
            getGenotypeDi(getText("mothers_prompt")),
        ),
    )
    male: DiEntity = DiEntity(
        DiGenotype.txt(
            getGenotypeDi(getText("fathers_prompt")),
        ),
    )

    # With the Entity.breed() function we breed the two entitys
    # The output of the function is their children and we put them inside the children list
    offspring: List[DiEntity] = male.breed(female)

    # By using the counter object we can count how many children with the same genotype there are
    # and ensure the iterator that we have doesn't have repeating elements
    counter: Counter = Counter(offspring)

    # --------------- P Phase ------------------
    pPhase(trait1, trait2, female, male)

    # -------------- F1 Phase ------------------
    f1Phase(trait1, trait2, counter, offspring)

    # -------------- F2 Phase ------------------
    # If we have only one genotype (phenotype also) in the f1 phaes
    # We can also easily calculate the f2 phase "the grandchildren"
    if len(set(offspring)) == 1:
        f2Phase(trait1, trait2, offspring)
