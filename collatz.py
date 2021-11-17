


''''
n > 0
if n % 2 == 0
    n = n/2
else
    n = 3*n + 1
'''



counter = 0

def collatz(n):

    global counter

    if n == 1:
        print("Counter", counter)
        return n

    if n % 2 == 0:
        n = n/2
        counter += 1
        print(n)
        return collatz(n)
    else:
        n = 3*n + 1
        counter += 1
        print(n)
        return collatz(n)


print(collatz(1254071358092357254901498623423423423423234234234234972394823948234987823498723948723497234987234987234987239478239487234972349782349823498234972343954238923425925987345934598734597345987345973459873459834597345987345977142))