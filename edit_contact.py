#TODO: User can edit only one field at a time
def all_fields(contact):
  contact['name'] = input('Digite o novo nome do contato: ')
  contact['phone'] = input('Digite o novo telefone do contato: ')
  contact['email'] = input('Digite o novo email do contato: ')
  contact['favorite'] = True if input('Digite o novo favorito do contato: ') == 's' else False  