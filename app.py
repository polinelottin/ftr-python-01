from menu import show_menu, options
from printer import display_selected_option, divider, feedback, display_contacts_info, press_enter_to_continue
from add_contact import add_contact
from edit_contact import change_all_fields
from helpers import sanitize_number_input, find_contact_by_number

contacts = []

divider()
while True:
    selected_option = show_menu()

    for key, value in options:
        if selected_option == key:
            ## Show selected option
            display_selected_option(value)

            ## Do something
            if key == '1':
                #########################################################
                # ADD CONTACT
                #########################################################
                # Show add contact form
                contact = add_contact()

                # Add contact to contacts list
                contacts.append(contact)

                # Show feedback
                feedback('Contato adicionado com sucesso!')

                # Wait for user to press enter
                press_enter_to_continue()
            elif key == '2':
                #########################################################
                # LIST ALL CONTACTS
                #########################################################
                # Show all contacts
                display_contacts_info(contacts)

                # Wait for user to press enter
                press_enter_to_continue()
            elif key == '3':
                #########################################################
                # EDIT CONTACT
                #########################################################
                # Get contact number to edit
                contact_number_to_edit = sanitize_number_input(input('Digite o número do contato que deseja editar: '))

                # Find contact by number
                contact_to_edit = find_contact_by_number(contacts, contact_number_to_edit)

                # If contact is found, edit it
                if contact_to_edit is not None:
                    # Show form to edit contact
                    change_all_fields(contact_to_edit)

                    # Show feedback
                    feedback('Contato editado com sucesso!')

                # Wait for user to press enter
                press_enter_to_continue()
            elif key == '4':
                #########################################################
                # FAVORITE CONTACT
                #########################################################
                # Get contact number to favorite
                contact_number_to_favorite = sanitize_number_input(input('Digite o número do contato que deseja favoritar/desfavoritar: '))

                # Find contact by number
                contact_to_favorite = find_contact_by_number(contacts, contact_number_to_favorite)

                # If contact is found, toggle favorite status
                if contact_to_favorite is not None:
                    # Get previous favorite status
                    previous_favorite_status = contact_to_favorite['favorite']

                    # Toggle favorite status
                    contact_to_favorite['favorite'] = not previous_favorite_status

                    # Show feedback
                    feedback(f'Contato {"desfavoritado" if previous_favorite_status else "favoritado"} com sucesso!')

                # Wait for user to press enter
                press_enter_to_continue()
            elif key == '5':
                #########################################################
                # LIST ALL FAVORITE CONTACTS
                #########################################################
                # Filter all favorite contacts
                favoritos = [c for c in contacts if c["favorite"]]

                # Show all favorite contacts
                display_contacts_info(favoritos)

                # Wait for user to press enter
                press_enter_to_continue()
            elif key == '6':
                #########################################################
                # REMOVE CONTACT
                #########################################################
                contact_number_to_remove = sanitize_number_input(input('Digite o número do contato que deseja remover: '))

                # Find contact by number
                contact_to_remove = find_contact_by_number(contacts, contact_number_to_remove)

                # If contact is found, remove it
                if contact_to_remove is not None:
                    # Remove contact from contacts list
                    contacts.remove(contact_to_remove)

                    # Show feedback
                    feedback('Contato removido com sucesso!')

                # Wait for user to press enter
                press_enter_to_continue()
            elif key == '0':
                #########################################################
                # EXIT
                #########################################################
                print('Saindo...')

                # Exit while loop
                exit()

            break
  