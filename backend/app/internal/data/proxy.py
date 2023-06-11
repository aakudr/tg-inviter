import json
from backend.app.internal.data.meta import SingletonMeta

class Proxy(metaclass=SingletonMeta):
    def populate(self, db_path):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """
        f = open(db_path, "r")
        self.proxy = json.loads(f.read())


"""
Usage:

>>> proxy = Proxy()
>>> proxy.populate(db_path) #use full path to json file

C:\\Users\\Лиза\\Code\\tg-inviter\\backend\\app\\internal\\data\\proxyDB
"""