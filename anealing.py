import random
import math

def jumlah(x,y):
    return ((4 - (2.1 * x ** 2) + ((x ** 4) / 3)) * x ** 2) + (x * y) + ((-4 + 4 * (y ** 2)) * (y ** 2))

def simulated():
    T = 100
    xsementara = 1.0
    ysementara = 1.0
    SolSementara = jumlah(ysementara, xsementara)
    x = xsementara + random.uniform(-1, 1)
    y = ysementara + random.uniform(-1, 1)


    Delta = 99
    print("Bismillah Hasilnya adalah :")
    while (T > 10**-228 and SolSementara > 10**-227):
        Solbaru = jumlah(x, y)
        x = x + random.uniform(-1, 0)
        y = y + random.uniform(-1, 0)
        # print(Solbaru)

        if (Solbaru < SolSementara):
            Delta = abs(SolSementara - Solbaru)
            SolSementara = Solbaru
            xsementara = x
            ysementara = y

        else:
            Delta = Solbaru - SolSementara
            if math.exp(-Delta / T) > random.uniform(0, 1):
                Delta = abs(SolSementara - Solbaru)
                SolSementara = Solbaru
                xsementara = x
                ysementara = y
            T = 0.999999 * T
        #print(SolSementara)
    return SolSementara

print(simulated())
