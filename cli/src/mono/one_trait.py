from typing import Counter, List

from src.lib.get.get_genotype import getGenotypeMono
from src.lib.data.mono_genotype import MonoGenotype
from src.lib.data.mono_entity import MonoEntity
from src.lib.get.get_trait import getTrait
from src.lib.data.language import getText
from src.mono.f1_phase import f1Phase
from src.mono.f2_phase import f2Phase
from src.lib.data.trait import Trait
from src.mono.p_phase import pPhase


def oneTrait():
    # We prompt the user with the getTrait() function to get the data for out trait
    trait: Trait = getTrait()

    # We prompt the user with the correct prompts using the getGenotype() function
    # The output of the getGenotype() functions we turn into the Genotype objects
    # With the Genotype objects we make the Entity objects which represents parents
    female: MonoEntity = MonoEntity(
        MonoGenotype.txt(
            getGenotypeMono(
                getText("mothers_prompt"),
            ),
        ),
    )
    male: MonoEntity = MonoEntity(
        MonoGenotype.txt(
            getGenotypeMono(
                getText("fathers_prompt"),
            ),
        ),
    )

    # With the Entity.breed() function we breed the two entitys
    # The output of the function is their children and we put them inside the children list
    offspring: List[MonoEntity] = male.breed(female)

    # By using the counter object we can count how many children with the same genotype there are
    # and ensure the iterator that we have doesn't have repeating elements
    counter: Counter = Counter(offspring)

    # --------------- P Phase ------------------
    pPhase(trait, female, male)

    # -------------- F1 Phase ------------------
    f1Phase(trait, counter, offspring)

    # -------------- F2 Phase ------------------
    # If we have only one genotype (phenotype also) in the f1 phaes
    # We can also easily calculate the f2 phase "the grandchildren"
    if len(set(offspring)) == 1:
        f2Phase(trait, offspring)
