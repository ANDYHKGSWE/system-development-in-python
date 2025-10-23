def show_main_menu() -> int:
    print("\nHuvudmeny")
    print("1) Starta övervakning")
    print("2) Lista aktiv övervakning")
    print("3) skapa larm)")
    print("4) visa larm")
    print("5) Starta övervakningsläge")
    from ui.input_helpers import read_menu_choice
    return read_menu_choice("välj 1-5: ", range(1, 6))
    