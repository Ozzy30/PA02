def funktion():
    ERGEBNIS = 0
    for i in range(0, 1000):    
        if i%6 == 0 and i%15 == 0:  ERGEBNIS += i
    return ERGEBNIS