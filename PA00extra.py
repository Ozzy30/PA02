#Funktion so wie in der Aufgabe beschrieben

def funktion():
    ERGEBNIS = 0
    for i in range(0, 1000):
        if i%6 == 0 and i%15 == 0:
            ERGEBNIS += i
    return ERGEBNIS

#print(funktion())

#Funktion wie ich sie besser finde

def SummeZahlenMitTeiler(n, Teiler1, Teiler2):
    Liste = []
    for i in range(0, n):
        if i%Teiler1 == 0 and i%Teiler2 == 0:
            Liste.append(i)
    Endergebnis = 0
    for i in range(0, len(Liste)):
        Endergebnis += Liste[i]
    print(Liste) 
    return(Endergebnis)

#print(SummeZahlenMitTeiler(120, 3, 4))