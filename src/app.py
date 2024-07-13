lista_principal = []

def cadastrar_aluno():
    print("Aqui vamos cadastrar o aluno")
    lista_aluno = []
    nome = input('Digite o nome do aluno: ')
    matrícula = int(input('Digite a matrícula do aluno: '))
    idade = int(input('Digite a idade do aluno: '))
    curso = input('Digite o curso do aluno: ')
    horário = input('Digite o horário do curso do aluno: ')
    lista_aluno.append(nome)
    lista_aluno.append(matrícula)
    lista_aluno.append(idade)
    lista_aluno.append(curso)
    lista_aluno.append(horário)
    lista_principal.append(lista_aluno)
    print("Aluno cadastrado com sucesso!")


def relatorio_estudantil():
    if len(lista_principal) == 0:
        print("Não há alunos cadastrados.")
    else:
        for aluno in lista_principal:
            print("Nome:", aluno[0])
            print("Matrícula:", aluno[1])
            print("Idade:", aluno[2])
            print("Curso:", aluno[3])
            print("Horário:", aluno[4])
            


def remover_aluno():
    matrícula = int(input("Informe a matrícula do aluno a ser removido: "))
    encontrou = False
    for aluno in lista_principal:
        if aluno[1] == matrícula:
            lista_principal.remove(aluno)
            encontrou = True
            print("Aluno removido com sucesso.")
            break
        if not encontrou:
            print("Aluno não encontrado.")







while True:
    print("1 - Cadastrar Aluno")
    print("2 - Relatório Estudantil")
    print("3 - Remover Aluno")
    print("0 - Sair")
    escolha = (input("Escolha sua opção: "))

    if escolha =="1":
        cadastrar_aluno()
    elif escolha == "2":
       relatorio_estudantil()
    elif escolha == "3":
        remover_aluno()
    elif escolha == "0":
        print("Obrigada por usar o programa, encerrando...")
        break
    else:
        print("Opção inválida. Tente novamente.")








