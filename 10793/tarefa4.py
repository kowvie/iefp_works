notas = []

def adicionar_nota():
    try:
        nota = float(input("Introduza a nota do aluno (0-20): "))
        
        if 0 <= nota <= 20:
            notas.append(nota)
            print("Nota adicionada com sucesso!\n")
        else:
            print("Erro! A nota deve estar entre 0 e 20.\n")
            
    except ValueError:
        print("Erro! Deve introduzir um número válido.\n")

def listar_notas():
    if not notas:
        print("Ainda não existem notas registadas.\n")
    else:
        print("Lista de Notas:")
        for i, nota in enumerate(notas, start=1):
            print(f"{i} - {nota}")
        print()

def eliminar_nota():
    if not notas:
        print("Não existem notas para eliminar.\n")
    else:
        listar_notas()
        try:
            indice = int(input("Indique o número da nota a eliminar: "))
            
            if 1 <= indice <= len(notas):
                removida = notas.pop(indice - 1)
                print(f"Nota {removida} eliminada com sucesso!\n")
            else:
                print("Índice inválido.\n")
                
        except ValueError:
            print("Erro! Deve introduzir um número inteiro.\n")

def estatisticas():
    if not notas:
        print("Não existem notas registadas.\n")
    else:
        media = round(sum(notas) / len(notas), 2)
        maior = max(notas)
        menor = min(notas)
        
        print(f"Média da turma: {media}")
        print(f"Maior nota: {maior}")
        print(f"Menor nota: {menor}\n")

while True:
    print(" Sistema de Gestão de Notas ")
    print("1 - Adicionar Nota")
    print("2 - Listar Notas")
    print("3 - Eliminar Nota")
    print("4 - Ver Estatísticas")
    print("0 - Terminar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_nota()
    elif opcao == "2":
        listar_notas()
    elif opcao == "3":
        eliminar_nota()
    elif opcao == "4":
        estatisticas()
    elif opcao == "0":
        print("Programa terminado. Obrigado!")
        break
    else:
        print("Opção inválida!\n")