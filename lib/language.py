from enum import Enum
from typing import Dict, Self


class Language(Enum):
    srb = 1
    eng = 2

    @staticmethod
    def txt(str: str) -> Self:
        match str:
            case "srb":
                return Language.srb
            case "eng":
                return Language.eng


def get_text(key: str, language: Language) -> str:
    return language_map[language][key]


language_map: Dict[Language, Dict[str, str]] = {
    Language.srb: {
        "choose_language_prompt": "Na kom je jeziku želite da nastavite (srb, eng): ",
        "mothers_prompt": "Genotip majke: ",
        "fathers_prompt": "Genotip oca: ",
        "dominant_prompt": "Dominantni tip: ",
        "recesive_prompt": "Recesivni tip: ",
        "invalid_genotype1": "(x) Nevažeći genotip.",
        "invalid_genotype2": "(>) Molim vas unesite jedno od sledećeg: AA, Aa, aa.",
        "p_phase": "P Faza: ",
        "f1_phase": "F1 Faza: ",
        "f2_phase": "F2 Faza: ",
        "invalid_language1": "(x) Nevažeći jezik.",
        "invalid_language2": "(x) Molim vas unesite jedno od sledećeg: srb, eng",
    },
    Language.eng: {
        "choose_language_prompt": "In what language would you like to continue (srb, eng): ",
        "mothers_prompt": "Mother's genotype: ",
        "fathers_prompt": "Father's genotype: ",
        "dominant_prompt": "Dominant type: ",
        "recesive_prompt": "Recesive type: ",
        "invalid_genotype1": "(x) Invalid genotype.",
        "invalid_genotype2": "(>) Please enter one of the following: AA, Aa, aa.",
        "p_phase": "P Phase: ",
        "f1_phase": "F1 Phase: ",
        "f2_phase": "F2 Phase: ",
        "invalid_language1": "(x) Invalid language.",
        "invalid_language2": "(x) Please enter one of the following: srb, eng.",
    },
}
