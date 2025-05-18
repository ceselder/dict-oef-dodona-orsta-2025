## Inleiding

Bij lineair zoeken doorloop je een lijst element per element, wat efficiënt is voor kleine datasets. Voor grotere gesorteerde lijsten biedt binair zoeken echter een sneller alternatief. Bij binair zoeken vergelijk je het middelste element met de zoekwaarde, en zoek je vervolgens alleen verder in de linker- of rechterhelft van de lijst.

## Opdracht

In deze oefening werk je met een vaste, gesorteerde lijst van getal-naam paren. Deze lijst is reeds gesorteerd op getal (oplopend) en vervolgens op naam (alfabetisch) voor items met hetzelfde getal. De lijst moet je hardcoderen (direct in je code plaatsen) binnen je Python-functie.

De lijst die je functie intern moet gebruiken is:

```python
    interne_data = [
        (5, "Adam"), (6, "Thomas"), (7, "Amber"), (8, "Daan"), (9, "Pedro"),
        (10, "Mila"), (11, "Emma"), (12, "Ben"), (13, "Max"), (14, "Finn"),
        (14, "Sarah"), (15, "David"), (16, "Liam"), (17, "Ian"), (18, "Els"),
        (18, "Yara"), (19, "Bram"), (20, "Luna"), (21, "Noah"),
        (23, "Charlotte"), (24, "Olivia"), (25, "Julia"), (26, "Sam"), (27, "Elias"),
        (28, "Maria"), (29, "Sofia"), (30, "Fatima"), (31, "Roos"), (32, "Jan"),
        (33, "Omar"), (35, "Zoe"), (64, "Mohammed")
    ]
```

Schrijf een Python-functie genaamd `zoek_naam_op_getal(gezocht_getal)` die:

1.  Als input een `gezocht_getal` (integer) ontvangt.
2.  Binair zoekt in de hierboven gespecificeerde, intern gedefinieerde lijst `interne_data`.
3.  Als het `gezocht_getal` wordt gevonden als het eerste element van een tuple in de lijst, geef dan het tweede element (de naam) van die tuple terug.
4.  Als het `gezocht_getal` niet in de lijst voorkomt, geef dan de string `"Niet gevonden"` terug.

**Voorbeeld:**
Als `gezocht_getal` gelijk is aan `14`, dan moet je functie `"Finn"` teruggeven.
Als `gezocht_getal` gelijk is aan `18`, dan moet je functie `"Els"` teruggeven.
Als `gezocht_getal` gelijk is aan `30`, dan moet je functie `"Fatima"` teruggeven.
Als `gezocht_getal` gelijk is aan `40`, dan moet je functie `"Niet gevonden"` teruggeven (omdat 40 niet als getal in de lijst staat).

**Functiedefinitie:**

```python

    interne_data = [
        (5, "Adam"), (6, "Thomas"), (7, "Amber"), (8, "Daan"), (9, "Pedro"),
        (10, "Mila"), (11, "Emma"), (12, "Ben"), (13, "Max"), (14, "Finn"),
        (14, "Sarah"), (15, "David"), (16, "Liam"), (17, "Ian"), (18, "Els"),
        (18, "Yara"), (19, "Bram"), (20, "Luna"), (21, "Noah"),
        (23, "Charlotte"), (24, "Olivia"), (25, "Julia"), (26, "Sam"), (27, "Elias"),
        (28, "Maria"), (29, "Sofia"), (30, "Fatima"), (31, "Roos"), (32, "Jan"),
        (33, "Omar"), (35, "Zoe"), (64, "Mohammed")
    ]


def zoek_naam_op_getal(gezocht_getal):

    # Jouw code hier (implementeer binair zoeken)
    pass
```

Implementeer binair zoeken om efficiënt door de gesorteerde lijst te navigeren.

**Opgelet!** Implementeer geen lineair zoeken.
