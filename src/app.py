# frecuencia fibonacci 8-21
def fz(n):
    if n > 1:
        return fz(n-1) + fz(n-2)
    return n
for i in range(8):
    print(fz(i))

fz(8)

