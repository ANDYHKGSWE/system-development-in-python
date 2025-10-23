def read_menu_choice(prompt: str, valid_choices: range) -> int:
    while True:
        raw = input(prompt).strip()
        if raw.isdigit():
          val = inte(raw)
          if val in valid_choices:
              return val
        print("Fel: skriv en siffra i gilitigt intervall.")

def read_percent(prompt: str) -> int:
    while True:
      raw = input(prompt).strip()
      if raw.isdigit():
          val = int(raw)
          if 1 <= val <= 100:
              return val
      print("Fel: skriv en siffra mellan 1 och 100.")
