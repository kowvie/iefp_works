import pickle

nomes = []
notas = []

def adicionar_aluno():
    try:
        nome = input("Introduza o nome do aluno: ")
        
        if nome == "":
            print("O nome não pode estar vazio!\n")
            return
        
        nota = float(input("Introduza a nota do aluno (0-20): "))
        
        if 0 <= nota <= 20:
            nomes.append(nome)
            notas.append(nota)
            print("Aluno registado com sucesso!\n")
        else:
            print("Erro! A nota deve estar entre 0 e 20.\n")
            
    except ValueError:
        print("Erro! A nota deve ser um número válido.\n")


def listar_alunos():
    if not nomes:
        print("Não existem alunos registados.\n")
    else:
        print("Lista de Alunos:")
        for i, (nome, nota) in enumerate(zip(nomes, notas), start=1):
            print(f"{i} - {nome} | Nota: {nota}")
        print()


def eliminar_aluno():
    if not nomes:
        print("Não existem alunos para eliminar.\n")
    else:
        listar_alunos()
        try:
            indice = int(input("Indique o número do aluno a eliminar: "))
            
            if 1 <= indice <= len(nomes):
                nome_removido = nomes.pop(indice - 1)
                nota_removida = notas.pop(indice - 1)
                print(f"Aluno {nome_removido} com nota {nota_removida} eliminado com sucesso!\n")
            else:
                print("Índice inválido.\n")
                
        except ValueError:
            print("Erro! Deve introduzir um número inteiro.\n")


def alterar_aluno():
    if not nomes:
        print("Não existem alunos registados.\n")
    else:
        listar_alunos()
        try:
            indice = int(input("Indique o número do aluno a alterar: "))
            
            if 1 <= indice <= len(nomes):
                novo_nome = input("Introduza o novo nome: ")
                nova_nota = float(input("Introduza a nova nota: "))
                
                if 0 <= nova_nota <= 20:
                    nomes[indice - 1] = novo_nome
                    notas[indice - 1] = nova_nota
                    print("Dados alterados com sucesso!\n")
                else:
                    print("Nota inválida!\n")
            else:
                print("Índice inválido.\n")
                
        except ValueError:
            print("Erro! Dados inválidos.\n")


def estatisticas():
    if not notas:
        print("Não existem dados registados.\n")
    else:
        media = round(sum(notas) / len(notas), 2)
        maior = max(notas)
        menor = min(notas)
        
        print(f"Média da turma: {media}")
        print(f"Maior nota: {maior}")
        print(f"Menor nota: {menor}\n")


def exportar_pickle():
    if not nomes:
        print("Não existem dados para guardar.\n")
    else:
        try:
            with open("alunos_backup.pkl", "wb") as ficheiro:
                pickle.dump((nomes, notas), ficheiro)
            print("Backup exportado com sucesso!\n")
        except Exception as e:
            print(f"Erro ao exportar ficheiro: {e}\n")


def importar_pickle():
    global nomes, notas
    try:
        with open("alunos_backup.pkl", "rb") as ficheiro:
            nomes, notas = pickle.load(ficheiro)
        print("Backup importado com sucesso!\n")
    except FileNotFoundError:
        print("Erro! Ficheiro não encontrado.\n")
    except Exception as e:
        print(f"Erro ao importar ficheiro: {e}\n")

while True:
    print("Sistema de Gestão de Alunos")
    print("1 - Registar Aluno")
    print("2 - Listar Alunos")
    print("3 - Eliminar Aluno")
    print("4 - Alterar Dados do Aluno")
    print("5 - Ver Estatísticas")
    print("6 - Exportar Backup")
    print("7 - Importar Backup")
    print("0 - Terminar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_aluno()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
        eliminar_aluno()
    elif opcao == "4":
        alterar_aluno()
    elif opcao == "5":
        estatisticas()
    elif opcao == "6":
        exportar_pickle()
    elif opcao == "7":
        importar_pickle()
    elif opcao == "0":
        print("Programa terminado. Obrigado!")
        break
    else:
        print("Opção inválida!\n")