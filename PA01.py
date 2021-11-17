





def roots(a, b, c, d, e, f):
    prev = None     #True ist positiv und False Negativ
    wechsel = -1
    c4 = a*d
    c3 = a*e + b*d
    c2 = a*f + b*e + c*d
    c1 = b*f + c*e
    c0 = c*f
    Liste = [c4, c3, c2, c1, c0]
    Liste2 = [1]
    
    #print("c0 ist " + str(c0))
    #print(Liste)

    for i in Liste:
        if i != 0:
            Liste2.append(i)

    #print(Liste2)

    for arg in Liste2:
        if arg >= 0:
            if prev == True:
                pass
            else:
                wechsel += 1
            prev = True
        elif arg < 0:
            if prev == False:
                pass
            else:
                wechsel += 1
            prev = False

    #print(wechsel)

    if wechsel%2 == 0:
        return 'Das Polynom hat eine gerade Anzahl von positiven reellen Wurzeln.'
    elif wechsel%2 != 0:
        return 'Das Polynom hat eine ungerade Anzahl von positiven reellen Wurzeln.'


#print(roots(1,2,-3,4,-5,6))


#print(roots(1,1,-1,1,1,-1))

def roots2(a,b,c,d,e,f):
    if c*f >= 0:    return 'Das Polynom hat eine gerade Anzahl von positiven reellen Wurzeln.'
    return 'Das Polynom hat eine ungerade Anzahl von positiven reellen Wurzeln.'

print(roots2(0,0,0,0,0,0))