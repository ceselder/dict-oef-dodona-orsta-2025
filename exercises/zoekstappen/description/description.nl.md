```markdown
# Zoekstappen bij Binair Zoeken

## Opdracht

Binair zoeken is een efficiënt algoritme om een element te vinden in een **gesorteerde** lijst (een lijst die op volgorde staat, bijvoorbeeld van klein naar groot). Het algoritme werkt volgens het "verdeel en heers"-principe: het deelt de lijst steeds in tweeën en bepaalt in welke helft het gezochte element zich zou moeten bevinden (als het überhaupt in de lijst zit).

Stel je hebt een gesorteerde lijst met getallen en je zoekt een specifiek getal. Het proces gaat als volgt:

1.  Neem de volledige gesorteerde lijst.
2.  Kijk naar het **middelste getal** in de huidige (deel)lijst.
3.  **Print dit middelste getal.** Dit is de 'zoekstap' die we willen zien voor deze oefening.
4.  Vergelijk dit middelste getal met het getal dat je zoekt:
    - Als het middelste getal **gelijk** is aan het gezochte getal, dan heb je het gevonden! Het proces stopt.
    - Als het gezochte getal **kleiner** is dan het middelste getal, dan weet je dat (als het gezochte getal in de lijst voorkomt) het zich in de linkerhelft van de huidige (deel)lijst moet bevinden. Negeer de rechterhelft en ga verder met de linkerhelft.
    - Als het gezochte getal **groter** is dan het middelste getal, dan zoek je op een vergelijkbare manier verder in de rechterhelft.
5.  Herhaal stap 2 t/m 4 met de steeds kleiner wordende deellijst, totdat je het getal vindt of de (deel)lijst leeg is (wat betekent dat het getal niet in de oorspronkelijke lijst voorkwam).

Jouw taak is om een programma te schrijven dat dit binair zoekproces uitvoert. Tijdens het zoeken moet je **elke keer het middelste getal printen** dat wordt vergeleken (zoals beschreven in stap 3).

## Invoerformaat

De invoer bestaat uit twee regels:

1.  De eerste regel bevat een reeks gehele getallen, gesorteerd van klein naar groot en gescheiden door spaties. Dit is de lijst waarin gezocht moet worden.
2.  De tweede regel bevat één geheel getal: het getal dat je zoekt in de lijst.

## Uitvoerformaat

Print elk getal dat als 'middelste getal' wordt gekozen en vergeleken tijdens het binair zoekproces. Elk van deze getallen moet op een nieuwe regel worden geprint, in de volgorde waarin ze worden getest.
Als het gezochte getal niet in de lijst voorkomt, print je de geteste getallen tot het punt waarop wordt vastgesteld dat het getal niet aanwezig is (d.w.z. totdat de deellijst waar nog in gezocht zou moeten worden leeg is).

## Voorbeeld 1: Getal gevonden

**Invoer:**
```

2 5 8 12 16 23 38 56 72 91
23

```

**Uitvoer:**
```

16
56
23

```

**Uitleg bij Voorbeeld 1:**
1.  Initiële lijst: `2 5 8 12 16 23 38 56 72 91`. Het gezochte getal is `23`.
    *   Het middelste element (bijv. index `(0+9)//2 = 4`) is `16`. Print `16`.
    *   `23` is groter dan `16`, dus zoek verder in de rechterhelft: `23 38 56 72 91`.
2.  Huidige deellijst: `23 38 56 72 91` (corresponderend met indices `5` t/m `9` in de originele lijst).
    *   Het middelste element (bijv. index `(5+9)//2 = 7`) is `56`. Print `56`.
    *   `23` is kleiner dan `56`, dus zoek verder in de linkerhelft van deze deellijst: `23 38`.
3.  Huidige deellijst: `23 38` (corresponderend met indices `5` t/m `6` in de originele lijst).
    *   Het middelste element (bijv. index `(5+6)//2 = 5`) is `23`. Print `23`.
    *   `23` is gelijk aan `23`. Getal gevonden.

*(Noot: De exacte keuze van het "middelste" element bij een deellijst met een even aantal elementen kan afhangen van de implementatie, bijvoorbeeld `floor((low + high) / 2)` of `ceil((low + high) / 2)`. Een veelgebruikte methode is `mid = low + (high - low) // 2` of simpelweg `mid = (low + high) // 2` met integerdeling, wat meestal naar beneden afrondt.)*

## Voorbeeld 2: Getal niet gevonden

**Invoer:**
```

10 20 30 40 50 60 70 80 90 100
35

```

**Uitvoer:**
```

50
20
30
40

```

**Uitleg bij Voorbeeld 2:**
1.  Lijst: `10 20 30 40 50 60 70 80 90 100`, zoek `35`.
    *   Midden: `50` (index `(0+9)//2=4`). Print `50`.
    *   `35 < 50`. Zoek links: `10 20 30 40` (indices `0` t/m `3`).
2.  Deellijst: `10 20 30 40`.
    *   Midden: `20` (index `(0+3)//2=1`). Print `20`.
    *   `35 > 20`. Zoek rechts: `30 40` (indices `2` t/m `3`).
3.  Deellijst: `30 40`.
    *   Midden: `30` (index `(2+3)//2=2`). Print `30`.
    *   `35 > 30`. Zoek rechts: `40` (index `3` t/m `3`).
4.  Deellijst: `40`.
    *   Midden: `40` (index `(3+3)//2=3`). Print `40`.
    *   `35 < 40`. Zoek links. De deellijst wordt nu leeg (bijv. `high` wordt kleiner dan `low`).
5.  Getal `35` niet gevonden. De geprinte stappen zijn de getallen die tijdens de zoektocht zijn vergeleken.
```
