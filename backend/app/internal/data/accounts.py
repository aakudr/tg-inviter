import json
from .meta import SingletonMeta

class Accounts(metaclass=SingletonMeta):
    def populate(self, db_path):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """
        f = open(db_path, "r")
        self.accounts = json.loads(f.read())
        return self

"""
Usage:

>>> accounts = Accounts()
>>> accounts.populate(db_path) #use full path to json file

C:\\Users\\Лиза\\Code\\tg-inviter\\backend\\app\\internal\\data\\accountsDB
"""