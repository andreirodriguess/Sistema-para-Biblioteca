from lib.interface.menu import *
option = 1
while option != 0:
    tela()
    option = leiaint(" : ")
    if option == 0:
        print("Volte sempre\n")
    #pessoa quer ver quais são os dados
    elif option == 1:
        ver_dados()
    #adicionar alguem
    elif option == 2:
        registrar_pessoa()
    elif option == 3:
        apagar_pessoa()
    else:
        print("digite um valor valido")
    
