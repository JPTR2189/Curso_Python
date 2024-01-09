print("Ínicio")

i = 0

while i < 10:
    i += 1

    if i % 2 == 0:
        continue

# Condição else não será executado pois o programa foi parado antes de seu final
    if i > 5:
        break

    print(i)

else:
    print("else")

print("Fim")
