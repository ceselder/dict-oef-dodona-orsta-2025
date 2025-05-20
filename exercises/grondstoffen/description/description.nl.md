# Grondstoffen Tellen (Lineair Zoeken: De Basis)

Welkom, jonge avonturiers! Stel je voor dat je een eenvoudig simulatiespel bouwt. Je speler legt een pad af, en bij elke stap langs dat pad kan er iets gebeuren: een grondstof vinden, een stap zetten, een vijand tegenkomen, enzovoort. Om bij te houden hoeveel van een specifieke grondstof je speler in totaal heeft verzameld, moeten we dit pad stap voor stap analyseren.

Het "pad" is voorgesteld als een **lijst** van gebeurtenissen. Elke gebeurtenis is een **paar** (een tuple) dat het _type_ gebeurtenis en een _waarde_ of _aantal_ vertegenwoordigt.

Dit is het pad dat je moet gebruiken

```python
pad_gebeurtenissen = [
    ("stap", 1),
    ("grondstof_hout", 5),
    ("stap", 1),
    ("vijand_goblin", 10),
    ("grondstof_steen", 8),
    ("stap", 1),
    ("grondstof_hout", 3),
    ("grondstof_goud", 2),
    ("stap", 1),
    ("grondstof_steen", 4),
    ("vijand_ork", 15),
    ("grondstof_hout", 7),
]
```

Om te weten hoeveel `grondstof_hout` je in totaal hebt verzameld, moet je door deze lijst heen lopen. Je kijkt naar de _eerste_ gebeurtenis, is het `grondstof_hout`? Nee? Ga verder. Ja? Tel het aantal bij je totaal op. Doe dit voor de _volgende_ gebeurtenis, en de _volgende_, net zolang tot je het einde van het pad bereikt. Je verzamelt het aantal bij **elke** gebeurtenis van het gevraagde type.

Dit proces, waarbij je elk element in een lijst na elkaar bekijkt om informatie te verzamelen, heet **Lineair Zoeken**. Hoewel je hier niet stopt bij het eerste dat je vindt (je wil een _totaal_ over meerdere items), is de fundamentele stap – elk item _lineair_ (één voor één, in volgorde) controleren. Je 'zoekt' naar alle items van een bepaald type en 'verwerkt' ze.

**De Opdracht:**

Schrijf een functie met de naam `total_resource` die twee argumenten neemt:

(zo moet je functie eruit zien)

```python
def total_resource(zoek_type):
```

1.  De lijst van pad-gebeurtenissen (zoals `pad_gebeurtenissen` hierboven). Dit is een lijst van paren (tuples of lijsten), waar het eerste element de _type_ gebeurtenis (string) en het tweede element de bijbehorende _waarde_ of _aantal_ (integer) is.
2.  Het type grondstof of gebeurtenis waarnaar je zoekt en waarvan je het totaal wilt berekenen (een string).

De functie moet de _totale som_ teruggeven van de aantallen voor alle gebeurtenissen van dat specifieke type langs het pad.

**Belangrijk:** Gebruik _geen_ ingebouwde Python functies die dit werk automatisch voor je doen (zoals list comprehensions met `sum()` of `filter()`). Het doel is dat je zelf het pad doorloopt met een `for`-loop en handmatig de telling opbouwt.

**Voorbeeld:**

Stel dat je de lijst `pad_gebeurtenissen` van hierboven hebt.

De aanroep `total_resource("grondstof_hout")` zou `5 + 3 + 7 = 15` moeten teruggeven.
De aanroep `total_resource("grondstof_steen")` zou `8 + 4 = 12` moeten teruggeven.
