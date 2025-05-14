# Dit dictionary bevat de punten van enkele kandidaten na een proef in De Mol.
# Keys zijn namen (string), values zijn punten (integer).
# Dit dictionary is hetzelfde als in Oefening 1.
punten = {
    'Sarah': 14,
    'Els': 18,
    'Pedro': 9,
    'Lucas': 12,
    'Fien': 16,
}

def rood_of_groen(punten_dict, naam, minimum):
  """
  Controleert of de punten van een persoon onder een minimum zitten en geeft "ROOD" of "GROEN" terug.

  Args:
    punten_dict: Een dictionary met namen als keys en punten (integer) als values.
    naam: De naam (string) van de persoon wiens status je wilt controleren.
    minimum: Het minimum aantal punten (integer) om "GROEN" te zijn.

  Returns:
    "ROOD" (string) als de punten onder het minimum zijn, anders "GROEN" (string).
  """
  # 1. Zoek de punten van de persoon op in het dictionary.
  score = punten_dict[naam]

  # 2. Vergelijk de score met het minimum en bepaal of het "ROOD" of "GROEN" is.
  if score < minimum:
    return "ROOD"
  else:
    return "GROEN"


# Je kunt hieronder eventueel je functie testen,
# maar de tests in suite2.yaml zullen bepalen of de oplossing juist is.
# print(rood_of_groen(punten, 'Sarah', 15)) # Moet ROOD printen
# print(rood_of_groen(punten, 'Els', 15))   # Moet GROEN printen
# print(rood_of_groen(punten, 'Pedro', 10)) # Moet ROOD printen
# print(rood_of_groen(punten, 'Fien', 16))  # Moet GROEN printen
# print(rood_of_groen(punten, 'Lucas', 13)) # Moet ROOD printen