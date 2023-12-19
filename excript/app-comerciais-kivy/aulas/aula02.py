num_int = 5
num_dec = 7.5
val_str = "texto"

print(f"Concatenando decimal: {num_dec:.2f}")
print("Concatenando decimal: {:.2f}".format(num_dec))
print(f"Concatenando decimal: " + str(num_dec))

print("-" * 40)

print(f"Concatenando strings: {val_str}")
print("Concatenando strings: {}".format(val_str))
print(f"Concatenando strings: " + val_str)
