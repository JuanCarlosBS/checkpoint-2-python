import authentication
import store
import storage
import settings

settings.init()

menu = 0

while menu != 7:
    print('\nMenu')
    menu = int(input(
        "\t1. Cadastrar Loja\n\t2. Cadastrar produto\n\t3. Listar Produto por Loja\n\t4. Sair\n"))

    if menu == 1:
        authentication.authenticationPossibleCreateStore()
        if settings.possibleCreateStore == True : 
            store.create()
        else :
            print("Não é possivel cadastrar mais lojas")
    elif menu == 2:
        authentication.authenticationPossibleCreateStore()
        if settings.possibleCreateStore == False :
            storage.create()
        else :
            print("Deve Cadastrar lojas antes de cadastrar produtos")
    elif menu == 3:     
        store.index()
    elif menu == 4:
        authentication.logout()
    else:
        print("\033[31mOPÇÃO INVALIDA!\033[m")