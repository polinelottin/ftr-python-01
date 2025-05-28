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