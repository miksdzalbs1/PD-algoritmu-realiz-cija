# ----------------------------------------------------------------------
# B1. Skaitļu summa līdz n
# ----------------------------------------------------------------------

# Programmai jāsaskaita visi skaitļi no 1 līdz n un jāizvada summa. Ar n = 5 pareizā atbilde ir 15. Aizpildi vietu, kur stāv TODO.
#
# Aizpildi vietu, kur stāv TODO. Tad palaid.
# ----------------------------------------------------------------------                                                                                                Pirms cikla izvadi tekstu "Skaitisana sakas".

n = 5
summa = 0
i = 1
print("skaitīšana sākas")
while i <= n:
    summa = summa + i
    i = i + 1

print("Summa:", summa)


# ----------------------------------------------------------------------
# B2. Funkcija ar noklusējuma atlaidi
# ----------------------------------------------------------------------

# Funkcijai jāatgriež cena pēc atlaides. Noklusējuma atlaide ir 10 procenti. Aizpildi vietu, kur stāv TODO.
#
# Aizpildi vietu, kur stāv TODO. Tad palaid.
# ----------------------------------------------------------------------                                                                                                Virs funkcijas pievieno komentāru # atlaide procentos.

def ar_atlaidi(cena, atlaide=10):
  return cena * atlaide / 100
print(ar_atlaidi(200))
print(ar_atlaidi(200, 25))
