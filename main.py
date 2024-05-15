import psycopg2
from datetime import date

from postgres import DATABASE, PASSWORD

class Connexion:
    def __init__(self):
        self.__HOST = "localhost"
        self.__USER = "postgres"
        self.__DATABASE = DATABASE
        self.__PASSWORD = PASSWORD

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


class Compte() :
    def __init__(self, cur):
        self.cur = cur
    def insertion(self):
        nom = input("Identifiant du compte à ajouter : ")
        self.cur.execute("SELECT * from Compte where nom = %s", (nom,))
        data = self.cur.fetchone()
        if data:
            print("/!\ L'identifiant renseigné est déjà utilisé.\n")
        else:
            type = input("Type du compte à ajouter (utilisateurice/artiste) : ")
            while type not in ['utilisateurice', 'artiste']:
                print("/!\ Le type de compte renseigné n'est pas valide.\n")
                type = input("Type du compte à ajouter (utilisateurice/artiste) : ")

            self.cur.execute("INSERT INTO Compte(nom) VALUES (%s)", (nom,))
            self.cur.execute("SELECT id from Compte where nom = %s", (nom,))
            id = self.cur.fetchone()

            if type == "utilisateurice":
                mail = input("Mail : ")
                mdp = input("Mot de passe : ")
                statut = input("Statut (premium/regulier) : ")

                while statut not in ['premium', 'regulier']:
                    print("/!\ Le statut renseigné n'est pas valide.\n")
                    statut = input("Statut (premium/regulier) : ")

                self.cur.execute("INSERT INTO Profil_Utilisateurice VALUES(%s,%s,%s,%s,%s)",
                            (id, mail, mdp, date.today(), statut))
                print("Donnée insérée avec succès.")

            if type == "artiste":
                bio = input("Biographie : ")
                p = input("Pays : ")
                self.cur.execute("SELECT * from Pays where nom = %s", (p,))
                pays = self.cur.fetchone()
                while not pays:
                    print("/!\ Le pays renseigné n'appartient pas à la base de donnée.\n")
                    p = input("Pays : ")
                    self.cur.execute("SELECT * from Pays where nom = %s", (p,))
                    pays = self.cur.fetchone()

                type = input("Type (artiste/solo/groupe) : ")
                while type not in ['artiste', 'solo', 'groupe']:
                    print("/!\ Le type renseigné n'est pas valide.\n")
                    type = input("Type (artiste/solo/groupe) : ")

                if type == 'artiste' or type == 'groupe':
                    type = 'Profil_' + type.capitalize()
                    self.cur.execute("INSERT INTO Profil_Artiste VALUES(%s,%s,%s,NULL,%s)", (id, bio, type, pays))
                    print("Donnée insérée avec succès.")

                if type == 'solo':
                    type = 'Profil_Artiste_Solo'
                    g = input("L'artiste appartient également à un groupe (y/n) : ")

                    while g not in ['y', 'n']:
                        print("/!\ La réponse à la question n'est pas valide.\n")
                        g = input("L'artiste appartient également à un groupe (y/n) : ")

                    if g == 'n':
                        self.cur.execute("INSERT INTO Profil_Artiste VALUES(%s,%s,%s,NULL,%s)", (id, bio, type, pays))
                        print("Donnée insérée avec succès.")

                    else:
                        gr = input("Nom du groupe : ")
                        self.cur.execute(
                            "SELECT type,id from Profil_Artiste where id = (SELECT id from Compte where nom = %s)",
                            (gr,))
                        data = self.cur.fetchone()
                        while not data or (data and data[0] != 'Profil_Groupe'):
                            print(
                                "/!\ Le nom de groupe renseigné n'appartient pas à la base de donnée ou ne correspond pas au profil d'un groupe. \n")
                            gr = input("Nom du groupe : ")
                            self.cur.execute(
                                "SELECT type,id from Profil_Artiste where id = (SELECT id from Compte where nom = %s)",
                                (gr,))
                            data = self.cur.fetchone()

                        self.cur.execute("INSERT INTO Profil_Artiste VALUES(%s,%s,%s,%s,%s)", (id, bio, type, data[1], pays))
                        print("Donnée insérée avec succès.")

    def consultation(self):
        type = input("Quel type de compte souhaitez vous visualiser (utilisateurice/artiste/tous) ? ")
        if type == "utilisateurice":
            self.cur.execute("SELECT * FROM Compte JOIN Profil_Utilisateurice on Compte.id = Profil_Utilisateurice.id")
        if type == "artiste":
            self.cur.execute("SELECT * FROM Compte JOIN Profil_Artiste on Compte.id = Profil_Artiste.id")
        if type == "tous":
            self.cur.execute("SELECT * FROM Compte")

        headers = [i[0] for i in self.cur.description]
        print(headers)
        data = self.cur.fetchall()
        for row in data:
            print(row)

    def suppression(self):
        type = 'default'
        while type != 'utilisateurice' and  type != 'artiste' and  type != 'personne' :
            type = input("Quel type de compte souhaitez vous supprimer (utilisateurice/artiste/personne) ? ")
        nom = input("Quel est le nom du compte à supprimer : ")
        if type == "utilisateurice":
            self.cur.execute("SELECT * FROM Compte JOIN Profil_Utilisateurice on Compte.id = Profil_Utilisateurice.id WHERE nom='%s'"%(nom))
            data = self.cur.fetchall()
            if data :
                self.cur.execute(
                    "DELETE FROM Assos_Playlist_Chanson WHERE playlist IN (SELECT id FROM Playlist WHERE createurice IN (SELECT id FROM Compte WHERE nom='%s'))" % (nom))
                self.cur.execute(
                    "DELETE FROM Assos_Playlist_Album WHERE id_Playlist IN (SELECT id FROM Playlist WHERE  createurice IN (SELECT id FROM Compte WHERE nom='%s'))" % (nom))
                self.cur.execute(
                    "DELETE FROM Playlist WHERE createurice IN (SELECT id FROM Compte WHERE nom='%s')" % (nom))
                self.cur.execute("DELETE FROM Profil_Utilisateurice WHERE id IN (SELECT id FROM Compte WHERE nom ='%s') "%(nom))
                self.cur.execute("DELETE FROM Compte WHERE Compte.nom = '%s' "%(nom))
            else :
                print("Le compte spécifié n'existe pas")

        if type == "artiste":
            self.cur.execute("SELECT * FROM Compte JOIN Profil_Artiste on Compte.id = Profil_Artiste.id WHERE nom='%s'"%(nom))
            data = self.cur.fetchall()
            if data:
                self.cur.execute('''DELETE FROM Profil_Artiste
                                WHERE id IN (SELECT id FROM Compte WHERE nom ='%s') ''' % (nom))
                self.cur.execute('''DELETE FROM Compte
                                                WHERE Compte.nom = '%s' ''' % (nom))
            else :
                print("Le compte spécifié n'existe pas")

        if type == "personne":
            self.cur.execute("SELECT * FROM Compte WHERE nom='%s'"%(nom))
            data = self.cur.fetchall()
            if data:
                self.cur.execute("DELETE FROM Compte WHERE nom='%s'"%(nom))
            else :
                print("Le compte spécifié n'existe pas")



