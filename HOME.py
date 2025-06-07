def linha():
    print("-"*20)

option = 1
while option != 0:
    
    print("""
    ------------------------------
    ESCOLHA UMA DAS OPCOES ABAIXO:
    ------------------------------
    1- PESSOAS REGISTRADAS:
    2- REGISTRAR ALGUEM
    3- REMOVER ALGUEM
    0- SAIR
    ------------------------------""")

    while True:
        option = input(":")
        if(option.isnumeric()):
            option = int(option)
            break
        else:
            print("digite uma opção valida\n")
    if option == 0:
        print("Volte sempre\n")
    #pessoa quer ver quais são os dados
    elif option == 1:
        with open("dados.txt", "r") as dados:
            conteudo = dados.read()
            print(conteudo)
        linha()
    #adicionar alguem
    elif option == 2:
        nome = input("Digite o nome da pessoa: ") + "\n"
        idade = input("Digite a idade: ") + "\n"
        sexo = input("Digite o sexo: " ) + '\n'
        with open("dados.txt", "a") as dados:
            dados.write(nome)
            dados.write(idade)
            dados.write(sexo)
    #elif option == 3: 
