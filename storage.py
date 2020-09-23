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
            idStore = settings.store[index]['id']
            nameStore = settings.store[index]['name'].upper()

            price = float(input(f'DIGITE O PREÇO DO PRODUTO NA LOJA {idStore} - {nameStore} : '))
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


def index(indexStore):
    print('PRODUTO \t PREÇO')
    print('-'*32)
    for index in range(len(settings.storage)): 
        idStorage = settings.storage[index]['id']
        priceStorage = priceStore = settings.storage[index]['price']
        priceStore = settings.storage[index]['price'][indexStore]
        print(f'{idStorage} \t {"R$ {:,.2f}".format(priceStore)}')
        minPrice = min(priceStorage)
        settings.lowestPrice.append(minPrice)

