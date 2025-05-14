- tab: "Vrijstelling Check (Data in Test)"
  testcases:
    # We definiëren het punten dictionary letterlijk in elke test expression.
    # Dit maakt de suite.yaml langer, maar de data staat nu hier.
    # De dictionary wordt als eerste argument doorgegeven aan de functie.

    - expression: 'rood_of_groen({"Sarah": 14, "Els": 18, "Pedro": 9, "Lucas": 12, "Fien": 16}, "Sarah", 15)'
      return: "ROOD"
    - expression: 'rood_of_groen({"Sarah": 14, "Els": 18, "Pedro": 9, "Lucas": 12, "Fien": 16}, "Pedro", 10)'
      return: "ROOD"
    - expression: 'rood_of_groen({"Sarah": 14, "Els": 18, "Pedro": 9, "Lucas": 12, "Fien": 16}, "Lucas", 13)'
      return: "ROOD"
    - expression: 'rood_of_groen({"Sarah": 14, "Els": 18, "Pedro": 9, "Lucas": 12, "Fien": 16}, "Els", 19)' # Els heeft 18, 18 < 19 is ROOD
      return: "ROOD"
    - expression: 'rood_of_groen({"Sarah": 14, "Els": 18, "Pedro": 9, "Lucas": 12, "Fien": 16}, "Sarah", 14)' # Gelijk aan minimum
      return: "GROEN"
    - expression: 'rood_of_groen({"Sarah": 14, "Els": 18, "Pedro": 9, "Lucas": 12, "Fien": 16}, "Sarah", 10)' # Boven minimum
      return: "GROEN"
    - expression: 'rood_of_groen({"Sarah": 14, "Els": 18, "Pedro": 9, "Lucas": 12, "Fien": 16}, "Els", 18)'   # Gelijk aan minimum
      return: "GROEN"
    - expression: 'rood_of_groen({"Sarah": 14, "Els": 18, "Pedro": 9, "Lucas": 12, "Fien": 16}, "Els", 17)'   # Boven minimum
      return: "GROEN"
    - expression: 'rood_of_groen({"Sarah": 14, "Els": 18, "Pedro": 9, "Lucas": 12, "Fien": 16}, "Pedro", 9)'   # Gelijk aan minimum
      return: "GROEN"
    - expression: 'rood_of_groen({"Sarah": 14, "Els": 18, "Pedro": 9, "Lucas": 12, "Fien": 16}, "Pedro", 5)'   # Boven minimum
      return: "GROEN"
    - expression: 'rood_of_groen({"Sarah": 14, "Els": 18, "Pedro": 9, "Lucas": 12, "Fien": 16}, "Fien", 16)'   # Gelijk aan minimum
      return: "GROEN"
    - expression: 'rood_of_groen({"Sarah": 14, "Els": 18, "Pedro": 9, "Lucas": 12, "Fien": 16}, "Lucas", 12)'  # Gelijk aan minimum
      return: "GROEN"