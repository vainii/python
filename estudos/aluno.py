from statistics import mean

# Função para validação das notas
def validar_nota(numero):
    while True:
        try:
            nota = float(input(f"Digite a nota da {numero}: "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida, digite um número de 0 a 10!")
        except ValueError:
            print("Valor inválido, digite um número!")
            
# Validação da quantiade de alunos
while True:
    q = input("Digite a quantidade de alunos: ")
    if not q.isdigit():
        print("Valor inválido, digite um número!")
    else:
        q = int(q)
        break
    
# Validação para quantidade de avaliações
while True:
        q_notas = input("Digite a quantiade de avaliações: ")
        if not q_notas.isdigit() or int(q_notas) <= 0:
            print("Digite um valor válido!")
        else:
            q_notas = int(q_notas)
            break

lista = []

# Armazena RMs cadastrados, para evitar duplicidade
rm_cadastrados = set()
 
for aluno in range(q):
    # Validação do nome
    while True:
        nome = input("Digite o nome do aluno: ")
        if all(c.isalpha() or c == " " for c in nome) and nome.strip():
            nome = ' '.join(nome.split())
            nome = nome.title()
            break
        else:
            print("Nome inválido, digite apenas letras!")

    # Validação do RM
    while True:
        rm = input("Digite o RM do aluno: ")
        if not (rm.isdigit() and len(rm) == 6):
            print("Valor inválido, digite um RM que contenha valores númericos e 6 dígitos!")
        elif rm in rm_cadastrados:
            print("RM já cadastrado, digite outro RM!")
        else:
            rm_cadastrados.add(rm)
            break        

    # Validação das notas
    notas = []
    for i in range(1, q_notas + 1):
        notas.append(validar_nota(i))
        
    media = mean(notas)
    
    lista.append([nome, rm, media])
    
    if aluno < q - 1:
        print("\n===Próximo aluno===\n")

print("\n===Resultados===")

for n in lista:
    print(f"\nAluno: {n[0]}\nRM: {n[1]}\nMédia: {n[2]:.1f}")