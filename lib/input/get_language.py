from lib.language import Language, get_text
from main import LANGUAGE


# Prompts the user for the language that they want to use in the rest of the program
# If the user inputs something that is not "srb" - Serbian or "eng" - English
# The function will repeatedly ask for the correct input, the desired language
def get_language():
    while True:
        lang: str = input(get_text("choose_language_prompt", LANGUAGE)).strip().lower()
        if lang in ["srb", "eng"]:
            return Language.txt(lang)
        else:
            print(
                f"\n{get_text("invalid_language1", LANGUAGE)}\n{get_text("invalid_language2", LANGUAGE)}\n"
            )
