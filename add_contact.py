def add_contact():
  name = input('Nome: ')
  phone = input('Telefone: ')
  email = input('Email: ')
  favorite = input('Favorito (s/N): ')

  contact = {
    'name': name,
    'phone': phone,
    'email': email,
    'favorite': True if favorite == 's' else False
  }

  return contact