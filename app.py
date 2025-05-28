options = (
    ('1', 'Adicionar'),
    ('2', 'Ver Todos'),
    ('3', 'Editar'),
    ('4', 'Favoritar'),
    ('5', 'Ver Favoritos'),
    ('6', 'Remover Contato'),
    ('0', 'Sair')
)

menu = 'O que deseja fazer? \n\n'
for key, value in options:
    menu += f'{key} - {value} \n'

selected_option = input(menu)

for key, value in options:
    if selected_option == key:
        print('')
        print(value)
        break
else:
    print('Sair')






