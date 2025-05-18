## Inleiding

Bij lineair zoeken doorloop je een lijst element per element, wat efficiënt is voor kleine datasets. Voor grotere gesorteerde lijsten biedt binair zoeken echter een sneller alternatief. Bij binair zoeken vergelijk je het middelste element met de zoekwaarde, en zoek je vervolgens alleen verder in de linker- of rechterhelft van de lijst.

## Opdracht

Je krijgt een gesorteerde lijst met naam-getal paren. Elke entry is een tuple bestaande uit een naam (string) en een bijbehorend getal (integer). De lijst is gesorteerd op naam in alfabetische volgorde.

Schrijf een Python-functie genaamd `hoeveel(naam_getal_paren, gezochte_naam)` die:

1. Als input een gesorteerde lijst `naam_getal_paren` en een `gezochte_naam` (string) ontvangt.
2. Binair zoekt in de gesorteerde lijst `naam_getal_paren`.
3. Als de `gezochte_naam` wordt gevonden als het eerste element van een tuple in de lijst, geef dan het tweede element (het getal) van die tuple terug.
4. Als de `gezochte_naam` niet in de lijst voorkomt, geef dan het getal `0` terug.

**Voorbeeld van een gesorteerde lijst:**

```python
gesorteerde_lijst_op_getal = [
    ("Adam", 5),
    ("Thomas", 6),
    ("Amber", 7),
    ("Daan", 8),
    ("Pedro", 9),
    ("Mila", 10),
    ("Emma", 11),
    ("Ben", 12),
    ("Max", 13),
    ("Finn", 14),
    ("Sarah", 14),
    ("David", 15),
    ("Liam", 16),
    ("Ian", 17),
    ("Els", 18),
    ("Yara", 18),
    ("Bram", 19),
    ("Luna", 20),
    ("Noah", 21),
    ("Hannah", 22),
    ("Charlotte", 23),
    ("Olivia", 24),
    ("Julia", 25),
    ("Sam", 26),
    ("Elias", 27),
    ("Maria", 28),
    ("Sofia", 29),
    ("Fatima", 30),
    ("Roos", 31),
    ("Jan", 32),
    ("Omar", 33),
    ("Zoe", 35),
    ("Mohammed", 64)
]
```

**Voorbeeld:**
Als `gezochte_naam` gelijk is aan `"Sarah"`, dan moet je functie `14` teruggeven.
Als `gezochte_naam` gelijk is aan `"Fatima"`, dan moet je functie `30` teruggeven.
Als `gezochte_naam` gelijk is aan `"Lisa"`, dan moet je functie `0` teruggeven (omdat "Lisa" niet in de lijst staat).

**Functiedefinitie:**

```python
def hoeveel(naam_getal_paren, gezochte_naam):
    # Jouw code hier
    pass
```

Implementeer binair zoeken om efficiënt door de gesorteerde lijst te navigeren.

**Opgelet!** Implementeer geen lineair zoeken.
