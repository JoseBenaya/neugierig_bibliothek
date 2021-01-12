from nbibliothek.ui import NbibliothekUI
from nbibliothek.database import NbibliothekDatabase

class NbibliothekService:
    def __init__(self, db_url):
        self.__db = NbibliothekDatabase(db_url)
        self.__ui = NbibliothekUI()

    def run(self):

        self.__ui.mainloop()

    def init_db(self):
        self.__db.init()
        
class AbstractObserver:
    def call(self):
        pass

class TitleNotFoundObserver(AbstractObserver):
    def call(self):
        pass