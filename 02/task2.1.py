terme = ""
total = 0
for i in range(1, 10):
    terme = terme + "1"
    nombre = int(terme)
    total = total + nombre
print(total)

for i in range(2, 6):
    to = total ** i
    print(to)