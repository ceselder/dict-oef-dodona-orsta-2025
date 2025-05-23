## Links of Rechts?

Je krijgt een gesorteerde lijst, een zoekgetal (_doel_), en een index (_midden_) van een element in de lijst.

**Jouw taak**: Schrijf een functie die aangeeft of je verder moet zoeken in het **linkerdeel**, het **rechterdeel**, of dat het doel gevonden is.

```python
def zoekrichting(getallen, doel, midden):
    # jouw code hier
```

### Voorbeelden

```python
>>> zoekrichting([2, 4, 6, 8, 10, 12], 10, 2)
'rechts'  # want 6 < 10

>>> zoekrichting([2, 4, 6, 8, 10, 12], 4, 1)
'gevonden'  # want 4 == 4

>>> zoekrichting([2, 4, 6, 8, 10, 12], 2, 3)
'links'  # want 8 > 2
```

### Voorbeelden

Voeg deze tests toe onderaan je code om te checken of je functie goed werkt:

```python
zoekrichting([1, 3, 5, 7, 9], 5, 2)
# dit moet 'gevonden' retourneren

zoekrichting([1, 3, 5, 7, 9], 7, 1)
# dit moet 'rechts' retourneren

zoekrichting([1, 3, 5, 7, 9], 3, 3)
# dit moet 'links' retourneren

zoekrichting([10, 20, 30, 40, 50], 45, 3)
# dit moet 'rechts' retourneren
```
