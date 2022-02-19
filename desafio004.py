from curses.ascii import isalnum


teste = input('Digite algo: ')
print('Segue analise')
print('Tipo primitivo', type(teste))
print('Alphanumérico', teste.isalnum())