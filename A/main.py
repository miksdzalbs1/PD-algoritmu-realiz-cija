# ----------------------------------------------------------------------
# A1. Divu skaitļu vidējais
# ----------------------------------------------------------------------

# Jāizrēķina divu ievadīto skaitļu vidējais. Ievada 4 un 6, bet izvadās 7.0. Atrodi un salabo kļūdu.
#
# Atrodi un salabo. Tad palaid.
# ----------------------------------------------------------------------                                                                                                Rezultātu izvadi ar tekstu "Vidēji:" pirms skaitļa.

a = int(input("Pirmais: "))
b = int(input("Otrais: "))

videjais = (a + b) / 2

print("Vidējais:", videjais)



# ----------------------------------------------------------------------
# A2. Pāra skaitļi līdz desmit
# ----------------------------------------------------------------------

# Jāizvada pāra skaitļi no 2 līdz 10, bet izvadās nepāra skaitļi. Atrodi un salabo kļūdu.
#
# Atrodi un salabo. Tad palaid.
# ----------------------------------------------------------------------                                                                                                Pēc cikla pievieno rindu, kas izvada tekstu "Beigas".

i = 2

while i <= 10:
    print(i)
    i = i + 2
