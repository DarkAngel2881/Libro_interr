import random
import time
import pandas as pd

falliti = {'Bolognese' : 0, 'Castellano': 0, 'Cucci':0, 'Ferriero':0, 'Greco A.':0, 'Greco G.':0, 'Leo':0, 'Marzo':0, 'Mazzotta':0, 'Pati':0, 'Sambuchi':0, 'Santo':0, 'Santoro':0, 'Sorgente':0, 'Taurino':0}
 
df = pd.DataFrame(falliti, index=[0])
def somma_cifre():
    for i in range(20000):
        lib_pag = str(random.randint(1, 700))
        n=0
        for i in lib_pag:
            n += int(i)
            if n>15:
                n = n-15
        try:
            df.iat[0, n-1] += 1
        except(IndexError):
            continue
    
def div_persone():
    for i in range(300000):
        lib_pag = random.randint(1, 300000)
        n = lib_pag % 15
        if n == 0:
            i = 1
        df.iat[0, n-1] += 1

div_persone()
df
