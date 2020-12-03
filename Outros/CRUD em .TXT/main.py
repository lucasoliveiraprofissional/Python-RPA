contato='xpto'
continuar='s'

with open('groups.txt', 'r', encoding='utf8') as f:
  groups = [group.strip() for group in f.readlines()]

while continuar == 's':
  contato= str(input('\nDigite o contato: '))
  if contato in groups:
    print('O contato já está no grupo! Não será adicionado!')
  else:
    print('Contato Inserido com sucesso!\n')
    with open('groups.txt', 'a', encoding='utf8') as f:
      f.write(f'\n{contato.strip()}')
  continuar = str(input('Deseja continuar (s/n)? '))
  continuar = continuar.lower()
  if continuar == 'n':
    break