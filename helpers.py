from printer import feedback

def sanitize_favorite_input(input):
  return True if input == 's' else False

def sanitize_number_input(input):
  try:
    value = int(input)
    return value
  except ValueError:
    return None
  
def find_contact_by_number(contacts, number):
  if number is None or number > len(contacts):
    feedback('Número de contato inválido')
    return None

  return contacts[number - 1]
