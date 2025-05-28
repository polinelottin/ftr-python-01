import menu
import printer
import add_contact
import edit_contact

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
                # Show add contact form
                contact = add_contact.add_contact()

                # Add contact to contacts list
                contacts.append(contact)

                # Show feedback
                printer.feedback('Contato adicionado com sucesso!')

                # Wait for user to press enter
                printer.press_enter_to_continue()
            elif key == '2':
                # Show all contacts
                printer.all(contacts)

                # Wait for user to press enter
                printer.press_enter_to_continue()
            elif key == '3':
                #TODO: Validate if the contact number is a number
                contact_number_to_edit = int(input('Digite o número do contato que deseja editar: '))

                edit_contact.all_fields(contacts[contact_number_to_edit - 1])

                # Show feedback
                printer.feedback('Contato editado com sucesso!')

                # Wait for user to press enter
                printer.press_enter_to_continue()
            elif key == '0':
                print('Saindo...')
                exit()

            break
  