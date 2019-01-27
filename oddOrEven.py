nombre = int(input("Entrez un nombre a tester: "))
num = int(input("Entrez le diviseur: "))

#Extra 1
if nombre % num == 0:
    print (str(nombre) + " est un multiple de " + str(num))
if nombre % 2 == 0:
    print (str(nombre) + " est pair")
else:
    print (str(nombre) + " est impair")