class Chanson() :
    def __init__(self, cur):
        self.cur = cur

    def insertion(self):
        artiste = input("Interprète de la chanson : ")
        self.cur.execute(
            "SELECT Profil_Artiste.id from Profil_Artiste JOIN Compte ON Profil_Artiste.id = Compte.id where nom = %s",
            (artiste,))
        art = self.cur.fetchone()

        while not art:
            print("/!\ Le nom d'artiste renseigné n'appartient pas à la base de donnée.\n")
            artiste = input("Interprète de la chanson : ")
            self.cur.execute(
                "SELECT Profil_Artiste.id from Profil_Artiste JOIN Compte ON Profil_Artiste.id = Compte.id where nom = %s",
                (artiste,))
            art = self.cur.fetchone()

        titre = input("Titre de la chanson : ")
        self.cur.execute(
            "SELECT * from Chanson JOIN Profil_Artiste ON Chanson.createurice = Profil_Artiste.id JOIN Compte ON Profil_Artiste.id = Compte.id where Compte.nom = %s and Chanson.titre=%s ",
            (artiste, titre))
        data = self.cur.fetchone()

        if data:
            print("/!\ L'artiste possède dèjà une chanson du même nom.\n")

        else:
            album = input("Album de la chanson : ")
            self.cur.execute("SELECT id, duree_totale from Album where titre = %s", (album,))
            alb = self.cur.fetchone()

            while not alb:
                print("/!\ Le nom d'album renseigné n'appartient pas à la base de donnée.\n")
                album = input("Album de la chanson : ")
                self.cur.execute("SELECT id, duree_totale from Album where titre = %s", (album,))
                alb = self.cur.fetchone()

            genre = input("Genre musical de la chanson : ")
            self.cur.execute("SELECT * from GenresMusicaux where nom = %s", (genre,))
            gen = self.cur.fetchone()

            while not gen:
                print("/!\ Le genre musical renseigné n'appartient pas à la base de donnée.\n")
                genre = input("Genre musical de la chanson : ")
                self.cur.execute("SELECT * from GenresMusicaux where nom = %s", (genre,))
                gen = self.cur.fetchone()

            duree = int(input("Durée de la chanson (en seconde): "))
            while duree < 0:
                print("/!\ La durée renseignée n'est pas valide.\n")
                duree = input("Durée de la chanson (en seconde): ")

            self.cur.execute("INSERT INTO Chanson VALUES(DEFAULT,%s,%s,%s,%s,%s)", (titre, duree, alb[0], art[0], genre))
            self.cur.execute("UPDATE Album SET duree_totale = %s where id = %s", (int(alb[1]) + duree, alb[0]))
            print("Donnée insérée avec succès.")

    def consultation(self):
        self.cur.execute("SELECT * FROM Chanson")
        headers = [i[0] for i in self.cur.description]
        print(headers)
        data = self.cur.fetchall()
        for row in data:
            print(row)

    def suppression(self):
        artiste = input("Nom de l'artiste de la chanson à supprimer : ")
        titre = input("Titre de la chanson à supprimer : ")
        self.cur.execute(
            "SELECT * from Chanson JOIN Profil_Artiste ON Chanson.createurice = Profil_Artiste.id JOIN Compte ON Profil_Artiste.id = Compte.id where Compte.nom = %s and Chanson.titre=%s ",
            (artiste, titre))
        data = self.cur.fetchone()

        if data:
                self.cur.execute("DELETE FROM Chanson WHERE createurice IN (SELECT id FROM Compte WHERE nom ='%s') AND titre='%s' "%(artiste,titre))
        else :
                print(f"{artiste} n'a pas de chanson {titre}")


