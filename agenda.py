def inserir(agenda):
    contato = {}
    print()
    codigo = int(input("Digite o codigo do contato: "))
    nome = input("Digite o nome do contato: ")
    telefone = int(input("Digite o numero de telefone: "))
    contato["codigo"] = codigo
    contato["nome"] = nome
    contato["telefone"] = telefone 
    agenda.append(contato)
    return "INSERIDO!"
#********************************************************************************************************************************* 
def mostrar_todos_os_contatos(agenda):
    print()
    for contatos in agenda:
        print(f"Nome: {contatos['nome']}")
        for chave, valor in contatos.items():
            if chave == "codigo":
                print(f"Codigo: {valor}")
            elif chave == "telefone":
                print(f"Numero: {valor}")
        print()
#********************************************************************************************************************************* 
def buscar_contato(agenda):
    print()
    pesquisa = input("1* CODIGO\n 2* NOME\n 3* TELEFONE\n Qual a forma pretende pesquisar pelo o contato? ").lower()

    if pesquisa == '1':
        codigo = int(input("Digite o codigo do contato: "))
        for contato in agenda:
            if contato['codigo'] == codigo:
                print(contato)
                return
        print("Contato nao esta na agenda!")

    elif pesquisa == '2':
        nome = input("Digite o nome do contato: ").lower()
        for contato in agenda:
            if contato["nome"] == nome:
                print(contato)
                return
        print("Contato não esta na agenda!")

    elif pesquisa == '3':
        telefone = int(input("Digíte o Telefone: "))
        for contato in agenda:
            if contato['telefone'] == telefone:
                print(contato)
        print("Contato nao esta na agenda!")
#********************************************************************************************************************************* 
def editar_contato(agenda):
    print()
    pesquisa = input("1* CODIGO\n 2* NOME\n 3* TELEFONE\n Qual a forma pretende pesquisar pelo o contato E editar? ").lower()
    if pesquisa == '1':
        codigo = int(input("Digite o atual CODIGO do contato: "))
        for contato in agenda:
            if contato["codigo"] == codigo:
                print("Codigo atual =",codigo)
                contato["codigo"] = int(input("Digite o novo codigo: "))
                return "Atualizado!"
        print("Codigo não esta na agenda!")

    elif pesquisa == '2':
        nome = input("Digite o atual NOME do contato: ").lower()
        for contato in agenda:
            if contato["nome"] == nome:
                print("Nome ATUAL =",nome)
                contato["nome"] = input("Digite um nome para Subistituir: ")
                return "Atualizado!"
        print("NOME nao esta na agenda")

    elif pesquisa == '3':
        telefone = int(input("Digite o atual TELEFONE do contato: "))
        for contato in agenda:
            if contato["telefone"] == telefone:
                print("Telefone ATUAL =",telefone)
                contato["telefone"] = int(input("Digite um telefone para Subistituir: "))
                return "Atualizado!"
        print("Telefone nao esta na agenda")

#********************************************************************************************************************************* 
def ordenar_contatos_por_nome(agenda):
    print()
    for i in range(len(agenda)):
        posicao_menor = i #posicao menor, usado para armazenar o menor elemento encontrado (i)
        for j in range(i + 1, len(agenda)):
            if agenda[j]["nome"] < agenda[posicao_menor]["nome"]: #maior e menor tambem funciona papa ftring(CARACTER)
                posicao_menor = j
        agenda[i], agenda[posicao_menor] = agenda[posicao_menor], agenda[i]
    print()
    for contatos in agenda:
        print(f"Nome: {contatos['nome']}")
        for chave, valor in contatos.items():
            if chave == "codigo":
                print(f"Codigo: {valor}")
            elif chave == "telefone":
                print(f"Numero: {valor}")
#********************************************************************************************************************************* 
def apagar_contato(agenda):
    print()
    pesquisa = input("MENU:\n (1) - CÓDIGO do contato.\n (2) - NOME do contato.\n (3) - TELEFONE do contato.\n Como gostaria de pesquisar o contato para deletar? ").lower()
    if pesquisa == '1':
        codig = int(input("Digite o código do contato: "))
        for contato in agenda:
            if contato["codigo"] == codig:
                print(contato)
                agenda.remove(contato)
                print("Contato removido: ", contato)
                return
            
    if pesquisa == '2':
        nome = input("Digite o nome do contato: ")
        for contato in agenda:
            if contato['nome'] == nome:
                print(contato)
                agenda.remove(contato)
                print("Contato removido: ", contato)
                return
            
    if pesquisa == '3':
        telefone = int(input("Digite o TELEFONE do contato: "))
        for contato in agenda:
            if contato["telefone"] == telefone:
                print(contato)
                agenda.remove(contato)
                print("Contato removido: ",contato)
                return
#*********************************************************************************************************************************        
def menu():
    agenda = []
    while True:
        print()
        escolha = input("MENU:\n (1) - INSERIR contato.\n (2) - MOSTRAR todos os Contatos.\n (3) - BUSCAR contato.\n (4) - EDITAR contato.\n (5) - ORDENAR contato.\n (6) - APAGAR contato.\n (0) - Para 'sair'.\n Digite qual função voce deseja: ").lower()
        if escolha == '1':
            print(inserir(agenda))
        elif escolha == '2':
            mostrar_todos_os_contatos(agenda)
        elif escolha == '3':
            buscar_contato(agenda)
        elif escolha == '4':
            print(editar_contato(agenda))
        elif escolha == '5':
            ordenar_contatos_por_nome(agenda)
        elif escolha == '6':
            apagar_contato(agenda)
        elif escolha.lower() == "0" or escolha.lower() == 'sair':
            break
        else:
            print("Opiçao inválida digite novamente.")
menu()

