

import random

liczba = random.randint(1, 10)

zakres = int(input("Do jakiej liczby ma być zakres: "))

for g in range(zakres):
    print("Szansa ", g + 1)
    odp = input("Jaką liczbę od 1 do 10 mam na myśli? ")

    if int(odp)  <= 0 or int(odp) > 10:
        print("Podałeś liczbe z poza zakresu")
    else:
        if liczba == int(odp):
            print("Gratulacje zgadłeś! Dostajesz nagrode!")
            break
        elif g == zakres:
            print("Myślałem o liczbie", liczba)
        else:
            print(":( Nie zgadłeś. Spróbuj jeszcze raz.")

print(" Niestety nie udało ci się, miałem na myśli liczbę ", liczba)



