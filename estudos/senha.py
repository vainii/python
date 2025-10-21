import random

print("Gerador de senhas aleatórias")

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

q_letras = int(input("Quantas letras você quer na sua senha?\n"))
q_numeros = int(input("Quanto números você quer na sua senha?\n"))
q_simbolos = int(input("Quantos símbolos você quer na sua senha?\n"))

senha_lista = []

for char in range(1, q_letras + 1):
    senha_lista.append(random.choice(letras))

for char in range(1, q_numeros + 1):
    senha_lista.append(random.choice(numeros))

for char in range(1, q_simbolos + 1):
    senha_lista.append(random.choice(simbolos)) 

random.shuffle(senha_lista)

print("Sua senha é: ", "".join(senha_lista))
