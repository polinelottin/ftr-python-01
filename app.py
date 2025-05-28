import menu
import add_contact
import printer

contacts = []

printer.divider()
while True:
    selected_option = menu.show_menu()

    for key, value in menu.options:
        if selected_option == key:
            ## Show selected option
            print('')
            print(value)
            printer.divider()

            ## Do something
            if key == '1':
                contact = add_contact.add_contact()
                contacts.append(contact)

                printer.divider()

                feedback = '\n'
                feedback += 'Contato adicionado com sucesso!'
                feedback += '\n'

                print(feedback)
                printer.divider()
                input('Pressione enter para continuar')
                printer.divider()
            elif key == '2':
                printer.all(contacts)
                input('Pressione enter para continuar')
                printer.divider()
            elif key == '0':
                print('Saindo...')
                exit()

            break
  