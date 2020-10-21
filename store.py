import settings
import storage


def create() :
    cont = 0
    while cont < 6:
        storeIsValid = False

        while storeIsValid != True:
            id = int(input('ESCREVA O CÓDIGO DA LOJA: '))
            found_item = list(filter(lambda _store: _store['id'] == id, settings.store))
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


def index():
    print('\n')
    indexAllMinAndMaxPrices = []
    allMinPrices = []
    allMaxPrices = []
    for index in range(len(settings.store)):
        idStore = settings.store[index]['id']
        nameStore = settings.store[index]['name'].upper()
        print(f'{idStore} - {nameStore}\n')
        storage.index(index)
        print('\n')
    for product in range(len(settings.storage)):
        minValueProduct = min(settings.storage[product]['price'])
        maxValueProduct = max(settings.storage[product]['price'])
        allPricesForItem = []
        for store in range(len(settings.storage[product]['price'])):
            allPricesForItem.append(settings.storage[product]['price'][store])
        indexMinValueProduct = allPricesForItem.index(minValueProduct)
        indexMaxValueProduct = allPricesForItem.index(maxValueProduct)
        formatMinValueProduct = '{:,.2f}'.format(minValueProduct)
        print('O Produto ', settings.storage[product]['id'], ' foi encontrado na loja', settings.store[indexMinValueProduct]['name'], ' por R$ ', formatMinValueProduct)
        indexMinAndMaxPrices = {
            'indexMin': indexMinValueProduct,
            'indexMax': indexMaxValueProduct,
        }
        indexAllMinAndMaxPrices.append(indexMinAndMaxPrices)
        allMinPrices.append(minValueProduct)
        allMaxPrices.append(maxValueProduct)

        
    minValueAllProduct = min(allMinPrices)
    maxValueAllProduct = max(allMaxPrices)

    indexMinValueAllProduct = allMinPrices.index(minValueAllProduct)
    indexMaxValueAllProduct = allMaxPrices.index(maxValueAllProduct)

    indexMinValueStore = indexAllMinAndMaxPrices[indexMinValueAllProduct]['indexMin']
    indexMaxValueStore = indexAllMinAndMaxPrices[indexMaxValueAllProduct]['indexMax']

    print('Produto mais barato: Produto', settings.storage[indexMinValueAllProduct]['id'], ' encontrado na ', settings.store[indexMinValueStore]['name'],'.')
    print('Produto mais caro:', settings.storage[indexMaxValueAllProduct]['id'], ' encontrado na ', settings.store[indexMaxValueStore]['name'],'.')
    print('\n')