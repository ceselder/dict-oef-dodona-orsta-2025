# Oefening: Binair Zoeken en Sortering Controleren

Stel je voor, je hebt een heel lange lijst met getallen en je moet controleren of een specifiek getal in die lijst voorkomt. De meest eenvoudige manier is om elk getal in de lijst één voor één te bekijken tot je het vindt of de lijst op is. Dit noemen we **lineair zoeken**. Dit werkt altijd, maar het kan lang duren als de lijst erg lang is.

Als de lijst echter gesorteerd is (van klein naar groot), kunnen we veel sneller zoeken! Dit doen we met **binair zoeken**. Binair zoeken maakt gebruik van het feit dat de lijst gesorteerd is om de zoekruimte steeds te halveren.

Schrijf een Python functie genaamd `geavanceerd_zoeken(lijst, zoek_waarde)`.

- **Input:**
  - `lijst`: Een lijst met getallen (deze kan gesorteerd of ongesorteerd zijn).
  - `zoek_waarde`: Het getal dat je zoekt.
- **Output:**
  - Als de lijst **niet gesorteerd** is: geef de string `"niet gesorteerd"` terug.
  - Als de lijst **wel gesorteerd** is: voer binair zoeken uit en geef het resultaat terug in het formaat `(gevonden_waarde, aantal_stappen)`, net als bij de vorige oefeningen.

````

Als je het getal niet vind, geef dan -1 terug.

## Voorbeelden

```python
geavanceerd_zoeken([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 23)
# dit moet [23, 3] teruggeven

geavanceerd_zoeken([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 25)
# dit moet [-1, 4] teruggeven

geavanceerd_zoeken([1, 3, 2, 4, 5], 3)
# dit moet "niet gesorteerd" teruggeven

geavanceerd_zoeken([], 10)
# dit moet [-1, 0] teruggeven

geavanceerd_zoeken([42], 42)
# dit moet [42, 1] teruggeven
````
