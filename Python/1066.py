even = 0
odd = 0
positive = 0
negative = 0

for i in range(5) :
    angka = int(input())

    if (abs(angka) % 2 == 0 and angka > 0) :
        even += 1
        positive += 1
    elif (abs(angka) % 2 == 0 and angka < 0) :
        even += 1
        negative += 1
    elif (abs(angka) % 2 != 0 and angka > 0) :
        odd += 1
        positive += 1
    elif (abs(angka) % 2 != 0 and angka < 0) :
        odd += 1
        negative += 1
    elif (angka % 2 == 0) :
        even += 1
    elif (angka % 2 != 0) :
        odd += 1

print(f"{even} valor(es) par(es)")
print(f"{odd} valor(es) impar(es)")
print(f"{positive} valor(es) positivo(s)")
print(f"{negative} valor(es) negativo(s)")