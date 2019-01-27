nombre = int(input("Entrez un nombre a tester: "))
num = int(input("Entrez le diviseur: "))

#Extra 1
if nombre % 4 == 0:
    print (str(nombre) + " est un multiple de 4")
elif nombre % 2 == 0:
    print (str(nombre) + " est pair")
else:
    print (str(nombre) + " est impair")

print ("\n Extra 2 \n")

#Extra 2
if nombre % num == 0:
    print (str(nombre) + " est un multiple de " + str(num))
else:
    print (str(nombre) + " n'est pas un multiple de " + str(num))
