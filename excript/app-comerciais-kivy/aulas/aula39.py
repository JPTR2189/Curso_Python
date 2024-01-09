# FATIANDO STRINGS

s = "Para o Python toda String é imutável."

print(f"O tipo de '{s[0]}' é {type(s[0])}")
print(f"O tipo de '{s[-1]}' é {type(s[-1])}")

print("-" * 40)

print(s[5:20])
print(s[0::])

print("-" * 40)

print(s[::-1])
print(s[::3])