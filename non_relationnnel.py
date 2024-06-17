import psycopg2
from prettytable import PrettyTable
from datetime import date
import json
from psycopg2.extras import Json

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
        titre = input("Titre de la playlist à modifier : ")
        compte = input("Compte dupuis lequel modifier la playlist : ")
        self.cur.execute("SELECT id from NR_Profil_Utilisateurice where nom = %s", (compte,))
        cre = self.cur.fetchone()

        while not cre:
            print("/!\ Le compte renseigné n'appartient pas à la base de donnée.\n")
            compte = input("Compte dupuis lequel modifier la playlist : ")
            self.cur.execute("SELECT id from NR_Profil_Utilisateurice where nom = %s", (compte,))
            cre = self.cur.fetchone()

        self.cur.execute("SELECT id from NR_Playlist where createurice=%s AND titre=%s", (cre, titre))
        playlist = self.cur.fetchone()

        if not playlist:
            print("/!\ Le profil ne possède aucune playlist ayant ce nom pour titre.\n")

        else:
            self.cur.execute("SELECT description, autorisation_acces FROM NR_Playlist where id = %s", (playlist[0],))
            des, aut = self.cur.fetchone()
            print(
                "Les modifications enregistrées ci-dessous seront prises en compte, si aucune donnée n'est insérée pour un attribut, la valeur restera inchangée.\n")

            t = input("Titre de la playlist : ")
            if t == '':
                t = titre

            c = input("Créateur•ice de la playlist : ")
            self.cur.execute("SELECT id from NR_Profil_Utilisateurice where nom = %s", (c,))
            c_ = self.cur.fetchone()

            while c != '' and not c_:
                print("/!\ Le compte renseigné n'appartient pas à la base de donné.\n")
                c = input("Créateur•ice de la playlist : ")
                self.cur.execute("SELECT id from NR_Profil_Utilisateurice where nom = %s", (c,))
                c_ = self.cur.fetchone()

            if c == '':
                c_ = cre

            if t != titre or c_ != cre:
                self.cur.execute("SELECT * FROM NR_Playlist where createurice = %s and titre = %s", (c_, t))
                data = self.cur.fetchone()

                if data:
                    print("/!\ Le compte possède dèjà une playlist du même nom.\n")
                    return

            d = input("Description de la playlist : ")
            if d == '':
                d = des

            a = input("Paramètre d'autorisation de la playlist (privee/publique/partagee_aux_amies) : ")

            while a not in ['privee', 'publique', 'partagee_aux_amies', '']:
                print("/!\ Le paramètre d'autorisation de la playlist n'est pas valide.\n")
                a = input("Paramètre d'autorisation de la playlist (privee/publique/partagee_aux_amies) : ")

            if a == '':
                a = aut

            self.cur.execute(
                "UPDATE NR_Playlist set titre = %s, createurice = %s, description = %s, autorisation_acces = %s where id = %s",
                (t, c_, d, a, playlist))
            print("Donnée modifiée avec succès.")

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
        titre = input("Titre de l'album à modifier : ")
        artiste = input("Artiste principal de l'album : ")
        self.cur.execute(
            "SELECT id from NR_Profil_Artiste where nom = %s",
            (artiste,))
        art = self.cur.fetchone()

        while not art:
            print("/!\ Le nom d'artiste renseigné n'appartient pas à la base de donnée.\n")
            artiste = input("Artiste principal de l'album : ")
            self.cur.execute(
                "SELECT id from NR_Profil_Artiste where nom = %s",
                (artiste,))
            art = self.cur.fetchone()

        self.cur.execute(
            "SELECT NR_Album.id from NR_Album JOIN NR_Profil_Artiste ON NR_Album.artiste_principal = NR_Profil_Artiste.id  where NR_Profil_Artiste.id = %s and NR_Album.titre=%s ",
            (art[0], titre))
        album = self.cur.fetchone()

        if not album:
            print("L'artiste n'interprète aucune album ayant ce nom pour titre.")
        else:

            print(
                "Les modifications enregistrées ci-dessous seront prises en compte, si aucune donnée n'est insérée pour un attribut, la valeur restera inchangée.\n")

            t = input("Titre de l'album : ")
            if t == '':
                t = titre

            i = input("Interprète de l'album : ")
            self.cur.execute("SELECT id from NR_Profil_Artiste where nom = %s", (i,))
            i_ = self.cur.fetchone()

            while i != '' and not i_:
                print("/!\ Le compte renseigné n'appartient pas à la base de donné.\n")
                i = input("Artiste principal de l'album : ")
                self.cur.execute("SELECT id from NR_Profil_Artiste where nom = %s", (i,))
                i_ = self.cur.fetchone()

            if i == '':
                i_ = art

            if t != titre or i_ != art:
                self.cur.execute(
                    "SELECT * from NR_Album JOIN NR_Profil_Artiste ON NR_Album.artiste_principal = NR_Profil_Artiste.id  where NR_Profil_Artiste.id = %s and NR_Album.titre=%s ",
                    (i_, t))
                data = self.cur.fetchone()

                if data:
                    print("/!\ L'artiste interprète déjà un album du même nom.\n")
                    return

            annee_sortie = input("Année de sortie de l'album : ")
            self.cur.execute(
                "SELECT annee_de_sortie from NR_Album JOIN NR_Profil_Artiste ON NR_Album.artiste_principal = NR_Profil_Artiste.id where NR_Profil_Artiste.nom = %s and NR_Album.titre=%s ",
                (artiste, titre))
            annee = self.cur.fetchone()

            while annee_sortie != '' and (int(annee_sortie) < 1900 or int(annee_sortie) > date.today().year):
                print("/!\ Renseignez une donnée valide.\n")
                annee_sortie = int(input("Année de sortie de l'album' : "))
                self.cur.execute(
                    "SELECT annee_de_sortie from NR_Album JOIN NR_Profil_Artiste ON NR_Album.artiste_principal = NR_Profil_Artiste.id  where NR_Profil_Artiste.nom = %s and NR_Album.titre=%s ",
                    (artiste, titre))
                annee = self.cur.fetchone()

            if annee_sortie == '':
                annee_sortie = annee
            else:
                annee_sortie = str(annee_sortie) + '-01-01'

            self.cur.execute("UPDATE NR_Album set titre = %s, artiste_principal = %s, annee_de_sortie =%s where id = %s",
                             (t, i_, annee_sortie, album))
            print("Donnée modifiée avec succès.")

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

    # def modification(self):
    #     album = input("Album auquel appartient la chanson à modifier : ") #nom de l'album
    #     true_exit = False
    #     while not true_exit : 
    #         chanson_choisit = input("Chanson à modifier : ") #nom de la chanson à modifier
    #         self.cur.execute("SELECT chansons FROM NR_Album WHERE titre = %s", (album,)) 
    #         chansons_list = self.cur.fetchone()[0] #recupt de toutes les chansons dans le Json de l'album selectionné
    #         # print(chansons)
        
    #         # chansons_list = json.loads(chansons) #liste de toutes les chansons dans le JSON
    #         for chanson in chansons_list:
    #             if chanson['titre'] == chanson_choisit:
                    
    #                 print("Les modifications enregistrées ci-dessous seront prises en compte, si aucune donnée n'est insérée pour attribut, la valeur restera inchangée.\n")

    #                 #choix des attributs à modifier
    #                 nouveau_titre = input("Nouveau titre de la chanson : ")
    #                 nouvelle_duree = input("Nouvelle durée de la chanson : ")
    #                 nouvel_interprete = input("Nouvel•le interprète de la chanson : ")
    #                 nouveau_genre = input("Nouveau genre de la chanson : ")
    #                 nouveaux_auteurices = input("Nouveau•lle auteur•ice•s de la chanson : ")
    #                 nouveaux_compositeurices = input("Nouveau•lle compositeur•ice•s de la chanson : ")
    #                 nouveaux_editeurices = input("Nouveau•lle editeur•ice•s de la chanson : ")

    #                 #modification des attributs de la chanson
    #                 if nouveau_titre != '': chanson['titre'] = nouveau_titre
    #                 if nouvelle_duree != '': chanson['duree'] = nouvelle_duree
    #                 if nouvel_interprete != '': chanson['interprete'] = nouvel_interprete
    #                 if nouveau_genre != '': chanson['genre'] = nouveau_genre
    #                 if nouveaux_auteurices != '': chanson['auteurices'] = nouveaux_auteurices
    #                 if nouveaux_compositeurices != '': chanson['compositeurices'] = nouveaux_compositeurices
    #                 if nouveaux_editeurices != '': chanson['editeurices'] = nouveaux_editeurices

                    

    #                 true_exit = True
    #                 break
    #         if not true_exit: #gestion du cas ou l'utilisateur ne choisit pas de chanson prsente
    #             print("La chanson n'existe pas dans l'album selectionné")


    def modification(self):
        album = input("Album auquel appartient la chanson à modifier : ")
        true_exit = False
        while not true_exit:
            chanson_choisit = input("Chanson à modifier : ")
            self.cur.execute("SELECT chansons FROM NR_Album WHERE titre = %s", (album,))
            chansons_list = self.cur.fetchone()[0]

            for i, chanson in enumerate(chansons_list):
                if chanson['titre'] == chanson_choisit:
                    print("Les modifications enregistrées ci-dessous seront prises en compte, si aucune donnée n'est insérée pour attribut, la valeur restera inchangée.\n")

                    # Choix des attributs à modifier
                    nouveau_titre = input("Nouveau titre de la chanson : ") or chanson['titre']
                    nouvelle_duree = input("Nouvelle durée de la chanson : ") or chanson['duree']
                    nouvel_interprete = input("Nouvel•le interprète de la chanson : ") or chanson['createurice']
                    nouveau_genre = input("Nouveau genre de la chanson : ") or chanson['genre_musical']
                    nouveaux_auteurices = input("Nouveau•lle auteur•ice•s de la chanson : ") or chanson['droit_auteurice']['auteurs']
                    nouveaux_compositeurices = input("Nouveau•lle compositeur•ice•s de la chanson : ") or chanson['droit_auteurice']['compositeurs']
                    nouveaux_editeurices = input("Nouveau•lle editeur•ice•s de la chanson : ") or chanson['droit_auteurice']['éditeurs']

                    # Modification de la chanson dans la liste
                    chansons_list[i] = {
                        'id': chanson['id'],
                        'titre': nouveau_titre,
                        'duree': int(nouvelle_duree),
                        'createurice': int(nouvel_interprete),
                        'genre_musical': nouveau_genre,
                        'droit_auteurice': {
                            'auteurs': nouveaux_auteurices.split(',') if nouveaux_auteurices else [],
                            'compositeurs': nouveaux_compositeurices.split(',') if nouveaux_compositeurices else [],
                            'éditeurs': nouveaux_editeurices.split(',') if nouveaux_editeurices else []
                        }
                    }

                    true_exit = True
                    break

            if not true_exit:
                print("La chanson n'existe pas dans l'album sélectionné")

        # Mise à jour de l'attribut JSON dans la base de données
        update_query = f"""
        UPDATE NR_Album
        SET chansons = {Json(chansons_list)}::jsonb
        WHERE titre = '{album}';
        """
        self.cur.execute(update_query)
        # self.conn.commit()



    def consultation(self):
        table = PrettyTable()
        self.cur.execute(open("Non_Relationnel/Views/Chanson_view.sql", "r").read())
        self.cur.execute("SELECT * from V_Chansons")
        print("Chansons")
        print('_______')
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