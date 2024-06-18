import psycopg2
from prettytable import PrettyTable
from datetime import date
import json
from psycopg2.extras import Json


class Profil_Artiste():
    def __init__(self, cur):
        self.cur = cur

    def consultation(self):
        table = PrettyTable()
        self.cur.execute("SELECT * from NR_Profil_Artiste;")
        print("Profils des artistes")
        print('_______')
        table.field_names = [i[0] for i in self.cur.description]
        data = self.cur.fetchall()
        table.add_rows(data)
        print(table)

    def modification(self):
        nom = input("Nom du compte artiste à modifier : ")
        self.cur.execute("SELECT id from NR_profil_Artiste where nom = %s", (nom,))
        id_compte = self.cur.fetchone()

        while not id_compte:
            print("/!\ Le compte renseigné n'appartient pas à la base de donnée.\n")
            nom = input("Nom du compte artiste à modifier : ")
            self.cur.execute("SELECT id from NR_profil_Artiste where nom = %s", (nom,))
            id_compte = self.cur.fetchone()

        print("Les modifications enregistrées ci-dessous seront prises en compte, si aucune donnée n'est insérée pour un attribut, la valeur restera inchangée.")

        new_name = input("Nouvel identifiant du compte : ")
        self.cur.execute("SELECT id from NR_Profil_Utilisateurice where nom = %s", (new_name,))
        id = self.cur.fetchone()

        while new_name != '' and id:
            print("/!\ Le compte renseigné appartient déjà à la base de donné.\n")
            new_name = input("Nouvel identifiant du compte : ")
            self.cur.execute("SELECT id from NR_Profil_Utilisateurice where nom = %s", (new_name,))
            id = self.cur.fetchone()

        id = id_compte

        self.cur.execute("SELECT bio, type, groupe, pays from NR_Profil_Artiste where id = %s", (id,))
        bio, t, g, pi = self.cur.fetchone()

        biographie = input("Biographie du profil artiste : ")
        if biographie == '':
            biographie = bio

        pays = input("Pays du profil artiste : ")
        if pays == '':
            pays = pi

        type = input("Type (artiste/solo/groupe) : ")
        while type not in ['artiste', 'solo', 'groupe', '']:
            print("/!\ Le type renseigné n'est pas valide.\n")
            type = input("Type (artiste/solo/groupe) : ")

        if type == '':
            type = t
            self.cur.execute("UPDATE NR_Profil_Artiste set nom = %s, bio =%s, type= %s, groupe = %s, pays= %s where id=%s", (new_name,biographie, type, g, pays, id))

        else:
            if type == 'artiste' or type == 'groupe':
                type = "Profil_" + type.capitalize()
                self.cur.execute("UPDATE Profil_Artiste set nom = %s, bio =%s, type= %s, groupe = NULL, pays= %s where id=%s",(new_name,biographie, type, pays, id))

            if t == 'solo':
                type = 'Profil_Artiste_Solo'
                has_groupe = input("L'artiste appartient également à un groupe (y/n) : ")

                while has_groupe not in ['y', 'n']:
                    print("/!\ La réponse à la question n'est pas valide.\n")
                    has_groupe = input("L'artiste appartient également à un groupe (y/n) : ")

                if has_groupe == 'n':
                    self.cur.execute("UPDATE Profil_Artiste set nom = %s, bio =%s, type= %s, groupe = NULL, pays= %s where id=%s",(new_name, biographie, type, pays, id))

                else:
                    groupe = input("Nom du groupe : ")
                    self.cur.execute("SELECT type,id from NR_Profil_Artiste where id = %s",(groupe,))
                    data = self.cur.fetchone()
                    while groupe != '' and (not data or (data and data[0] != 'Profil_Groupe')):
                        print("/!\ Le nom de groupe renseigné n'appartient pas à la base de donnée ou ne correspond pas au profil d'un groupe. \n")
                        groupe = input("Nom du groupe : ")
                        self.cur.execute("SELECT type,id from NR_Profil_Artiste where id = %s", (groupe,))
                        data = self.cur.fetchone()

                        self.cur.execute("UPDATE NR_Profil_Artiste set nom=%s, bio =%s, type= %s, groupe = %s, pays= %s where id=%s",(new_name, biographie, type, data[1], pays, id))
        print("Donnée modifiée avec succès.")

