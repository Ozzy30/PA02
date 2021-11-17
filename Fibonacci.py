



from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}
def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]



#print(fib3(500))


#def Aryeh(name = "Aryeh"):
#    return name

#print(Aryeh("Nicht Aryeh"))

def Sex(Joav, Ass):
    print(Joav, Ass)

Sex("Noel", "Aryeh")