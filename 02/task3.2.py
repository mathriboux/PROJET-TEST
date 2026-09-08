nombre = 123456789 * 987654321
texte = str(nombre)

total = 0
for chiffre in texte:
    total = total + int(chiffre)

print(total)
    