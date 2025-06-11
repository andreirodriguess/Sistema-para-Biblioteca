def linha():
    print("-"*30)

def tela():
    print("""
        ------------------------------
        ESCOLHA UMA DAS OPCOES ABAIXO:
        ------------------------------
        1- PESSOAS REGISTRADAS:
        2- REGISTRAR ALGUEM
        3- REMOVER ALGUEM
        0- SAIR
        ------------------------------\n""")
def leiaint(texto):
    while True:
        try:
            num = int(input(texto))
        except KeyboardInterrupt:
            print('\033[0;31mO usuario preferiu não digitar os valores\033[m')
            return 0
        except:
            print('\033[0;31mDigite um valor inteiro valido\033[m')
            continue
        else:
            return num
def ver_dados():
    try:
        with open("dados.txt", "r") as dados:
            conteudo = dados.read()
            print(conteudo)
    except FileNotFoundError:
        with open("dados.txt", "w") as dados:
            pass
    linha()

def registrar_pessoa():
    nome = "|nome : " + input("Digite o nome da pessoa: ")
    idade = "|idade : " + input("Digite a idade: ") 
    sexo = input("Digite o sexo: ") 
    sexo = "|sexo : " + sexo[0].upper() + '\n'
    with open("dados.txt", "a") as dados:
        dados.write(nome)
        dados.write(idade)
        dados.write(sexo)

def apagar_pessoa():
    nome_apagado = input("Digite o nome da pessoa que deseja apagar: ")
    with open("dados.txt", "r") as dados:
        linhas = dados.readlines()
    encontrado = False
    with open("dados.txt", "w") as dados:
        for l in linhas:
            if nome_apagado not in l and encontrado == False: #se o nome não estiver na linha, eu adiciono ela
                dados.writelines(l)
            else:
                encontrado = True
                print(f"{nome_apagado} foi removido")
        if encontrado == False:
            print(f"{nome_apagado} não foi encontrado")