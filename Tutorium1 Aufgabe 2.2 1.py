


'''
Zahl1 = int(input("Geben sie ihre erste Zahl an:"))
Zahl2 = int(input("Geben sie ihre zweite Zahl an:"))
print(Zahl1 + Zahl2)
'''



def A3(a, b):
    if a < 0:
        a = a * -1
    if b < 0:
        b = b * -1
    if a == 0 or b == 0:
        return False
    while b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

print(A3(23425, 25))