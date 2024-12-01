from lib.language import get_text
from lib.trait import Trait
from main import LANGUAGE


# Prompts the user for the names of the dominant and the recesive
# types of the trait and then returns the Trait object with that data
def get_trait():
    return Trait(
        dominant=input(get_text("dominant_prompt", LANGUAGE)).strip().lower(),
        recesive=input(get_text("recesive_prompt", LANGUAGE)).strip().lower(),
    )
