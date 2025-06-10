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
        nome = "|nome : " + input("Digite o nome da pessoa: ")
        idade = "|idade : " + input("Digite a idade: ") 
        sexo = input("Digite o sexo: ") 
        sexo = "|sexo : " + sexo[0].upper() + '\n'
        with open("dados.txt", "a") as dados:
            dados.write(nome)
            dados.write(idade)
            dados.write(sexo)
    elif option == 3:
        nome_apagado = input("Digite o nome da pessoa que deseja apagar: ")
        with open("dados.txt", "r") as dados:
            linhas = dados.readlines()
        with open("dados.txt", "w") as dados:
            for l in linhas:
                if nome_apagado not in l: #se o nome não estiver na linha, eu adiciono ela
                    dados.writelines(l)
                else:
                    print(f"{nome_apagado} foi removido")
                    
                    
                    