class Album() :
    def __init__(self, cur):
        self.cur = cur

    def insertion(self):
        artiste = input("Artiste principal de l'album : ")
        self.cur.execute(
            "SELECT Profil_Artiste.id from Profil_Artiste JOIN Compte ON Profil_Artiste.id = Compte.id where nom = %s",
            (artiste,))
        art = self.cur.fetchone()

        while not art:
            print("/!\ Le nom d'artiste renseigné n'appartient pas à la base de donnée.\n")
            artiste = input("Artiste principal de l'album : ")
            self.cur.execute(
                "SELECT Profil_Artiste.id from Profil_Artiste JOIN Compte ON Profil_Artiste.id = Compte.id where nom = %s",
                (artiste,))
            art = self.cur.fetchone()

        titre = input("Titre de l'album : ")
        self.cur.execute(
            "SELECT * from Album JOIN Profil_Artiste ON Album.artiste_principal = Profil_Artiste.id JOIN Compte ON Profil_Artiste.id = Compte.id where Compte.nom = %s and Album.titre=%s ",
            (artiste, titre))
        data = self.cur.fetchone()

        if data:
            print("/!\ L'artiste possède dèjà un album du même nom.\n")

        else:
            annee = int(input("Année de sortie de l'album : "))
            while annee < 1900 or annee > date.today().year:
                print("/!\ L'année de sortie renseignée n'est pas valide.\n")
                annee = int(input("Année de sortie de l'album : "))

            ads = str(annee) + '-01-01'
            self.cur.execute("INSERT INTO Album VALUES(DEFAULT,%s,%s,%s,%s)", (titre, ads, 0, art[0]))
            print("Donnée insérée avec succès.")

    def consultation(self):
        self.cur.execute("SELECT * FROM Album")
        headers = [i[0] for i in self.cur.description]
        print(headers)
        data = self.cur.fetchall()
        for row in data:
            print(row)

    def suppression(self):
        artiste = input("Nom de l'artiste de l'album à supprimer : ")
        titre = input("Titre de l'album à supprimer : ")
        self.cur.execute(
            "SELECT * from Album JOIN Profil_Artiste ON Album.artiste_principal = Profil_Artiste.id JOIN Compte ON Profil_Artiste.id = Compte.id where Compte.nom = %s and Album.titre=%s ",
            (artiste, titre))
        data = self.cur.fetchone()

        if data:
            self.cur.execute(
                "DELETE FROM Chanson WHERE album IN (SELECT id FROM Album WHERE titre ='%s')" % (titre))
            self.cur.execute("DELETE FROM Album WHERE artiste_principal IN (SELECT id FROM Compte WHERE nom ='%s') AND titre='%s' "%(artiste,titre))
        else :
                print(f"{artiste} n'a pas d'album' {titre}")

