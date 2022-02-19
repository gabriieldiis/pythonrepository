a = input('Digite algo: ')
print('O tipo primitivo de algo é', type(a))
#sem conversões todos as respostas em a serão classificadas como <class 'str'> testaremos como 
print('Só tem espaços?', a.isspace())
print('É alphanumerico?', a.isalnum())
print('É numérico?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É formado por letras meiusculas?', a.isupper())
print('É formado apenas por letras minusculas?', a.islower())