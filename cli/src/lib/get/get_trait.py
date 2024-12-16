from src.lib.data.language import getText
from src.lib.data.trait import Trait


# Prompts the user for the names of the dominant and the recesive
# types of the trait and then returns the Trait object with that data
def getTrait(indent: bool = False) -> Trait:
    return Trait(
        dominant=input(f"{"  " if indent else ""}{getText("dominant_prompt")}")
        .strip()
        .lower(),
        recesive=input(f"{"  " if indent else ""}{getText("recesive_prompt")}")
        .strip()
        .lower(),
    )
