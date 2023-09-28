from enum import Enum


class JobState(str, Enum):
    C = "C"
    E = "E"
    F = "F"
    Q = "Q"
    R = "R"
    T = "T"
    W = "W"

    def __str__(self) -> str:
        return str(self.value)
