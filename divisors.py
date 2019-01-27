nombre = int(input("Entrez un nombre: "))
divisors = []
i = 0

while True:
    i+=1
    if nombre % i == 0:
        divisors.append(i)
    if i >= (nombre - 1):
        break

print (divisors)