class GenresMusicaux :
    def __init__(self, cur):
        self.cur = cur

    def insertion(self):
        genre = input("Quel genre musical souhaitez vous ajoutez ? ")
        self.cur.execute("SELECT * from GenresMusicaux where nom = %s", (genre,))
        data = self.cur.fetchone()
        if data:
            print("Cette donnée est déjà présente dans la base de donnée.")
        else:
            self.cur.execute("INSERT INTO GenresMusicaux(nom) VALUES (%s)", (genre,))
            print("Donnée insérée avec succès.")

    def consultation(self):
        self.cur.execute("SELECT * FROM GenresMusicaux")
        headers = [i[0] for i in self.cur.description]
        print(headers)
        data = self.cur.fetchall()
        for row in data:
            print(row)

    def suppression(self):
        genre = input("Titre du genre musical à supprimer : ")
        self.cur.execute("SELECT * from GenresMusicaux where nom = '%s'" %(genre))
        data = self.cur.fetchone()
        if data:
            self.cur.execute(
                "DELETE FROM Assos_Utilisateurice_GenreMusicaux WHERE genre IN (SELECT nom FROM GenresMusicaux WHERE nom ='%s')" % (genre))
            self.cur.execute(
                "DELETE FROM Chanson WHERE genre_musical IN (SELECT nom FROM GenresMusicaux WHERE nom ='%s')" % (genre))
            self.cur.execute("DELETE FROM GenresMusicaux WHERE nom='%s' "%(genre))
            print("Suppression réalisée avec succès ! \n")
        else :
                print(f"Le genre musical {genre} n'existe pas")

class Playlist():
    def __init__(self,cur):
        self.cur = cur

    def insertion(self):
        compte = input("Compte duquel crée la playlist : ")
        self.cur.execute("SELECT id from Compte where nom = %s",(compte,))
        c = self.cur.fetchone()

        while not c :
            print("/!\ Le compte renseigné n'appartient pas à la base de donnée.\n")
            compte = input("Compte duquel crée la playlist :")
            self.cur.execute("SELECT id from Compte where nom = %s", (compte,))
            c = self.cur.fetchone()

        titre = input("Titre de la playlist : ")
        self.cur.execute("SELECT * from Playlist JOIN Compte ON Playlist.createurice = Compte.id where Compte.id = %s and Playlist.titre=%s ",(c[0], titre))
        data = self.cur.fetchone()

        if data:
            print("/!\ Le compte possède dèjà une playlist du même nom.\n")

        else:
            des = input("Description de la playlist : ")
            aut = input("Paramètre d'autorisation de la playlist (privee/publique/partagee_aux_amies) : ")
            while aut not in ['privee', 'publique','partagee_aux_amies'] :
                print("/!\ Le paramètre d'autorisation de la playlist n'est pas valide.\n")
                aut = input("Paramètre d'autorisation de la playlist (privee/publique/partagee_aux_amies) : ")

            self.cur.execute("INSERT INTO Playlist VALUES(DEFAULT,%s,%s,%s,%s)", (titre, des, aut, c))
            print("Donnée insérée avec succès.")


    def consultation(self):
        self.cur.execute("SELECT * FROM Playlist")
        headers = [i[0] for i in self.cur.description]
        print(headers)
        data = self.cur.fetchall()
        for row in data:
            print(row)

    def suppression(self):
        titre = input("Titre de la playlist à supprimer : ")
        createurice = input("Nom de le.a createurice de la playlist : ")
        self.cur.execute("SELECT * from Playlist JOIN Compte ON Playlist.createurice = Compte.id where Compte.id IN (SELECT id FROM Compte WHERE nom='%s') AND Playlist.titre='%s' "%(createurice, titre))
        data = self.cur.fetchone()

        if data:
            self.cur.execute(
                "DELETE FROM Assos_Playlist_Chanson WHERE playlist IN (SELECT id FROM Playlist WHERE titre ='%s' AND createurice IN (SELECT id FROM Compte WHERE nom='%s'))" % (titre, createurice))
            self.cur.execute(
                "DELETE FROM Assos_Playlist_Album WHERE id_Playlist IN (SELECT id FROM Playlist WHERE titre ='%s' AND createurice IN (SELECT id FROM Compte WHERE nom='%s'))" % (titre, createurice))

            self.cur.execute("DELETE FROM Playlist WHERE titre='%s' AND createurice IN (SELECT id FROM Compte WHERE nom='%s')"%(titre, createurice))
            print("Suppression réalisée avec succès ! \n")
        else :
                print(f"{createurice} n'a pas de playlist {titre}")

