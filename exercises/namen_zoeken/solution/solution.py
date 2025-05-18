NAAM_GETAL_PAREN = [
    ("Sarah", 14),
    ("Jan", 22),
    ("Els", 18),
    ("Mohammed", 20),
    ("Pedro", 9),
    ("Fatima", 16),
    ("Ben", 12)
]

def hoeveel(gezochte_naam):
    for naam, getal in NAAM_GETAL_PAREN:
        if naam == gezochte_naam:
            return getal
    return 0