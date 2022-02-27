i=0
gandalf = [10, 11, 13, 30, 22, 11, 10, 23, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]
for n in range(min(len(gandalf),(len(saruman)))):
    i=i+1
    if gandalf[n] == saruman[n]:
       print("El",i,"choque los magos han empatado, Gandalf", gandalf[n],"empata con Saruman", saruman[n]) 
    elif gandalf[n] > saruman[n]:
        print("El",i,"choque lo gana Gandalf", gandalf[n], "contra",saruman[n], "gana el", gandalf[n])
    else:
        print("El",i,"choque lo gana Saruman", saruman[n], "contra",gandalf[n], "gana el",saruman[n]) 