class Ivan():

    def __init__(self):
      
        self.__description = {
          'name': 'Ivan',
          'surname': 'Buryackov',
          'age': '19',
          'repllink': '@Buryackov-Ivan'
        }

    def __str__(self):
        return f""" {str(self.__description.get('name'))}
                        {str(self.__description.get('surname'))}
                        {str(self.__description.get('age'))}
                        {str(self.__description.get('repllink'))}
                    """

    @property
    def full_name(self):
        return f'{self.__description.get("name")} {self.__description.get("surname")} '
