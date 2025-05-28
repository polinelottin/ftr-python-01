from helpers import sanitize_favorite_input

def add_contact():
  name = input('Nome: ')
  phone = input('Telefone: ')
  email = input('Email: ')
  favorite = input('Favorito (s/N): ')

  contact = {
    'name': name,
    'phone': phone,
    'email': email,
    'favorite': sanitize_favorite_input(favorite)
  }

  return contact