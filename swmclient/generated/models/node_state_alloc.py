from enum import Enum


class NodeStateAlloc(str, Enum):
    BUSY = "busy"
    IDLE = "idle"
    MAINT = "maint"
    OFFLINE = "offline"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
