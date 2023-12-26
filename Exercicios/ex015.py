# Os endereços IP versão 4 são divididos em cinco classes: A, B, C, D e E. Os endereços no intervalo de 0 à 127 são classe A,
# de 128 a 191 são classe B, de 192 a 223 são classe C,  de 224 à 239 são classe D e a partir de 240 são classe E.
# Faça um algoritmo que leia o primeiro octeto, no formato decimal de um endereço IP, e informe a sua classe.

ips = {127: 'A', 191: 'B', 223: 'C', 239: 'D', 240: 'E'}

ip = input("Digite um IP: ")

while '.' not in ip or '.' in ip[0:3]:
    print("Digite um ip válido!")
    ip = input("Digite um IP: ")

indentificacao = ip[0:3]
print('-' * 30)

if 0 < int(indentificacao) < 128 :
    print(f"O IP é da classe 'A'")
        
elif 128 <= int(indentificacao) < 191 :
    print(f"O IP é da classe 'B'")
        
elif 192 <= int(indentificacao) < 223 :
    print(f"O IP é da classe 'C'")
        
elif 224 <= int(indentificacao) < 239 :
    print(f"O IP é da classe 'D'")

elif int(indentificacao) > 240 :
    print(f"O IP é da classe 'E'")

else:
    print("Endereço IP inválido! ")