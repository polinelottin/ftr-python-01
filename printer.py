def all(contacts):
  for index, contact in enumerate(contacts, start=1):
    print(f'Contato #{index}')
    print(f'Nome: {contact["name"]}')
    print(f'Telefone: {contact["phone"]}')
    print(f'Email: {contact["email"]}')
    print(f'Favorito: {contact["favorite"]}')
    print('---------------------')

def divider():
  print('--------------------')

def press_enter_to_continue():
  input('Pressione enter para continuar')
  divider()

def feedback(message):
  divider()
  feedback = '\n'
  feedback += message
  feedback += '\n'
  print(feedback)
  divider()

def all_favorites(contacts):
  for index, contact in enumerate(contacts, start=1):
    if contact['favorite']:
      print(f'Contato #{index}')
      print(f'Nome: {contact["name"]}')
      print(f'Telefone: {contact["phone"]}')
      print(f'Email: {contact["email"]}')
      print(f'Favorito: {contact["favorite"]}')
      print('---------------------')