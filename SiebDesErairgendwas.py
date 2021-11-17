
import math

def isPrime(n):

    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

def Sieb(n):
    Liste = []
    for i in range(0, n + 1):
        Liste.append(i)

    Liste2 = []

    for j in range(0, n):
        if isPrime(Liste[j]) == True:
            for k in range(0, n):
                pass
        


    #print(Liste)


for i in range(0, 120):
    if isPrime(i) == True:
        print(i)    
    





