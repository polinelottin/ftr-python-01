import menu

selected_option = menu.show_menu()

for key, value in menu.options:
  if selected_option == key:
    # Show next menu
    print('')
    print(value)

    # Do something

    # Show root
    # selected_option = menu.show_menu()
    break
else:
  print('Sair')
  