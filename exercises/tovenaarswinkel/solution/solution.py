from typing import Dict, List, Union

def bereken_totale_kost(prijzenlijst: Dict[str, Union[int, float]], boodschappenlijst: List[str]) -> Union[int, float]:
    """
    Berekent de totale kostprijs van items op een boodschappenlijst
    op basis van een gegeven prijzenlijst.

    Args:
        prijzenlijst: Een dictionary met itemnamen als sleutels en prijzen als waarden.
        boodschappenlijst: Een lijst met de namen van de items die gekocht worden.

    Returns:
        De totale kostprijs van de items. Items die niet in de prijzenlijst staan, kosten 0.
    """
    totaal_kost = 0

    for item in boodschappenlijst:
        # Controleer of het item in de prijzenlijst staat
        if item in prijzenlijst:
            # Haal de prijs op en tel deze op bij de totale kost
            prijs = prijzenlijst[item]
            totaal_kost += prijs
        # Else: item staat niet in de lijst, kost 0, dus doe niets

    return totaal_kost