class Profil_Utilisateurice():
    def __init__(self, cur):
        self.cur = cur

    def consultation(self):
        table = PrettyTable()
        self.cur.execute("SELECT * from NR_Profil_Utilisateurice;")
        print("Profils des utilisateur•ice•s")
        print('_______')
        table.field_names = [i[0] for i in self.cur.description]
        data = self.cur.fetchall()
        table.add_rows(data)
        print(table)

    def modification(self):
        nom = input("Nom du compte utilisateurice à modifier : ")
        self.cur.execute("SELECT id from NR_profil_Utilisateurice where nom = %s", (nom,))
        id_compte = self.cur.fetchone()

        while not id_compte:
            print("/!\ Le compte renseigné n'appartient pas à la base de donnée.\n")
            nom = input("Nom du compte utilisateurice à modifier : ")
            self.cur.execute("SELECT id from NR_profil_Utilisateurice where nom = %s", (nom,))
            id_compte = self.cur.fetchone()

        print("Les modifications enregistrées ci-dessous seront prises en compte, si aucune donnée n'est insérée pour un attribut, la valeur restera inchangée.")

        new_name = input("Nouvel identifiant du compte : ")
        self.cur.execute("SELECT id from NR_Profil_Utilisateurice where nom = %s", (new_name,))
        id = self.cur.fetchone()

        while new_name != '' and id:
            new_name = input("Nouvel identifiant du compte : ")
            self.cur.execute("SELECT id from NR_Profil_Utilisateurice where nom = %s", (new_name,))
            id = self.cur.fetchone()

        id = id_compte

        self.cur.execute("SELECT mail, mdp, statut from NR_Profil_Utilisateurice where id = %s", (id,))
        mel, mdp, st = self.cur.fetchone()

        email = input("Mail du profil utilisateurice : ")
        self.cur.execute("SELECT mail from NR_Profil_Utilisateurice where mail =%s ", (email,))
        mail = self.cur.fetchone()

        while email != '' and mail:
            print("/!\ Un compte est déjà enregistré avec cet email.\n")
            email = input("Mail du profil utilisateurice : ")
            self.cur.execute("SELECT mail from NR_Profil_Utilisateurice where mail =%s ", (email,))
            mail = self.cur.fetchone()

        if email == '':
            email = mel

        mot_de_passe = input("Mot de passe de l'utilisateurice : ")
        if mot_de_passe == '':
            mot_de_passe = mdp

        statut = input("Statut du compte (premium/regulier) : ")

        while statut not in ['premium', 'regulier', '']:
            print("/!\ Le status du compte n'est pas valide.\n")
            statut = input("Statut du compte (premium/regulier) : ")

        if statut == '':
            statut = st

        self.cur.execute("UPDATE NR_Profil_Utilisateurice set nom = %s, mail = %s, mdp = %s, statut = %s where id = %s",(new_name, email, mot_de_passe, statut, id))
        print("Donnée modifiée avec succès.")

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
        self.cur.execute(open("Views/Playlists_view.sql", "r").read())
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
        self.cur.execute(open("Views/Albums_view.sql", "r").read())
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
        titre = input("Titre de l'album de la chanson à modifier : ")
        artiste = input("Artiste principal de l'album : ")
        self.cur.execute("SELECT art.id from NR_Profil_Artiste art where nom = %s", (artiste,))
        art = self.cur.fetchone()

        while not art:
            print("/!\ Le nom d'artiste renseigné n'appartient pas à la base de donnée.\n")
            artiste = input("Artiste principal de l'album : ")
            self.cur.execute("SELECT art.id from NR_Profil_Artiste art where nom = %s", (artiste,))
            art = self.cur.fetchone()

        self.cur.execute("SELECT a.id from NR_Album a where a.artiste_principal=%s and a.titre=%s ", (art[0], titre))
        album = self.cur.fetchone()

        if not album:
            print("L'artiste n'interprète aucune album ayant ce nom pour titre.")

        else :
            true_exit = False
            while not true_exit :
                chanson_choisit = input("Titre de la chanson à modifier : ")
                self.cur.execute("SELECT chansons FROM NR_Album WHERE id = %s", (album,))
                chansons_list = self.cur.fetchone()[0]

                for i, chanson in enumerate(chansons_list):
                    if chanson['titre'] == chanson_choisit:

                        print( "Les modifications enregistrées ci-dessous seront prises en compte, si aucune donnée n'est insérée pour un attribut, la valeur restera inchangée.\n")

                        # Choix des attributs à modifier
                        nouveau_titre = input("Nouveau titre de la chanson : ") or chanson['titre']

                        nouvel_interprete = input("Nouvel•le interprète de la chanson : ")
                        self.cur.execute("SELECT id from NR_Profil_Artiste where nom = %s", (nouvel_interprete,))
                        nouvel_interprete_id = self.cur.fetchone()

                        while nouvel_interprete != '' and not nouvel_interprete_id:
                            print("/!\ L'artiste renseigné n'appartient pas à la base de donné.\n")
                            nouvel_interprete = input("Nouvel•le interprète de la chanson : ")
                            self.cur.execute("SELECT id from NR_Profil_Artiste where nom = %s", (nouvel_interprete,))
                            nouvel_interprete_id = self.cur.fetchone()

                        if nouvel_interprete == '':
                            nouvel_interprete_id = chanson['createurice']
                        else :
                            nouvel_interprete_id = nouvel_interprete_id[0]

                        nouvelle_duree = input("Nouvelle durée de la chanson (en seconde) : ")
                        while nouvelle_duree != '' and int(nouvelle_duree) < 0:
                            print("/!\ La durée renseignée n'est pas valide.\n")
                            nouvelle_duree = input("Nouvelle durée de la chanson (en seconde) : ")

                        if nouvelle_duree == '':
                            nouvelle_duree = chanson['duree']

                        nouveau_genre = input("Nouveau genre de la chanson : ") or chanson['genre_musical']

                        nouveaux_auteurices = input("Nouvelles•aux auteur•ice•s de la chanson : ") or chanson['droit_auteurice']['auteurs']
                        nouveaux_compositeurices = input("Nouvelles•aux compositeur•ice•s de la chanson : ") or chanson['droit_auteurice']['compositeurs']
                        nouveaux_editeurices = input("Nouvelles•aux editeur•ice•s de la chanson : ") or chanson['droit_auteurice']['editeurs']

                        # Modification de la chanson dans la liste
                        chansons_list[i] = {
                            'id': chanson['id'],
                            'titre': nouveau_titre,
                            'duree': int(nouvelle_duree),
                            'createurice': int(nouvel_interprete_id),
                            'genre_musical': nouveau_genre,
                            'droit_auteurice': {
                            'auteurs': nouveaux_auteurices,
                            'compositeurs': nouveaux_compositeurices,
                            'editeurs': nouveaux_editeurices
                            }
                        }
                        true_exit = True
                        break

                if not true_exit:
                    print("La chanson n'existe pas dans l'album sélectionné")

            # Mise à jour de l'attribut JSON dans la base de données

            update_query = "UPDATE NR_Album SET chansons = %s::jsonb WHERE id = %s ;"

            # Exécution de la requête avec les paramètres sécurisés
            self.cur.execute(update_query, (Json(chansons_list), album))
            print("Donnée modifiée avec succès.")

    def suppression(self):
        titre = input("Titre de l'album de la chanson à supprimer : ")
        artiste = input("Artiste principal de l'album : ")
        self.cur.execute("SELECT art.id from NR_Profil_Artiste art where nom = %s", (artiste,))
        art = self.cur.fetchone()

        while not art:
            print("/!\ Le nom d'artiste renseigné n'appartient pas à la base de données.\n")
            artiste = input("Artiste principal de l'album : ")
            self.cur.execute("SELECT art.id from NR_Profil_Artiste art where nom = %s", (artiste,))
            art = self.cur.fetchone()

        self.cur.execute("SELECT a.id from NR_Album a where a.artiste_principal=%s and a.titre=%s", (art[0], titre))
        album = self.cur.fetchone()

        if not album:
            print("L'artiste n'interprète aucun album ayant ce nom pour titre.")
        else:
            true_exit = False
            while not true_exit:
                chanson_choisit = input("Titre de la chanson à supprimer : ")
                self.cur.execute("SELECT chansons FROM NR_Album WHERE id = %s", (album[0],))
                chansons_list = self.cur.fetchone()[0]

                chanson_found = False
                for i, chanson in enumerate(chansons_list):
                    if chanson['titre'] == chanson_choisit:
                        chanson_found = True
                        del chansons_list[i]
                        break

                if chanson_found:
                    update_query = "UPDATE NR_Album SET chansons = %s::jsonb WHERE id = %s;"
                    self.cur.execute(update_query, (Json(chansons_list), album[0]))
                    print("Chanson supprimée avec succès.")
                    true_exit = True
                else:
                    print("La chanson spécifiée n'a pas été trouvée dans l'album.")


    def consultation(self):
        table = PrettyTable()
        self.cur.execute(open("Views/Chanson_view.sql", "r").read())
        self.cur.execute("SELECT * from V_Chansons")
        print("Chansons")
        print('_______')
        table.field_names = [i[0] for i in self.cur.description]
        data = self.cur.fetchall()
        table.add_rows(data)
        print(table)

