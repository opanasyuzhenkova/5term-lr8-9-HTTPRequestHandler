class Logwinow():
  def __init__(self):
    self.__description = {'name':'Andrew', 'surname': 'Logwinow', 'repllink':'@AndrieiLoghvino', 'age':'20'}
    
  def __str__(self):
        return f""" {str(self.__description.get('name'))}
                    {str(self.__description.get('surname'))}
                    {str(self.__description.get('repllink'))}
                    {str(self.__description.get('age'))}
                """
  @property
  def full_name(self):
      return f'{self.__description.get("name")} {self.__description.get("surname")} '