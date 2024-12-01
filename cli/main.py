from typing import Counter, List

from lib.table.gpercent_table import gpercent_table
from lib.table.ppercent_table import ppercent_table
from lib.input.get_genotype import get_genotype
from lib.language import Language, get_text
from lib.input.get_trait import get_trait
from lib.table.pg_table import pg_table
from lib.genotype import Genotype
from lib.entity import Entity
from lib.trait import Trait

# Variable that controls what language is displayed in the app
LANGUAGE: Language = Language.srb


def main():
    # We prompt the user with the message in the given language
    # Then we parse the users input into the language enum
    global LANGUAGE
    LANGUAGE = Language.txt(input(get_text("choose_language_prompt", LANGUAGE)))

    # We prompt the user with the get_trait() function to get the data for out trait
    trait: Trait = get_trait()

    # We prompt the user with the correct prompts using the get_genotype() function
    # The output of the get_genotype() functions we turn into the Genotype objects
    # With the Genotype objects we make the Entity objects which represents parents
    female: Entity = Entity(
        Genotype.txt(get_genotype(get_text("mothers_prompt", LANGUAGE)))
    )
    male: Entity = Entity(
        Genotype.txt(get_genotype(get_text("fathers_prompt", LANGUAGE)))
    )

    # With the Entity.breed() function we breed the two entitys
    # The output of the function is their children and we put them inside the children list
    children: List[Entity] = male.breed(female)
    # By using the counter object we can count how many children with the same genotype there are
    # and ensure the iterator that we have doesn't have repeating elements
    counter: Counter = Counter(children)

    # Print the p phase text
    print(f"\n{get_text("p_phase", LANGUAGE)}")
    # We print the genotypes and phenotypes of the two parents in the P phases
    print(
        f"-> {female.genotype} x {male.genotype} ({trait.pheno(female.genotype)} x {trait.pheno(male.genotype)})"
    )

    # Print the f1 phase text
    print(f"\n{get_text("f1_phase", LANGUAGE)}")
    # We print the children with different genotypes in different lines
    # n -> number of children with the same genotype
    for child, n in counter.items():
        genotype: Genotype = child.genotype
        phenotype: str = trait.pheno(child.genotype)
        print(f"-> {n}x {genotype} ({phenotype})")
    print()

    # We print the "pg", "gpercent", "ppercent" tables
    # with the pg_table(), gpercent_table() and ppercent_table() methods
    pg_table(trait, children)
    gpercent_table(trait, children)
    ppercent_table(trait, children)

    # If we have only one genotype (phenotype also) in the f1 phaes
    # We can also easily calculate the f2 phase "the grandchildren"
    if len(set(children)) == 1:
        # The new parents are the children from the f1 generation
        # This f2 phase can also be looked at as p2 phase
        male2: Entity = children[0]
        female2: Entity = children[0]
        # We again get the children by breading the parents
        children2: List[Entity] = male2.breed(female2)
        # and the same as before with the Counter object
        counter2: Counter = Counter(children2)

        # Print f2 phase
        print(f"\n{get_text("f2_phase", LANGUAGE)}")
        # We, again, print the children with different genotypes in different lines
        # But this time these are the children from the f2 phase
        for child, n in counter2.items():
            print(f"-> {n}x {child.genotype} ({trait.pheno(child.genotype)})")
        print()

        # We print the "pg", "gpercent", "ppercent" tables
        # with the pg_table(), gpercent_table() and ppercent_table() methods
        pg_table(trait, children2)
        gpercent_table(trait, children2)
        ppercent_table(trait, children2)


if __name__ == "__main__":
    main()
