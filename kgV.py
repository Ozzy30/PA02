



def kgV(a,b):
    Liste = []
    for i in range(2, max(a,b)):
        Liste.append(i)
    for i in range(2, int(max(a,b)/2)+1):
        if max(a,b)%i in Liste:
            return i+1
    for i in range(min(a,b),max(a,b)+1):
        if (max(a,b) * i)%(min(a,b)) in Liste:
            return Liste[i]


print(kgV(1232,22134))