from enum import Enum
from dataclasses import dataclass
from typing import List

class AlarmType(Enum):
    CPU = "CPU"
    MEMORY = "Memory"
    DISK = "Disk"

@dataclass
class Alarm:
    type: AlarmType
    threshold: int  # 1–100

class AlarmManager:
    def __init__(self) -> None:
        self._alarms: List[Alarm] = []

    def add_alarm(self, alarm_type: AlarmType, threshold: int) -> None:
        self._alarms.append(Alarm(alarm_type, threshold))

    def list_alarms_sorted(self) -> List[Alarm]:
        # Funktionell programmering: sorted + lambda
        return sorted(self._alarms, key=lambda a: (a.type.value, a.threshold))
