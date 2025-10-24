from ui.menu import show_main_menu
from ui.input_helpers import read_menu_choice, read_percent
from core.monitor import get_system_status
from core.alarms import AlarmManager, AlarmType

class AppState:
    def __init__(self) -> None:
        self.monitoring_started = False
        self.alarm_manager = AlarmManager()

def create_alarm_flow(state: AppState):
    print("\nKonfigurera larm")
    print("1) CPU användning")
    print("2) Minnesanvändning")
    print("3) Diskanvändning")
    print("4) Tillbaka")
    choice = read_menu_choice("Välj 1-4: ", range(1, 5))
    if choice == 4:
        return
    alarm_type = {1: AlarmType.CPU, 2: AlarmType.MEMORY, 3: AlarmType.DISK}[choice]
    level = read_percent("Ställ in nivå för alarm mellan 1-100: ")
    state.alarm_manager.add_alarm(alarm_type, level)
    if alarm_type == AlarmType.CPU:
        print(f"Larm för CPU användning satt till {level}%.")
    elif alarm_type == AlarmType.MEMORY:
        print(f"Larm för Minnesanvändning satt till {level}%.")
    else:
        print(f"Larm för Diskanvändning satt till {level}%.")


def main():
    state = AppState()
    print("Välkommen till Andys systemövervakare.")
    while True:
        choice = show_main_menu()

        if choice == 1:
            # Starta övervakning (endast flagga – ingen auto-loop)
            state.monitoring_started = True
            print("Övervakning startad.")

        elif choice == 2:
            # Lista aktiv övervakning eller visa meddelande
            if not state.monitoring_started:
                print("Ingen övervakning är aktiv.")
            else:
                s = get_system_status()
                print(f"CPU Användning: {s.cpu_pct}%")
                print(f"Minnesanvändning: {s.mem_pct}% ({s.mem_used_gb} GB out of {s.mem_total_gb} GB used)")
                print(f"Diskanvändning: {s.disk_pct}% ({s.disk_used_gb} GB out of {s.disk_total_gb} GB used)")
            input("Tryck enter för att gå tillbaka till huvudmeny")
        elif choice == 3:
            create_alarm_flow(state)

        elif choice == 4:
            alarms = state.alarms.list_alarms_sorted()
            if not alarms:
                print("Inga larm konfigurerade.")
            else:
                # Exempelvis: CPU larm 70%
                for a in alarms:
                    t = "CPU" if a.type == AlarmType.CPU else ("Minnes" if a.type == AlarmType.MEMORY else "Disk")
                    print(f"{t}larm {a.threshold}%")
            input("Tryck enter för att gå tillbaka till huvudmeny")


        elif choice == 5:
            print("TODO: starta övervakningsläge")

if __name__ == "__main__":
    main()
