from src.lib.data.language import getText


# Prompts the user to input the genotype
# If the genotype is incorrectly inputed the program will repeat
# until the correct input is inserted


def getGenotypeMono(prompt: str) -> str:
    while True:
        genotype: str = input(prompt).strip()
        if genotype in ["AA", "Aa", "aa"]:
            return genotype
        else:
            print(
                f"\n{getText("invalid_genotype")}\n{getText("invalid_genotype_mono")}\n"
            )


def getGenotypeDi(prompt: str) -> str:
    while True:
        genotype: str = input(prompt).strip()

        mid: int = len(genotype) // 2
        left: str = genotype[:mid]
        right: str = genotype[mid:]

        leftOk: bool = left in ["AA", "Aa", "aa"]
        rightOk: bool = right in ["BB", "Bb", "bb"]
        startsWithA: bool = genotype.lower().startswith("a")

        if leftOk and rightOk and startsWithA:
            return genotype
        else:
            print(
                f"\n{getText("invalid_genotype")}\n{getText("invalid_genotype_di")}\n"
            )
