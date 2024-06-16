import psycopg2
from prettytable import PrettyTable
from datetime import date

class Connexion:
    def __init__(self):
        self.__HOST = "localhost"
        self.__USER = "postgres"
        self.__DATABASE = ""
        self.__PASSWORD = ""

    @property
    def HOST(self):
        return self.__HOST

    @HOST.setter
    def HOST(self, value):
        if type(value) != str:
            raise TypeError("Host doit être une str")
        self.__HOST = value

    @property
    def USER(self):
        return self.__USER

    @USER.setter
    def USER(self, value):
        if type(value) != str:
            raise TypeError("User doit être une str")
        self.__USER = value

    @property
    def DATABASE(self):
        return self.__DATABASE

    @DATABASE.setter
    def DATABASE(self, value):
        if type(value) != str:
            raise TypeError("Database doit être une str")
        self.__DATABASE = value

    @property
    def PASSWORD(self):
        return self.__PASSWORD

    @PASSWORD.setter
    def PASSWORD(self, value):
        if type(value) != str:
            raise TypeError("Host doit être une str")
        self.__PASSWORD = value

class Playlist():
    def __init__(self,cur):
        self.cur = cur

    def modification(self):
        pass

    def consultation(self):
        table = PrettyTable()
        self.cur.execute(open("Non_Relationnel/Views/Playlists_view.sql", "r").read())
        self.cur.execute("SELECT * from V_Playlists")
        print("Playlist")
        print('_______')
        table.field_names = [i[0] for i in self.cur.description]
        data = self.cur.fetchall()
        table.add_rows(data)
        print(table)

class Album():
    def __init__(self,cur):
        self.cur = cur

    def modification(self):
        pass

    def consultation(self):
        table = PrettyTable()
        self.cur.execute(open("Non_Relationnel/Views/Albums_view.sql", "r").read())
        self.cur.execute("SELECT * from V_Albums")
        print("Albums")
        print('_______')
        table.field_names = [i[0] for i in self.cur.description]
        data = self.cur.fetchall()
        table.add_rows(data)
        print(table)

class Chanson():
    def __init__(self,cur):
        self.cur = cur

    def modification(self):
        pass

    def consultation(self):
        table = PrettyTable()
        self.cur.execute(open("Non_Relationnel/Views/Chanson_view.sql", "r").read())
        self.cur.execute("SELECT * from V_Chansons")
        table.field_names = [i[0] for i in self.cur.description]
        data = self.cur.fetchall()
        table.add_rows(data)
        print(table)

def creation_table(cur):
    cur.execute(open("Non_Relationnel/Profil_Artiste/Profil_Artiste_TABLE.sql", "r").read())
    cur.execute(open("Non_Relationnel/Profil_Utilisateurice/Profil_Utilisateurice_TABLE.sql", "r").read())
    cur.execute(open("Non_Relationnel/Album/Album_TABLE.sql", "r").read())
    cur.execute(open("Non_Relationnel/Playlist/Playlist_TABLE.sql", "r").read())

def insertion_donnee(cur):
    cur.execute(open("Non_Relationnel/Profil_Artiste/Profil_Artiste_INSERTION.sql", "r").read())
    cur.execute(open("Non_Relationnel/Profil_Utilisateurice/Profil_Utilisateurice_INSERTION.sql", "r").read())
    cur.execute(open("Non_Relationnel/Album/Album_INSERTION.sql", "r").read())
    cur.execute(open("Non_Relationnel/Playlist/Playlist_INSERTION.sql", "r").read())

def suppression_bdd(cur):
    cur.execute("DROP VIEW IF EXISTS V_Chansons")
    cur.execute("DROP VIEW IF EXISTS V_Playlists")
    cur.execute("DROP VIEW IF EXISTS V_Albums")
    cur.execute(open("Non_Relationnel/Playlist/Playlist_DELETE.sql", "r").read())
    cur.execute(open("Non_Relationnel/Album/Album_DELETE.sql", "r").read())
    cur.execute(open("Non_Relationnel/Profil_Utilisateurice/Profil_Utilisateurice_DELETE.sql", "r").read())
    cur.execute(open("Non_Relationnel/Profil_Artiste/Profil_Artiste_DELETE.sql", "r").read())

def modification(cur, table):
    if table == 'a':
        Playlist(cur).modification()
    if table == 'b':
        Chanson(cur).modification()
    if table == 'c':
        Album(cur).modification()


def consultation(cur, table):
    if table == 'a':
        Playlist(cur).consultation()
    if table == 'b':
        Chanson(cur).consultation()
    if table == 'c':
        Album(cur).consultation()

def main():
    try:
        print("\nBienvenue dans le programme d'accès à votre base de donnée de streaming musical !")

        identifiants = Connexion()
        identifiants.HOST = input("Entrez le nom du serveur (HOST) : ")
        identifiants.USER = input("Entrez votre nom d'utilisteurice (USER) : ")
        identifiants.PASSWORD = input("Entrez votre mot de passe (PASSWORD) : ")
        identifiants.DATABASE = input("Entrez le nom de votre base de donnée (DATABASE) : ")

        conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (identifiants.HOST, identifiants.DATABASE, identifiants.USER, identifiants.PASSWORD))
        conn.autocommit = True
        print("Connexion réussie")
        choice = '1'

        while choice in ['1', '2', '*', '#']:
            cur = conn.cursor()
            print("__________________________________________________")
            print("Pour créer la base de donnée, entrez *")
            print("Pour supprimer l'entièreté de la base de donnée, entrez # ")
            print("Pour effectuer une modification dans la base de donnée, entrez 1")
            print("Pour effectuer une consultation dans la base de donnée, entrez 2")
            print("Pour quitter, entrez n'importe quel autre charactère")
            print("__________________________________________________")

            choice = input("Votre choix : ")
            if '1' <= choice <= '2':
                table = 'z'
                print("\nChoisissez la table concernée : Playlist(a), Chanson(b), Album(c)")
                table = input("Table : ")
                print("-----\n")

                while 'a' <= table <= 'c':
                    if choice == '1':
                        modification(cur, table)
                    if choice == '2':
                        consultation(cur, table)
                    table = 'z'

            if choice == '5' :
                print("Pour afficher la durée moyenne des chansons de chaque artiste (plus de 5 chansons), entrez a")
                print("Pour afficher les 10 artistes les plus prolifiques de la base de donnée, entrez b")
                print("Pour afficher les artistes ayant les chansons les plus longues (> 10 min), entrez c")
                print("Pour afficher les 10 genres musicaux préférés des utilisateur•ice•s, entrez d")
                req = input("Requête : ")
                print("-----\n")


            if choice == '*':
                suppression_bdd(cur)
                creation_table(cur)
                insertion_donnee(cur)
                print("La base de données a bien été crée.")

            if choice == '#' :
                suppression_bdd(cur)
                print("La base de donnée a été supprimée.")

        conn.close()

    except Exception as error :
        print("Une erreur s'est produite : ", error)
        print("Type d'exception : ", type(error))


if __name__ == '__main__':
    main()