import menu
import add_contact

contacts = []

while True:
    selected_option = menu.show_menu()

    for key, value in menu.options:
        if selected_option == key:
            ## Show selected option
            print('')
            print(value)
            print('---------------------')

            ## Do something
            if key == '1':
                contact = add_contact.add_contact()
                contacts.append(contact)
                print('Contato adicionado com sucesso!')
            elif key == '2':
                print(contacts)
            elif key == '0':
                print('Saindo...')
                exit()

            break
    else:
        print('Opção inválida')
  