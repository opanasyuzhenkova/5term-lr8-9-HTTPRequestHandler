class Sergeeva():

  def __init__(self):
    self.__description = {
      'name': 'Darya',
      'surname': 'Sergeeva',
      'repllink': '@DaryaSergeeva',
      'age': '32'
    }

  def __str__(self):
    return f""" {str(self.__description.get(b'name'))}
                    {str(self.__description.get(b'surname'))}
                    {str(self.__description.get(b'repllink'))}
                    {str(self.__description.get(b'age'))}
                """

  @property
  def full_name(self):
    return f'{self.__description.get("name")} {self.__description.get("surname")} '
