# Midden zoeken

Voor binair zoeken zullen we de index moeten zoeken die exact tussen 2 indexes ligt.

Maak een functie `midden` dat de index tussen de 2 meegegeven indexes teruggeeft.

```python
midden(getal1, getal2)
```

# Voorbeelden

```python
>>> midden(2, 4)
3
>>> midden(10, 20)
15
>>> midden(5, 5)
5
>>> midden(7, 1)
4
```

**opgelet!** Geef geen kommagetallen terug, dat houd natuurlijk geen steek als index!. Dan vragen we jullie om naar beneden af te ronden

Je kan afronden naar beneden alsvolgt in python

```python
import math #dit moet vanboven komen in je programma

afgerond = math.floor(3.5)
print(afgerond) # dit zal nu 3 teruggeven
```
