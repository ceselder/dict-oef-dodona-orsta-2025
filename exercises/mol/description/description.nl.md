# Python Oefening 2: De Mol - Rood of Groen?

Na het tellen van de punten in De Mol is het moment suprême aangebroken: de eliminatietest! Kandidaat na kandidaat hoort of hun antwoorden 'groen' zijn (ze mogen blijven) of 'rood' (ze liggen eruit). Dit hangt af van het aantal punten dat ze hebben gescoord ten opzichte van een minimum aantal punten dat nodig is om door te gaan.

**De Gegevens**

Je krijgt een dictionary genaamd `punten` dat de punten van de kandidaten bevat (namen als keys, punten als integers values).

Je krijgt ook:

- Een string, de `naam` van de kandidaat wiens status je wilt controleren.
- Een integer, het `minimum` aantal punten dat een kandidaat nodig heeft om 'groen' te zijn.

**Jouw Taak**

Schrijf een Python functie genaamd `rood_of_groen`. Deze functie moet drie argumenten accepteren:

1.  De `punten` dictionary.
2.  Een string, de `naam` van de kandidaat.
3.  Een integer, het `minimum` aantal punten.

- Als de punten **kleiner** zijn dan het minimum, dan moet de functie de string `"ROOD"` teruggeven.
- Als de punten **niet kleiner** zijn dan het minimum (dus groter dan of gelijk aan), geef dan de string `"GROEN"` terug.

Je hoeft het `punten` dictionary niet zelf te maken, en je hoeft er niet over te itereren. Focus op het opzoeken van de score en het vergelijken ervan.

**Voorbeeld:**
Als het dictionary er zo uitziet:

```python
punten = {
    'Sarah': 14,
    'Els': 18,
    'Pedro': 9
}
```

```

En het minimum is `15`:

- `rood_of_groen(punten, 'Sarah', 15)`: Sarah heeft 14 punten. 14 is kleiner dan 15. Retourneer `"ROOD"`.
- `rood_of_groen(punten, 'Els', 15)`: Els heeft 18 punten. 18 is niet kleiner dan 15. Retourneer `"GROEN"`.
- `rood_of_groen(punten, 'Pedro', 10)`: Pedro heeft 9 punten. 9 is kleiner dan 10. Retourneer `"ROOD"`.
- `rood_of_groen(punten, 'Pedro', 9)`: Pedro heeft 9 punten. 9 is niet kleiner dan 9. Retourneer `"GROEN"`.

Spannend! Wie blijft er in het spel en wie moet De Mol verlaten?
```
