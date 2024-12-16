from enum import Enum
from typing import Self


# Enum that represents a dominant or a recesive AlleleA
class AlleleA(Enum):
    A = 1
    a = 2

    @staticmethod
    def txt(s: str) -> Self:
        match s:
            case "A":
                return AlleleA.A
            case "a":
                return AlleleA.a

    def __str__(self: Self) -> str:
        match self:
            case AlleleA.A:
                return "A"
            case AlleleA.a:
                return "a"

    def __repr__(self: Self) -> str:
        return self.__str__()


# Enum that represents a dominant or a recesive AlleleA
class AlleleB(Enum):
    B = 1
    b = 2

    @staticmethod
    def txt(s: str) -> Self:
        match s:
            case "B":
                return AlleleB.B
            case "b":
                return AlleleB.b

    def __str__(self: Self) -> str:
        match self:
            case AlleleB.B:
                return "B"
            case AlleleB.b:
                return "b"

    def __repr__(self: Self) -> str:
        return self.__str__()
