import settings

def logout():
  print('SAINDO...')
  exit()

def authenticationPossibleCreateStore() :
    if len(settings.store) > 0:
        settings.possibleCreateStore = False
