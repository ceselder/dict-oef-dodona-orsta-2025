## Grenzen Aanpassen

Wanneer we later binair zoeken gaan implementeren, zullen we vaak het zoekgebied moeten verkleinen. Dat doe je door de ondergrens of bovengrens aan te passen op basis van de uitkomst van een gok.

Bijvoorbeeld: als je gok te laag is, weet je dat het gezochte getal in de bovenste helft van het interval ligt. Is de gok te hoog, dan ligt het gezochte getal in de onderste helft.

In deze oefening gaan we precies dat simuleren: het aanpassen van de grenzen op basis van of een gok te hoog of te laag was.

## De opdracht
Nu zullen jullie een functie moeten schrijven die 3 argumenten heeft:
- `ondergrens` (int): De huidige ondergrens van het interval.
- `bovengrens` (int): De huidige bovengrens van het interval.
- `Hoger` (bool): Een boolean waarde die aangeeft of de `gok` te laag was.
  - Indien `True`, betekent dit dat de nieuwe grenzen de **onderste helft** van de originele grenzen moet zijn.
  - Indien `False`, betekent dit dat de nieuwe grenzen de **bovenste helft** van de originele grenzen moet zijn.

- De functie retourneert een tuple met twee getallen: `(nieuwe_ondergrens, nieuwe_bovengrens)`.

**Voorbeeld:**
```python
update_grenzen(0, 19, True)
# return waarde moet hier [10, 19] zijn.

update_grenzen(0, 19, False)
# return waarde moet hier [0, 10] zijn.

update_grenzen(10, 15, False)
# return waarde moet hier [10, 12] zijn.

update_grenzen(12, 15, False)
# return waarde moet hier [10, 12] zijn.
```

**Hint**: denk logisch na, schets op papier...
Je oplossing voor "midden" van de vorige oefening kan hier zeker handig zijn.

Opnieuw, geef hier geen kommagetallen terug. We zoeken naar indices...
