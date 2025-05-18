## Inleiding

Bij lineair zoeken doorloop je een lijst (of een andere datastructuur) element per element, van begin tot eind, totdat je het gezochte item vindt of de lijst volledig doorlopen is. Het is de meest eenvoudige zoekmethode.

## Opdracht

Je krijgt een lijst met de naam `NAAM_GETAL_PAREN`. Deze lijst bevat tuples, waarbij elke tuple bestaat uit een naam (een string) en een bijbehorend getal (een integer).

Schrijf een Python-functie genaamd `hoeveel(gezochte_naam)` die:

1.  Als input een `gezochte_naam` (string) ontvangt.
2.  Lineair zoekt in de lijst `NAAM_GETAL_PAREN`.
3.  Als de `gezochte_naam` wordt gevonden als het eerste element van een tuple in de lijst, geef dan het tweede element (het getal) van die tuple terug.
4.  Als de `gezochte_naam` niet in de lijst voorkomt, geef dan het getal `0` terug.

**Gegeven lijst:**

```python
NAAM_GETAL_PAREN = [
    ("Sarah", 14),
    ("Jan", 22),
    ("Els", 18),
    ("Mohammed", 20),
    ("Pedro", 9),
    ("Fatima", 16),
    ("Ben", 12)
]
```

**Voorbeeld:**
Als `gezochte_naam` gelijk is aan `"Sarah"`, dan moet je functie `14` teruggeven.
Als `gezochte_naam` gelijk is aan `"Pedro"`, dan moet je functie `9` teruggeven.
Als `gezochte_naam` gelijk is aan `"Lisa"`, dan moet je functie `0` teruggeven (omdat "Lisa" niet in de lijst staat).

**Functiedefinitie:**

```python
def hoeveel(gezochte_naam):
    # Jouw code hier
    pass
```

Je mag ervan uitgaan dat de lijst `NAAM_GETAL_PAREN` beschikbaar is in de scope waar je functie wordt aangeroepen (je hoeft deze dus niet als parameter mee te geven aan de functie `hoeveel`).