def creation_table(cur):
    cur.execute(open("Profil_Artiste/Profil_Artiste_TABLE.sql", "r").read())
    cur.execute(open("Profil_Utilisateurice/Profil_Utilisateurice_TABLE.sql", "r").read())
    cur.execute(open("Album/Album_TABLE.sql", "r").read())
    cur.execute(open("Playlist/Playlist_TABLE.sql", "r").read())

def insertion_donnee(cur):
    cur.execute(open("Profil_Artiste/Profil_Artiste_INSERTION.sql", "r").read())
    cur.execute(open("Profil_Utilisateurice/Profil_Utilisateurice_INSERTION.sql", "r").read())
    cur.execute(open("Album/Album_INSERTION.sql", "r").read())
    cur.execute(open("Playlist/Playlist_INSERTION.sql", "r").read())

def suppression_bdd(cur):
    cur.execute("DROP VIEW IF EXISTS V_Chansons")
    cur.execute("DROP VIEW IF EXISTS V_Playlists")
    cur.execute("DROP VIEW IF EXISTS V_Albums")
    cur.execute(open("Playlist/Playlist_DELETE.sql", "r").read())
    cur.execute(open("Album/Album_DELETE.sql", "r").read())
    cur.execute(open("Profil_Utilisateurice/Profil_Utilisateurice_DELETE.sql", "r").read())
    cur.execute(open("Profil_Artiste/Profil_Artiste_DELETE.sql", "r").read())

