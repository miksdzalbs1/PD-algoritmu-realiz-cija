# ----------------------------------------------------------------------
# C1. Atzīmju kopsavilkums
# ----------------------------------------------------------------------

# Kodā izveido sarakstu ar septiņām atzīmēm. Izvadi to skaitu, summu, vidējo, augstāko un zemāko. Visu kodu raksti pats.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ----------------------------------------------------------------------  
lielākais = []
mazakais = []
atzimes = [7, 8, 5, 6, 4, 9, 4]
skaits = 0
for a in atzimes:
  if skaits < len(atzimes):
    skaits = skaits + 1
def atzimes(num):
   mazakais = int(str(num)[0])
mazakais.append(a)




print("videjais ir", (sum(atzimes / len(atzimes))))
print("saraksta ir", skaits)



# ---------------------------------------------------------------------- 
# C2. Degviela un braucieni 
# ---------------------------------------------------------------------- 
 
# Tvertnē ir 50 litri degvielas. Viens brauciens patērē 7 litrus. Izvadi, cik braucienu var veikt un cik degvielas paliek pāri. Visu kodu raksti pats. 
# 
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas. 
# ----------------------------------------------------------------------  
braucieni = 0 
tvertne = 50 
while tvertne >= 7: 
  tvertne = tvertne - 7 
  braucieni = braucieni + 1 
print("pāri palika: ", tvertne) 
print("braucieni: ", braucieni)   

  



  
  







