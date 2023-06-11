import json


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Accounts(metaclass=SingletonMeta):
    def populate(self, db_path):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """
        f = open(db_path, "r")
        self.accounts = json.loads(f.read())


"""
Usage:

>>> accounts = Accounts()
>>> accounts.populate(db_path) #use full path to json file

C:\\Users\\Лиза\\Code\\tg-inviter\\backend\\app\\internal\\data\\accountsDB
"""