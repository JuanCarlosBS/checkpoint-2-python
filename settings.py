

def init() :
    global menu
    global store
    global storage
    global possibleCreateStore


    menu = 0 
    store = [
        {
            'id' : 123,
            'name' : 'Casas Bahia'
        },
        {
            'id' : 456,
            'name' : 'Marisa'
        },
        {
            'id' : 789,
            'name' : 'Marabras'
        },
        {
            'id' : 98,
            'name' : 'AliExpress'
        },
        {
            'id' : 765,
            'name' : 'Amazon'
        },
        {
            'id' : 432,
            'name' : 'Ponto Frio'
        }
    ]
    storage = [
        {
            'id' : 1001,
            'price': [10,15,20,25,30,35],
        },
        {
            'id' : 1002,
            'price': [3,25,23,32,15,150],
        },
        {
            'id' : 1003,
            'price': [140,180,234,150,230,116],
        },
        {
            'id' : 1004,
            'price': [32,43,22,76,45,34],
        },
        {
            'id' : 1005,
            'price': [19,34,87,76,34,54],
        }
    ]
    possibleCreateStore = True