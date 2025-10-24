from ui.menu import show_main_menu
from core.monitor import get_system_status

class AppState:
    def __init__(self) -> None:
        self.monitoring_started = False

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
            print("TODO: skapa larm")
        elif choice == 4:
            print("TODO: visa larm")
        elif choice == 5:
            print("TODO: starta övervakningsläge")

if __name__ == "__main__":
    main()