def modification(cur, table):
    if table == 'a':
        Playlist(cur).modification()
    if table == 'b':
        Chanson(cur).modification()
    if table == 'c':
        Album(cur).modification()
    if table == 'd':
        Profil_Artiste(cur).modification()
    if table == 'e' :
        Profil_Utilisateurice(cur).modification()


def consultation(cur, table):
    if table == 'a':
        Playlist(cur).consultation()
    if table == 'b':
        Chanson(cur).consultation()
    if table == 'c':
        Album(cur).consultation()
    if table == 'd':
        Profil_Artiste(cur).consultation()
    if table == 'e' :
        Profil_Utilisateurice(cur).consultation()

def suppression(cur, table):
    if table == 'b':
        Chanson(cur).suppression()

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

        while choice in ['1', '2','3', '*', '#']:
            cur = conn.cursor()
            print("__________________________________________________")
            print("Pour créer la base de donnée, entrez *")
            print("Pour supprimer l'entièreté de la base de donnée, entrez # ")
            print("Pour effectuer une modification dans la base de donnée, entrez 1")
            print("Pour effectuer une consultation dans la base de donnée, entrez 2")
            print("Pour supprimer une chanson dans la base de donnée, entrez 3")
            print("Pour quitter, entrez n'importe quel autre charactère")
            print("__________________________________________________")

            choice = input("Votre choix : ")
            if '1' <= choice <= '3':
                table = 'z'
                print("\nChoisissez la table concernée : Playlist(a), Chanson(b), Album(c), Profil_Artiste(d), Profil_Utilisateurice(e)")
                table = input("Table : ")
                print("-----\n")

                while 'a' <= table <= 'e':
                    if choice == '1':
                        modification(cur, table)
                    if choice == '2':
                        consultation(cur, table)
                    if choice == '3':
                        suppression(cur, table)
                    table = 'z'

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