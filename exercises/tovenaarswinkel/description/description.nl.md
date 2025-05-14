# De Tovenaarswinkel: Boodschappenlijstje

In de magische wereld van Python run jij een kleine tovenaarswinkel. Je hebt een lijst van alle items die je verkoopt met hun bijbehorende prijzen, opgeslagen als een verzameling waarbij elk item (een string) gekoppeld is aan zijn prijs (een getal).

Elke dag komen er avonturiers met een boodschappenlijstje. Dit lijstje is gewoon een opsomming van de items die ze willen kopen. Soms staat er een item op het lijstje dat je niet verkoopt in je winkel.

**Jouw taak:**

Schrijf een Python-functie met de naam `bereken_totale_kost` die twee argumenten accepteert:

1.  `prijzenlijst`: Een verzameling die de prijzen van de items bevat. De namen van de items zijn de sleutels en de prijzen zijn de waarden.
2.  `boodschappenlijst`: Een lijst met de namen van de items die de klant wil kopen.

De functie moet de totale kostprijs berekenen van alle items op de `boodschappenlijst` op basis van de `prijzenlijst`.

**Belangrijke opmerking:** Als een item op de `boodschappenlijst` _niet_ voorkomt in de `prijzenlijst`, kost dat item 0 (het wordt misschien ergens anders gekocht of is gratis).

De functie moet de totale kostprijs als een getal (integer of float, afhankelijk van de prijzen) teruggeven.
