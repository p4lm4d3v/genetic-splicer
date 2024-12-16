from typing import Dict


def getText(key: str) -> str:
    return textMap[key]


textMap: Dict[str, str] = {
    "mothers_prompt": "Genotip majke: ",
    "fathers_prompt": "Genotip oca: ",
    "dominant_prompt": "Dominantni tip: ",
    "recesive_prompt": "Recesivni tip: ",
    "invalid_genotype": "(x) Nevažeći genotip.",
    "invalid_genotype_mono": "(>) Molim vas unesite jedno od sledećeg: 'AA', 'Aa', 'aa'.",
    "invalid_genotype_di": "(>) Molim vas unesite kombinaciju A i B grupa:\n  A: 'AA', 'Aa', 'aa'\n  B: 'BB', 'Bb', 'bb'",
    "cross_type_prompt": "Kakvo je ukrštanje: ",
    "invalid_cross_type1": "(x) Nevažeći tip ukrštanja.",
    "invalid_cross_type2": "(>) Molim vas unesite jedno od sledećeg: '1', '2', '1.', '2.', 'm', 'n', 'mono', 'di', 'monohibridno', 'dihibridno'.",
    "p_phase": "P Faza: ",
    "f1_phase": "F1 Faza: ",
    "f2_phase": "F2 Faza: ",
    "first_trait": "Prva osobina: ",
    "second_trait": "Druga osobina: ",
}
