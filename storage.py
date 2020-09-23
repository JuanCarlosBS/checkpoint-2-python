import settings

def create():
    cont = 0
    while cont < 5:
        storageIsValid = False

        while storageIsValid != True:
            id = int(input('ESCREVA O CÓDIGO DO PRODUTO: '))
            found_item = list(filter(lambda _product: _product['id'] == id, settings.storage))
            if len(found_item) > 0:
                print('CÓDIGO JÁ EXISTENTE.')
            elif id == 0:
                print('CÓDIGO DEVE SER DIFERENTE DE 0')
            else:
                storageIsValid = True

        pricesPerStore = []

        for index in range(len(settings.store)):
            code = settings.store[index]['name'].upper()
            price = float(input(f'DIGITE O PREÇO DO PRODUTO NA LOJA {code} : '))
            pricesPerStore.append(price)

        product = {
            'id' : id,
            'price': pricesPerStore,
        }

        settings.storage.append(product)
        print('PRODUTO CADASTRADO COM SUCESSO.')
        cont += 1
        print(settings.storage)

    return settings.storage