class Pays():
    def __init__(self, cur):
        self.cur = cur

    def insertion(self):
        pays = input("Quel pays souhaitez vous ajoutez ? ")
        self.cur.execute("SELECT * from Pays where nom = %s", (pays,))
        data = self.cur.fetchone()
        if data:
            print("Cette donnée est déjà présente dans la base de donnée.")
        else:
            self.cur.execute("INSERT INTO Pays(nom) VALUES (%s)", (pays,))
            print("Donnée insérée avec succès.")

    def consultation(self):
        self.cur.execute("SELECT * FROM Pays")
        headers = [i[0] for i in self.cur.description]
        print(headers)
        data = self.cur.fetchall()
        for row in data:
            print(row)

    def suppression(self):
        pays = input("Nom du pays à supprimer : ")
        self.cur.execute("SELECT * from Pays where nom = '%s' "%(pays))
        data = self.cur.fetchone()

        if data:
            self.cur.execute("SELECT id from Profil_Artiste where pays = '%s' " %(pays))
            profils={}
            profils = self.cur.fetchone()
            self.cur.execute("DELETE FROM Profil_Artiste WHERE pays='%s' " % (pays))
            for i in profils :
                self.cur.execute("DELETE FROM Compte WHERE Compte.id = '%s' " % (i))
            self.cur.execute("DELETE FROM Pays WHERE nom='%s' "%(pays))
            print("Suppression réalisée avec succès ! \n")
        else :
                print(f"Le pays {pays} n'a ps été trouvé dans la base de donnée")


def creation_table(cur):
    cur.execute(open("Pays/Pays_TABLE.sql", "r").read())
    cur.execute(open("Compte/Compte_TABLE.sql", "r").read())
    cur.execute(open("GenresMusicaux/GenresMusicaux_TABLE.sql", "r").read())
    cur.execute(open("Profil_Artiste/Profil_Artiste_TABLE.sql", "r").read())
    cur.execute(open("Profil_Utilisateurice/Profil_Utilisateurice_TABLE.sql", "r").read())
    cur.execute(open("Album/Album_TABLE.sql", "r").read())
    cur.execute(open("Chanson/Chanson_TABLE.sql", "r").read())
    cur.execute(open("Playlist/Playlist_TABLE.sql", "r").read())
    cur.execute(open("Assos_Playlist_Album/Assos_Playlist_Album_TABLE.sql", "r").read())
    cur.execute(open("Assos_Playlist_Chanson/Assos_Playlist_Chanson_TABLE.sql", "r").read())
    cur.execute(open("Assos_Utilisateurice_Utilisateurice/Assos_Utilisateurice_Utilisateurice_TABLE.sql", "r").read())
    cur.execute(open("Assos_Utilisateurice_GenreMusicaux/Assos_Utilisateurice_GenreMusicaux_TABLE.sql", "r").read())
    cur.execute(open("DroitsAuteurs/DroitsAuteurs_TABLE.sql", "r").read())

