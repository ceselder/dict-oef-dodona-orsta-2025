# Oefening: Introductie tot Binair Zoeken

Stel je voor dat je een specifiek getal moet zoeken in een heel lange lijst met getallen, bijvoorbeeld de scorelijst van alle studenten op een test. Als de lijst niet gesorteerd is, is de enige manier om het getal te vinden om elk getal in de lijst één voor één te controleren. Dit noemen we **lineair zoeken**. Voor een hele lange lijst (bijvoorbeeld 1000 getallen) kan dit best lang duren, zeker als het getal er niet in staat of helemaal op het einde staat.

Maar wat als de lijst wél gesorteerd is? Bijvoorbeeld van laag naar hoog. Dan kunnen we veel slimmer zoeken! We kunnen **binair zoeken** gebruiken. Dit is veel sneller, vooral bij grote lijsten.

**Hoe werkt binair zoeken (het idee):**

1.  Kijk naar het getal precies in het **midden** van de lijst.
2.  Is dit het getal dat je zoekt? Top, gevonden!
3.  Is het getal dat je zoekt **kleiner** dan het middelste getal? Dan weet je zeker dat het _niet_ in de rechterhelft van de lijst kan staan (want alles rechts is groter dan of gelijk aan het middelste getal). Je hoeft dus alleen nog maar verder te zoeken in de **linkerhelft**.
4.  Is het getal dat je zoekt **groter** dan het middelste getal? Dan weet je zeker dat het _niet_ in de linkerhelft van de lijst kan staan. Je hoeft dus alleen nog maar verder te zoeken in de **rechterhelft**.
5.  Herhaal dit proces (stap 1 tot en met 4) met de overgebleven helft van de lijst, totdat je het getal vindt of totdat er geen getallen meer over zijn om te controleren.

Het mooie is dat je bij elke stap de helft van de overgebleven lijst weggooit! Dit is super efficiënt.

**De Opgave:**

Jouw taak is om een functie te schrijven die binair zoeken implementeert.

Schrijf een functie met de naam `zoek_binair` die twee argumenten accepteert:

1.  `lijst`: Een **gesorteerde** lijst met getallen (integers).
2.  `zoekgetal`: Het getal (integer) dat je in de lijst zoekt.

De functie moet het volgende teruggeven:

- De **index** (positie) van het `zoekgetal` in de `lijst` als het gevonden wordt.
- `-1` als het `zoekgetal` **niet** in de lijst voorkomt.

**Voorbeelden:**

```python
# Voorbeeld 1: Getal gevonden
lijst = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
zoekgetal = 23
# zoek_binair(lijst, zoekgetal) moet 5 teruggeven (omdat 23 op index 5 staat)

# Voorbeeld 2: Getal niet gevonden
lijst = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
zoekgetal = 50
# zoek_binair(lijst, zoekgetal) moet -1 teruggeven (omdat 50 niet in de lijst staat)

# Voorbeeld 3: Getal op eerste positie
lijst = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
zoekgetal = 2
# zoek_binair(lijst, zoekgetal) moet 0 teruggeven

# Voorbeeld 4: Lege lijst
lijst = []
zoekgetal = 10
# zoek_binair(lijst, zoekgetal) moet -1 teruggeven


```
