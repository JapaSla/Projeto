import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_menu():
    opcoes = [
        "Cadastrar Médico",
        "Cadastrar Enfermeira",
        "Cadastrar Técnica de Enfermagem",
        "Listar Funcionários",
        "Buscar Funcionário",
        "Atualizar Funcionário",
        "Excluir Funcionário",
        "Sair"
    ]
    print("==== Sistema de Gerenciamento de Funcionários ====")
    for i, opcao in enumerate(opcoes):
        print(f"{i+1}. {opcao}")
    print("=================================================")