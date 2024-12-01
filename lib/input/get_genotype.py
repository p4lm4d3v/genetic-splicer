from lib.language import get_text
from main import LANGUAGE


# Prompts the user to input the genotype
# If the genotype is incorrectly inputed the program will repeat
# until the correct input is inserted
def get_genotype(prompt):
    while True:
        genotype: str = input(prompt).strip()
        if genotype in ["AA", "Aa", "aa"]:
            return genotype
        else:
            print(
                f"\n{get_text("invalid_genotype1", LANGUAGE)}\n{get_text("invalid_genotype2", LANGUAGE)}\n"
            )
