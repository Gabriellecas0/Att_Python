
usuario = {"admin": "12345"}
def tela_login():
    print("=== TELA DE LOGIN ===")
    while True:
        login = input("Login: ")
        senha = input("Senha: ")

        if login in usuario and usuario[login] == senha:
            print("\nLogin feito com sucesso!\n")
            return True
        else:
            print("Login ou senha incorretos.\n")
def cadastrar_usuario():
    print("\n--- CADASTRO DE USUÁRIO ---")
    login = input("Digite um novo login: ")
    if not login:
        print("O login está errado!")
        return
    if login in usuario:
        print("Este login já está cadastrado")
    else:
        senha = input("Digite uma nova senha: ")
        usuario[login] = senha
        print(f"Usuário {login} cadastrado com sucesso!")
def listar_usuarios():
    print("\n--- USUÁRIOS CADASTRADOS ---")
    for login in usuario:
        print(f"- Login: {login}")

    print("\n--- PESQUISAR USUÁRIO ---")
    busca = input("Digite o login para pesquisar (ou Pressione Enter para voltar): ")
    if busca:
        if busca in usuario:
            print(f"Usuário {busca} encontrado no sistema!")
        else:
            print(f"Usuário {busca} não encontrado.")
def remover_usuario():
    print("\n--- REMOVER USUÁRIO ---")
    login = input("Digite o login do usuário a ser removido: ")
    if login == "admin":
        print("O usuário admin não pode ser removido")
    elif login in usuario:
        del usuario[login]
        print(f"Usuário {login} removido com sucesso!")
    else:
        print("Usuário não encontrado")
def menu_principal():
    while True:
        print("\n" "======================")
        print("    MENU PRINCIPAL")
        print("===========================")
        print("1. Cadastrar usuário")
        print("2. Pesquisar usuários")
        print("3. Remover usuário")
        print("4. Sair")
        opcao = input("Escolha uma opção (1-4): ")
        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            remover_usuario()
        elif opcao == "4":
            print("\nSaindo do sistema...")
            break
        else:
            print("Opção inválida")
if tela_login():
    menu_principal()