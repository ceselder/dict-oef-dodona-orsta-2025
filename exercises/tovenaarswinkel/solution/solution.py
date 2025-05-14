def bereken_totale_kost(prijzenlijst, boodschappenlijst):
    x = 0
    for boodschap in boodschappenlijst:
        x += prijzenlijst[boodschap]
    return x