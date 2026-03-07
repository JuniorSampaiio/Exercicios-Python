alunos = []

def cadastrar_aluno():
    nome = input("Informe seu nome: ")
    idade = int(input("Informe sua idade: "))

    aluno = {
        "nome": nome,
        "idade": idade
    }

    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")


def listar_alunos():
    print("\nLista de Alunos:")

    for i, aluno in enumerate(alunos):
        print(i, "-", aluno["nome"], "-", aluno["idade"], "anos")


def atualizar_aluno():
    listar_alunos()

    indice = int(input("Digite o número do aluno que deseja atualizar: "))

    novo_nome = input("Novo nome: ")
    nova_idade = int(input("Nova idade: "))

    alunos[indice]["nome"] = novo_nome
    alunos[indice]["idade"] = nova_idade

    print("Aluno atualizado!")


def excluir_aluno():
    listar_alunos()

    indice = int(input("Digite o número do aluno que deseja excluir: "))

    alunos.pop(indice)

    print("Aluno excluído!")


while True:

    print("\n1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Atualizar aluno")
    print("4 - Excluir aluno")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar_aluno()

    elif opcao == 2:
        listar_alunos()

    elif opcao == 3:
        atualizar_aluno()

    elif opcao == 4:
        excluir_aluno()

    elif opcao == 5:
        print("Encerrando sistema...")
        break