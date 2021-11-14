from enum import Enum


class NodeStateAlloc(str, Enum):
    IDLE = "idle"
    STOPPED = "stopped"
    BUSY = "busy"

    def __str__(self) -> str:
        return str(self.value)