def insertion_donnee(cur):
    cur.execute(open("Pays/Pays_DATA.sql", "r").read())
    cur.execute(open("Compte/Compte_DATA.sql", "r").read())
    cur.execute(open("GenresMusicaux/GenresMusicaux_DATA.sql", "r").read())
    cur.execute(open("Profil_Artiste/Profil_Artiste_DATA.sql", "r").read())
    cur.execute(open("Profil_Utilisateurice/Profil_Utilisateurice_DATA.sql", "r").read())
    cur.execute(open("Album/Album_DATA.sql", "r").read())
    cur.execute(open("Chanson/Chanson_DATA.sql", "r").read())
    cur.execute(open("Playlist/Playlist_DATA.sql", "r").read())
    cur.execute(open("Assos_Playlist_Album/Assos_Playlist_Album_DATA.sql", "r").read())
    cur.execute(open("Assos_Playlist_Chanson/Assos_Playlist_Chanson_DATA.sql", "r").read())
    cur.execute(open("Assos_Utilisateurice_Utilisateurice/Assos_Utilisateurice_Utilisateurice_DATA.sql", "r").read())
    cur.execute(open("Assos_Utilisateurice_GenreMusicaux/Assos_Utilisateurice_GenreMusicaux_DATA.sql", "r").read())
    cur.execute(open("DroitsAuteurs/DroitsAuteurs_DATA.sql", "r").read())

def suppression_bdd(cur):
    cur.execute(open("Assos_Playlist_Album/Assos_Playlist_Album_DELETE.sql", "r").read())
    cur.execute(open("Assos_Playlist_Chanson/Assos_Playlist_Chanson_DELETE.sql", "r").read())
    cur.execute(open("Assos_Utilisateurice_Utilisateurice/Assos_Utilisateurice_Utilisateurice_DELETE.sql", "r").read())
    cur.execute(open("Assos_Utilisateurice_GenreMusicaux/Assos_Utilisateurice_GenreMusicaux_DELETE.sql", "r").read())
    cur.execute(open("DroitsAuteurs/DroitsAuteurs_DELETE.sql", "r").read())
    cur.execute(open("Playlist/Playlist_DELETE.sql", "r").read())
    cur.execute(open("Chanson/Chanson_DELETE.sql", "r").read())
    cur.execute(open("Album/Album_DELETE.sql", "r").read())
    cur.execute(open("Profil_Utilisateurice/Profil_Utilisateurice_DELETE.sql", "r").read())
    cur.execute(open("Profil_Artiste/Profil_Artiste_DELETE.sql", "r").read())
    cur.execute(open("Compte/Compte_DELETE.sql", "r").read())
    cur.execute(open("GenresMusicaux/GenresMusicaux_DELETE.sql", "r").read())
    cur.execute(open("Pays/Pays_DELETE.sql", "r").read())

def insertion(cur, table):
    if table == 'a':
        Compte(cur).insertion()
    if table == 'b':
        Chanson(cur).insertion()
    if table == 'c':
        Album(cur).insertion()
    if table == 'd':
        GenresMusicaux(cur).insertion()
    if table == 'e':
        Playlist(cur).insertion()
    if table == 'f':
        Pays(cur).insertion()

def modification(cur, table):
    pass

def suppression(cur, table):
    if table == 'a':
        Compte(cur).suppression()
    if table == 'b':
        Chanson(cur).suppression()
    if table == 'c':
        Album(cur).suppression()
    if table == 'd':
        GenresMusicaux(cur).suppression()
    if table == 'e':
        Playlist(cur).suppression()
    if table == 'f':
        Pays(cur).suppression()

def consultation(cur, table):
    if table == 'a':
        Compte(cur).consultation()
    if table == 'b':
        Chanson(cur).consultation()
    if table == 'c':
        Album(cur).consultation()
    if table == 'd':
        GenresMusicaux(cur).consultation()
    if table == 'e':
        Playlist(cur).consultation()
    if table == 'f':
        Pays(cur).consultation()

def Commande_perso(conn):
    cur = conn.cursor()
    commande = input("Entrez votre commande : ")
    cur.execute(commande)
    # Fetch data line by line
    raw = cur.fetchone()
    while raw:
        print(raw[0])
        raw = cur.fetchone()

def chansons_longues(conn):
    cur = conn.cursor()
    cur.execute(open("Interrogation/Artistes_chansons_longues.sql", "r").read())
    # Fetch data line by line
    raw = cur.fetchone()
    if raw :
        while raw:
            print("- Nom de l'auteur %s" % (raw[0]))
            raw = cur.fetchone()

def artistes_prolifiques(conn):
    cur = conn.cursor()
    cur.execute(open("Interrogation/Artistes_Prolifiques.sql", "r").read())
    # Fetch data line by line
    raw = cur.fetchone()
    if raw :
        while raw:
            print("- %s a sorti %s chansons" % (raw[0],raw[1]))
            raw = cur.fetchone()

