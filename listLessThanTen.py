list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for el in list:
    if el < 5:
        print(str(el))

#Extra 1
print ("\n EXTRA 1 \n")
#Extra 1

list5 = []
for el in list:
    if el < 5:
        list5.append(el)
print (list5)

#Extra 2
print ("\n EXTRA 2 \n")
#Extra 2

print ([el for el in list if el < 5])

#Extra 3
print ("\n EXTRA 3 \n")
#Extra 3

num = int(input("Entrez un nombre: "))

print ([el for el in list if el < num])
