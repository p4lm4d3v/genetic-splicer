from src.lib.data.language import getText
from src.mono.one_trait import oneTrait
from src.di.two_traits import twoTraits


def main() -> None:
    while True:
        crossType: str = input(getText("cross_type_prompt")).strip().strip(".")
        if crossType in ["1", "mono", "m", "monohibridno"]:
            return oneTrait()
        elif crossType in ["2", "di", "d", "dihibridno"]:
            return twoTraits()
        else:
            print(
                f"\n{getText("invalid_cross_type1")}\n{getText("invalid_cross_type2")}\n"
            )


if __name__ == "__main__":
    main()
