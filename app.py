import menu
import add_contact
import print_contacts

contacts = []

print('--------------------')
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

                print('--------------------\n')
                print('Contato adicionado com sucesso!\n')
                print('--------------------')
                input('Pressione enter para continuar')
                print('--------------------')
            elif key == '2':
                print_contacts.all(contacts)
                input('Pressione enter para continuar')
                print('--------------------')
            elif key == '0':
                print('Saindo...')
                exit()

            break
  