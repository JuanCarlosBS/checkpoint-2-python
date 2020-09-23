import settings


def create() :
    cont = 0
    while cont < 6:
        storeIsValid = False

        while storeIsValid != True:
            id = int(input('ESCREVA O CÓDIGO DA LOJA: '))
            found_item = list(filter(lambda _product: _product['id'] == id, settings.store))
            if len(found_item) > 0:
                print('CÓDIGO JÁ EXISTENTE.')
            elif id == 0:
                print('CÓDIGO DEVE SER DIFERENTE DE 0')
            else:
                storeIsValid = True

        name = input('ESCREVA O NOME DA LOJA: ')

        store = {
            'id' : id,
            'name' : name
        }

        settings.store.append(store)

        print('LOJA CADASTRADA COM SUCESSO.')

        cont += 1

    return settings.store