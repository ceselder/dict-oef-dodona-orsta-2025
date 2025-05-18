c## Opdracht

Binair zoeken is een efficiënt algoritme om een element te vinden in een **gesorteerde** lijst (een lijst die op volgorde staat, bijvoorbeeld van klein naar groot). Het algoritme werkt volgens het "verdeel en heers"-principe: het deelt de lijst steeds in tweeën en bepaalt in welke helft het gezochte element zich zou moeten bevinden (als het überhaupt in de lijst zit).

Stel je hebt een gesorteerde lijst met getallen en je zoekt een specifiek getal. Het proces gaat als volgt:

1. Neem de volledige gesorteerde lijst.
2. Kijk naar het **middelste getal** in de huidige (deel)lijst.
3. **Voeg dit middelste getal toe aan je resultaatlijst.** Dit is de 'zoekstap' die we willen bijhouden voor deze oefening.
4. Vergelijk dit middelste getal met het getal dat je zoekt:
   - Als het middelste getal **gelijk** is aan het gezochte getal, dan heb je het gevonden! Het proces stopt.
   - Als het gezochte getal **kleiner** is dan het middelste getal, dan weet je dat (als het gezochte getal in de lijst voorkomt) het zich in de linkerhelft van de huidige (deel)lijst moet bevinden. Negeer de rechterhelft en ga verder met de linkerhelft.
   - Als het gezochte getal **groter** is dan het middelste getal, dan zoek je op een vergelijkbare manier verder in de rechterhelft.
5. Herhaal stap 2 t/m 4 met de steeds kleiner wordende deellijst, totdat je het getal vindt of de (deel)lijst leeg is (wat betekent dat het getal niet in de oorspronkelijke lijst voorkwam).

Jouw taak is om een functie te schrijven die dit binair zoekproces uitvoert. Tijdens het zoeken moet je **elke keer het middelste getal bijhouden** dat wordt vergeleken (zoals beschreven in stap 3).

## Functie

Implementeer een functie `zoekstappen(getallen, zoekgetal)` die:

- Als parameter `getallen` een gesorteerde lijst van gehele getallen ontvangt
- Als parameter `zoekgetal` het te zoeken getal ontvangt
- Een lijst teruggeeft met alle getallen die als 'middelste getal' worden gekozen tijdens het binair zoekproces, in de volgorde waarin ze worden getest

## Uitvoerformaat

De functie moet een lijst teruggeven met elk getal dat als 'middelste getal' wordt gekozen en vergeleken tijdens het binair zoekproces. Als het gezochte getal niet in de lijst voorkomt, bevat de resultaatlijst alle geteste getallen tot het punt waarop wordt vastgesteld dat het getal niet aanwezig is.

## Voorbeeld 1: Getal gevonden

```python
zoekstappen([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 23)
```

**Resultaat:**

```
[16, 56, 23]
```

**Uitleg bij Voorbeeld 1:**

1. Initiële lijst: `[2, 5, 8, 12, 16, 23, 38, 56, 72, 91]`. Het gezochte getal is `23`.
   - Het middelste element (index `(0+9)//2 = 4`) is `16`. Voeg `16` toe aan het resultaat.
   - `23` is groter dan `16`, dus zoek verder in de rechterhelft: `[23, 38, 56, 72, 91]`.
2. Huidige deellijst: `[23, 38, 56, 72, 91]` (corresponderend met indices `5` t/m `9` in de originele lijst).
   - Het middelste element (index `(5+9)//2 = 7`) is `56`. Voeg `56` toe aan het resultaat.
   - `23` is kleiner dan `56`, dus zoek verder in de linkerhelft van deze deellijst: `[23, 38]`.
3. Huidige deellijst: `[23, 38]` (corresponderend met indices `5` t/m `6` in de originele lijst).
   - Het middelste element (index `(5+6)//2 = 5`) is `23`. Voeg `23` toe aan het resultaat.
   - `23` is gelijk aan `23`. Getal gevonden.

Je mag er van uitgaan dat het getal altijd aanwezig is in de lijst.
