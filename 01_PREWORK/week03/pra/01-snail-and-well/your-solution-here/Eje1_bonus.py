import numpy as np 
avance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
d_pozo= 125*100
dr=0
dia=0
while dr <= d_pozo:
    if dr < d_pozo:
        for n in avance_cm:
            #print(avance_cm[n])
            dr=dr+ n
            dia = dia + 1
            print(dia)
            print(dr)
print("El caracol tarda:", dia)
print(dr)
print(max(avance_cm))
print(min(avance_cm))
print(sum(avance_cm)/len(avance_cm))
print(np.std(avance_cm))