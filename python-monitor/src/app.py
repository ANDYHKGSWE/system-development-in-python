from ui.menu import show_main_menu

def main():
    print("Välkommen till Andys Systemövervakaren")
    while True:
      choice = show_main_menu()
      if choice == 1:
          print("Starta övervakning")
      elif choice == 2:
          print("Lista aktiv övervakning")
      elif choice == 3:
          print("skapa larm")
      elif choice == 4:
          print("visa larm")
      elif choice == 5:
          print("Starta övervakningsläge")

if __name__ == "__main__":
    main()