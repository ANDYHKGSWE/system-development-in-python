def read_menu_choice(prompt: str, valid_choices: range) -> int:
    while True:
        user_input = input(prompt).strip()
        if user_input.isdigit():
            number = int(user_input)
            if number in valid_choices:
                return number
        print("Fel: skriv en siffra i giltigt intervall.")

def read_percent(prompt: str) -> int:
    while True:
        user_input = input(prompt).strip()
        if user_input.isdigit():
            number = int(user_input)
            if 1 <= number <= 100:
                return number
        print("Fel: skriv en siffra mellan 1 och 100.")
