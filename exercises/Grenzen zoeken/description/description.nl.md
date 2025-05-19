## Grenzen Aanpassen

Wanneer we later binair zoeken volledig implementeren zullen we vaak onze "grenzen" moeten aanpassen. (de indexes die ons zoekgebied begrenzen)

We zullen later zien dat, afhankelijk van onze vergelijking we ons zoekgebied zullen moeten begrenzen naar de **bovenste helft** of de **onderste helft**

## De opdracht

Nu zullen jullie een functie moeten schrijven die 3 argumenten heeft:

- `ondergrens` (int): De huidige ondergrens van het interval.
- `bovengrens` (int): De huidige bovengrens van het interval.
- `Hoger` (bool): Een boolean waarde die aangeeft of de `gok` te laag was.

  - Indien `True`, betekent dit dat de `gok` lager was dan het te zoeken getal.
  - Indien `False`, betekent dit dat de `gok` hoger was dan het te zoeken getal.

- De functie retourneert een tuple met twee getallen: `(nieuwe_ondergrens, nieuwe_bovengrens)`.

**Werking:**

- Als hoger == True, verplaats links naar midden + 1.
- Anders verplaats rechts naar midden - 1.

**Voorbeeld:**
Gegeven de volgende aanroep:

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
