import authentication
import store
import storage
import settings

settings.init()

menu = 0

while menu != 7:
    print('\nMenu')
    menu = int(input(
        "\t1. Cadastrar Loja\n\t2. Listar Produtos por Loja\n\t3. Cadastrar Lojas\n\t4. Sair"))

    if menu == 1:

    elif menu == 2:

    elif menu == 3:     

    elif menu == 4:
        authentication.logout()
        
    else:
        print("\033[31mOPÇÃO INVALIDA!\033[m")