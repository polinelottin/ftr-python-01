def divider():
  print('--------------------')

def display_selected_option(option):
  print('')
  print(option)
  divider()

def contact_info(index, contact):
  print(f'Contato #{index}')
  print(f'Nome: {contact["name"]}')
  print(f'Telefone: {contact["phone"]}')
  print(f'Email: {contact["email"]}')
  print(f'Favorito: {contact["favorite"]}')
  print('---------------------')

def display_contacts_info(contacts):
  if len(contacts) == 0:
    print('Nenhum contato encontrado')
    return
  
  print(f'Listando {len(contacts)} contatos')
  print('--------------------')
  
  for index, contact in enumerate(contacts, start=1):
    contact_info(index, contact)

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

