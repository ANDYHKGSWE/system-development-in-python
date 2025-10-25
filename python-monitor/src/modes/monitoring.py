import sys
import time
import select
from core.monitor import get_system_status
from core.alarms import AlarmType

def _check_alarms(status, alarm_manager):
    msgs = []
    for a in alarm_manager.list_alarms_sorted():
        current = {
            AlarmType.CPU: status.cpu_pct,
            AlarmType.MEMORY: status.mem_pct,
            AlarmType.DISK: status.disk_pct,
        }[a.type]
        if current >= a.threshold:
            msgs.append(f"***VARNING, LARM AKTIVERAT, {a.type.value.upper()} ANVÄNDNING ÖVERSTIGER {a.threshold}%***")
    return msgs

def run_monitoring_loop(state, interval_seconds: float = 1.0):
    print("Övervakning är aktiv, tryck Enter för att återgå till menyn.")
    while True:
        status = get_system_status()
        alerts = _check_alarms(status, state.alarm_manager)
        for msg in alerts:
            print(msg)

        # Avsluta om användaren tryckt Enter
        rlist, _, _ = select.select([sys.stdin], [], [], interval_seconds)
        if rlist:
            _ = sys.stdin.readline()
            break
