options = (
    ('1', 'Adicionar'),
    ('2', 'Ver Todos'),
    ('3', 'Editar'),
    ('4', 'Favoritar'),
    ('5', 'Ver Favoritos'),
    ('6', 'Remover Contato'),
    ('0', 'Sair')
)

def show_menu():
  menu = '---------------------\n'
  menu += 'O que deseja fazer? \n'
  menu += '--------------------\n'

  for key, value in options:
    menu += f'{key} - {value} \n'
  
  selected_option = input(menu)
  
  return selected_option