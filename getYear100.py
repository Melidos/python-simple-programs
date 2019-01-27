import datetime

year = datetime.datetime.now().year
name = input("Entrez votre nom: ")
age = int(input("Entrez maintenant votre age actuel: "))
times = int(input("Combien de fois voulez vous voir le prochain message ? "))

an100 = (year-age)+100
i = 0

while True:
    print(name + ", vous aurez 100 ans en " + str(an100))
    i+=1
    if i == times:
        break

print("Le message a ete affiche " + str(i) + " fois")
