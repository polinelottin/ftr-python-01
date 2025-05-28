from helpers import sanitize_favorite_input

#TODO: User can edit only one field at a time
def change_all_fields(contact):
  contact['name'] = input('Digite o novo nome do contato: ')
  contact['phone'] = input('Digite o novo telefone do contato: ')
  contact['email'] = input('Digite o novo email do contato: ')
  contact['favorite'] = sanitize_favorite_input(input('Digite o novo favorito do contato: '))