def duree_moyenne(conn):
    cur = conn.cursor()
    cur.execute(open("Interrogation/Duree_moyenne_artiste.sql", "r").read())
    # Fetch data line by line
    raw = cur.fetchone()
    if raw :
        while raw:
            print("- Nom de l'auteur %s, durée moyenne %s : " % (raw[0], raw[1]))
            raw = cur.fetchone()

def genre_prefere(conn):
    cur = conn.cursor()
    user=input("De quel utilisateurice cherchez vous le genre préféré : ")
    sql ='''Select Compte.nom, Chanson.genre_musical, COUNT(Chanson.genre_musical) as "nombre_musiques_du_genre" 
        FROM Compte
        JOIN Playlist ON playlist.createurice = Compte.id
        JOIN Assos_Playlist_Chanson ON Assos_Playlist_Chanson.playlist = Playlist.id
        JOIN Chanson ON Chanson.id = Assos_Playlist_Chanson.chanson
    WHERE nom = '%s'
    GROUP BY Compte.nom, Chanson.genre_musical
    ORDER BY nom, nombre_musiques_du_genre DESC
    LIMIT 1'''%(user)
    cur.execute(sql)
    # Fetch data line by line
    raw = cur.fetchone()
    if raw :
        while raw:
            print("- Le genre préféré de %s est : %s" % (raw[0], raw[1]))
            raw = cur.fetchone()

def main():
    try:
        print("\nBienvenue dans le programme d'accès à votre base de donnée de streaming musical !")
        type_connexion='z'
        while type_connexion != 'o' and type_connexion != 'n' :
            type_connexion=input("Souhaitez vous utiliser des identifiants personnalisés ? o/n : ")
        identifiants = Connexion()

        if type_connexion =='o':
            identifiants.HOST=input("Entrez votre le nom du serveur (HOST) : ")
            identifiants.USER = input("Entrez votre nom d'utilisteur (USER) : ")
            identifiants.PASSWORD = input("Entrez votre mot de passe (PASSWORD) : ")
            identifiants.DATABASE = input("Entrez le nom de votre base de donnée (DATABASE) : ")

        conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (identifiants.HOST, identifiants.DATABASE, identifiants.USER, identifiants.PASSWORD))
        conn.autocommit = True
        cur = conn.cursor()
        print("Connexion réussie")
        choice = '1'

        # A exécuter pour supprimer l'entièreté de la base de donnée
        # suppression_bdd(cur)

        # A exécuter si la base de donnée n'est pas déjà crée
        # creation_table(cur)
        # insertion_donnee(cur)

        while '1' <= choice <= '4':
            print("__________________________________________________")
            print("Pour effectuer une insertion dans la base de donnée, entrez 1")
            print("Pour effectuer une modification dans la base de donnée, entrez 2")
            print("Pour effectuer une suppression dans la base de donnée, entrez 3")
            print("Pour effectuer une consultation dans la base de donnée, entrez 4")

            '''
            print("Pour executer une commande de votre choix en SQL, entrez 5")
            print("Pour afficher les artistes aux chansons longues, entrez 6")
            print("Pour afficher les artistes prolifiques, entrez 7")
            print("Pour afficher la durée moyenne des chansons d'un artiste, entrez 8")
            print("Pour afficher le genre musical préféré d'un.e utilisateurice, entrez 9")
            '''
            print("Pour quitter, entrez n'importe quel autre charactère")
            print("__________________________________________________")
            choice = input("Votre choix : ")

            '''
            if choice == '6':
                chansons_longues(conn)
            if choice == '7':
                artistes_prolifiques(conn)
            if choice == '8':
                duree_moyenne(conn)
            if choice == '9':
                genre_prefere(conn)
            '''

            if '1' <= choice <= '4':
                table = 'z'
                print("\nChoisissez la table concernée : Compte(a), Chanson(b), Album(c), GenreMusicaux(d), Playlist(e), Pays(f)")
                table = input("Table : ")
                print("-----\n")

                while 'a' <= table <= 'f':
                    if choice == '1':
                        insertion(cur, table)
                    if choice == '2':
                        modification(cur, table)
                    if choice == '3':
                        suppression(cur,table)
                    if choice == '4':
                        consultation(cur,table)
                    table = 'z'

        conn.close()

    except Exception as error :
        print("Une erreur s'est produite : ", error)
        print("Type d'exception : ", type(error))


if __name__ == '__main__':
    main()