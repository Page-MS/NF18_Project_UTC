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
                        self.cur.execute("SELECT type,id from Profil_Artiste where id = (SELECT id from Compte where nom = %s)",(gr,))
                        data = self.cur.fetchone()
                        while not data or (data and data[0] != 'Profil_Groupe'):
                            print("/!\ Le nom de groupe renseigné n'appartient pas à la base de donnée ou ne correspond pas au profil d'un groupe. \n")
                            gr = input("Nom du groupe : ")
                            self.cur.execute("SELECT type,id from Profil_Artiste where id = (SELECT id from Compte where nom = %s)",(gr,))
                            data = self.cur.fetchone()

                        self.cur.execute("INSERT INTO Profil_Artiste VALUES(%s,%s,%s,%s,%s)", (id, bio, type, data[1], pays))
                        print("Donnée insérée avec succès.")

    def consultation(self):
        type = input("Type de compte à visualiser (utilisateurice/artiste/tous) ? ")
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

        nom = input("Identifiant du compte à supprimer : ")
        self.cur.execute("SELECT id from Compte where nom = %s", (nom,))
        id = self.cur.fetchone()
        while not id :
            print("/!\ Le compte renseigné n'appartient pas à la base de donnée.\n")
            nom = input("Identifiant du compte à supprimer : ")
            self.cur.execute("SELECT id from Compte where nom = %s", (nom,))
            id = self.cur.fetchone()

        self.cur.execute("DELETE FROM Assos_Playlist_Chanson WHERE playlist IN (SELECT id FROM Playlist WHERE createurice = %s)",(id,))
        self.cur.execute("DELETE FROM Assos_Playlist_Album WHERE id_Playlist IN (SELECT id FROM Playlist WHERE  createurice =%s)",(id,))
        self.cur.execute("DELETE FROM Assos_Utilisateurice_GenresMusicaux WHERE utilisateurice =%s",(id,))
        self.cur.execute("DELETE FROM Assos_Utilisateurice_Utilisateurice WHERE ami_1 =%s OR ami_2=%s",(id,id))
        self.cur.execute("DELETE FROM DroitsAuteurs WHERE compte=%s",(id,))
        self.cur.execute("DELETE FROM Playlist WHERE createurice = %s", (id[0],))
        self.cur.execute("DELETE FROM Chanson WHERE createurice = %s", (id,))
        self.cur.execute("DELETE FROM Album WHERE artiste_principal = %s", (id,))
        self.cur.execute("DELETE FROM Profil_Utilisateurice WHERE id = %s", (id,))
        self.cur.execute("DELETE FROM Profil_Artiste WHERE id = %s", (id,))
        self.cur.execute("DELETE FROM Compte WHERE id = %s", (id,))
        print("Donnée supprimée avec succès.")


    def modification(self):

        nom = input("Compte à modifier : ")
        self.cur.execute("SELECT id from Compte where nom = %s", (nom,))
        compte = self.cur.fetchone()

        while not compte:
            print("/!\ Le compte renseigné n'appartient pas à la base de donnée.\n")
            nom = input("Compte à modifier : ")
            self.cur.execute("SELECT id from Compte where nom = %s", (nom,))
            compte = self.cur.fetchone()

        print("Les modifications enregistrées ci-dessous seront prises en compte, si aucune donnée n'est insérée pour un attribut, la valeur restera inchangée.")
        print("Il n'est pas possible de modifier un compte utilisateurice en compte artiste et inversement.\n")

        identifiant = input("Nouvel identifiant du compte : ")
        self.cur.execute("SELECT id from Compte where nom = %s", (identifiant,))
        id = self.cur.fetchone()

        while identifiant != '' and id :
            print("/!\ Le compte renseigné appartient déjà à la base de donné.\n")
            identifiant = input("Identifiant du compte: ")
            self.cur.execute("SELECT id from Compte where id = %s", (identifiant,))
            id = self.cur.fetchone()

        if identifiant == '':
            id = compte

        self.cur.execute("SELECT id from Profil_Utilisateurice where id = %s", (compte,))
        data = self.cur.fetchone()
        if data :  # profil utilisateurice

            self.cur.execute("SELECT mail, mdp, statut from Profil_Utilisateurice where id = %s", (compte,))
            mail, mot_de_passe, statut = self.cur.fetchone()

            mel = input("Mail du profil utilisateurice : ")
            self.cur.execute("SELECT mail from Profil_Utilisateurice where mail =%s ", (mel,))
            email = self.cur.fetchone()

            while mel != '' and email:
                print("/!\ Un compte est déjà enregistré avec cet email.\n")
                mel = input("Mail du profil utilisateurice : ")
                self.cur.execute("SELECT mail * Profil_Utilisateurice where mail =%s ", (mel,))
                email = self.cur.fetchone()

            if mel == '':
                mel = email

            mdp = input("Mot de passe de l'utilisateurice : ")

            if mdp == '':
                mdp = mot_de_passe

            st = input("Statut du compte (premium/regulier) : ")

            while st not in ['premium', 'regulier', '']:
                print("/!\ Le status du compte n'est pas valide.\n")
                st = input("Statut du compte (premium/regulier) : ")

            if st == '':
                st = statut

            if id != compte :
                self.cur.execute("UPDATE Compte set nom = %s where id = %s", (identifiant, compte))

            self.cur.execute("UPDATE Profil_Utilisateurice set mail = %s, mdp = %s, statut = %s where id = %s", (mel, mdp, st, id))
            print("Donnée modifiée avec succès.")


        else : # profil artiste

            self.cur.execute("SELECT bio, type, groupe, pays from Profil_Artiste where id = %s", (compte,))
            biographie, type, groupe, pays = self.cur.fetchone()

            bio = input("Biographie du profil artiste : ")

            if bio == '':
                bio = biographie

            p = input("Pays du profil artiste : ")
            self.cur.execute("SELECT * from Pays where nom = %s", (p,))
            pay = self.cur.fetchone()
            while p!='' and  not pay:
                print("/!\ Le pays renseigné n'appartient pas à la base de donnée.\n")
                p = input("Pays : ")
                self.cur.execute("SELECT * from Pays where nom = %s", (p,))
                pay = self.cur.fetchone()

            if p =='':
                p = pays

            t = input("Type (artiste/solo/groupe) : ")
            while t not in ['artiste', 'solo', 'groupe', '']:
                print("/!\ Le type renseigné n'est pas valide.\n")
                t = input("Type (artiste/solo/groupe) : ")

            if t == '':
                t = type
                self.cur.execute("UPDATE Profil_Artiste set bio =%s, type= %s, groupe = %s, pays= %s where id=%s", (bio, t, groupe, p, id))

            else :

                if t == 'artiste' or t == 'groupe':
                    t = "Profil_" + t.capitalize()
                    self.cur.execute("UPDATE Profil_Artiste set bio =%s, type= %s, groupe = NULL, pays= %s where id=%s", (bio,t, p, id))

                if t== 'solo' :
                    t = 'Profil_Artiste_Solo'
                    g = input("L'artiste appartient également à un groupe (y/n) : ")

                    while g not in ['y', 'n']:
                        print("/!\ La réponse à la question n'est pas valide.\n")
                        g = input("L'artiste appartient également à un groupe (y/n) : ")

                    if g == 'n':
                        self.cur.execute("UPDATE Profil_Artiste set bio =%s, type= %s, groupe = NULL, pays= %s where id=%s", (bio,t, p, id))

                    else:
                        gr = input("Nom du groupe : ")
                        self.cur.execute("SELECT type,id from Profil_Artiste where id = (SELECT id from Compte where nom = %s)", (gr,))
                        data = self.cur.fetchone()
                        while gr!='' and (not data or (data and data[0] != 'Profil_Groupe')):
                            print("/!\ Le nom de groupe renseigné n'appartient pas à la base de donnée ou ne correspond pas au profil d'un groupe. \n")
                            gr = input("Nom du groupe : ")
                            self.cur.execute("SELECT type,id from Profil_Artiste where id = (SELECT id from Compte where nom = %s)",(gr,))
                            data = self.cur.fetchone()

                        self.cur.execute("UPDATE Profil_Artiste set bio =%s, type= %s, groupe = %s, pays= %s where id=%s", (bio, t, data[1], p, id))

            if id != compte :
                self.cur.execute("UPDATE Compte set nom = %s where id = %s", (identifiant, compte))

            print("Donnée modifiée avec succès.")


class Amitie():
    def __init__(self, cur):
        self.cur = cur

    def insertion(self):
        print("Ajout d'un lien d'amitié entre deux utilisateur•ice•s.")
        nom_1 = input("Nom du premièr compte : ")
        self.cur.execute("SELECT Compte.id from Compte JOIN Profil_Utilisateurice ON Profil_Utilisateurice.id = Compte.id where nom = %s", (nom_1,))
        id_1 = self.cur.fetchone()

        while not id_1:
            print("/!\ Le nom de compte renseigné n'appartient pas à la base de donnée ou n'est pas calui d'un•e utilisateur•ice.\n")
            nom = input("Nom du premièr compte : ")
            self.cur.execute("SELECT Compte.id from Compte JOIN Profil_Utilisateurice ON Profil_Utilisateurice.id = Compte.id where nom = %s",(nom_1,))
            id_1 = self.cur.fetchone()

        nom_2 = input("Nom du deuxième compte : ")
        self.cur.execute("SELECT Compte.id from Compte JOIN Profil_Utilisateurice ON Profil_Utilisateurice.id = Compte.id where nom = %s",(nom_2,))
        id_2 = self.cur.fetchone()

        while not id_2:
            print("/!\ Le nom de compte renseigné n'appartient pas à la base de donnée ou n'est pas calui d'un•e utilisateur•ice.\n")
            nom_2 = input("Nom du deuxième compte : ")
            self.cur.execute("SELECT Compte.id from Compte JOIN Profil_Utilisateurice ON Profil_Utilisateurice.id = Compte.id where nom = %s",(nom_2,))
            id_2 = self.cur.fetchone()

        if id_1 == id_2 :
            print("/!\ Les deux comptes renseignés sont les mêmes. L'insertion n'est pas possible.\n")
        else :
            self.cur.execute("SELECT * FROM  Assos_Utilisateurice_utilisateurice where (ami_1 = %s and ami_2 = %s) or (ami_2 = %s and ami_1 = %s)", (id_1,id_2,id_1,id_2))
            data = self.cur.fetchone()

        if data :
            print("Cette relation existe déjà dans la base de donnée.")

        else :
            self.cur.execute("INSERT INTO Assos_Utilisateurice_Utilisateurice VALUES(%s,%s)", (id_1, id_2))
            print("Donnée insérée avec succès.")

    def consultation(self):
        self.cur.execute("SELECT * FROM Assos_Utilisateurice_Utilisateurice")
        h1, h2 = [i[0] for i in self.cur.description]
        print(h1 + " | " + h2)
        data = self.cur.fetchall()
        for compte_1, compte_2 in data:
            self.cur.execute("SELECT nom FROM Compte where id = %s", (compte_1,))
            nom_1 = self.cur.fetchone()[0]
            self.cur.execute("SELECT nom FROM Compte where id = %s", (compte_2,))
            nom_2 = self.cur.fetchone()[0]
            print(nom_1 + " | " + nom_2)

    def suppression(self):
        print("Suppression d'un lien d'amitié entre deux utilisateur•ice•s.")
        nom_1 = input("Nom du premièr compte : ")
        self.cur.execute("SELECT Compte.id from Compte JOIN Profil_Utilisateurice ON Profil_Utilisateurice.id = Compte.id where nom = %s",(nom_1,))
        id_1 = self.cur.fetchone()

        while not id_1:
            print("/!\ Le nom de compte renseigné n'appartient pas à la base de donnée ou n'est pas calui d'un•e utilisateur•ice.\n")
            nom = input("Nom du premièr compte : ")
            self.cur.execute("SELECT Compte.id from Compte JOIN Profil_Utilisateurice ON Profil_Utilisateurice.id = Compte.id where nom = %s",(nom_1,))
            id_1 = self.cur.fetchone()

        nom_2 = input("Nom du deuxième compte : ")
        self.cur.execute("SELECT Compte.id from Compte JOIN Profil_Utilisateurice ON Profil_Utilisateurice.id = Compte.id where nom = %s",(nom_2,))
        id_2 = self.cur.fetchone()

        while not id_2:
            print("/!\ Le nom de compte renseigné n'appartient pas à la base de donnée ou n'est pas calui d'un•e utilisateur•ice.\n")
            nom_2 = input("Nom du deuxième compte : ")
            self.cur.execute("SELECT Compte.id from Compte JOIN Profil_Utilisateurice ON Profil_Utilisateurice.id = Compte.id where nom = %s",(nom_2,))
            id_2 = self.cur.fetchone()

        if id_1 == id_2:
            print("/!\ Les deux comptes renseignés sont les mêmes. La suppression n'est pas possible.\n")
        else:
            self.cur.execute("SELECT * FROM  Assos_Utilisateurice_utilisateurice where (ami_1 = %s and ami_2 = %s) or (ami_2 = %s and ami_1 = %s)",(id_1, id_2, id_1, id_2))
            data = self.cur.fetchone()

        if not data:
            print("Cette relation n'existe pas.")

        else:
            self.cur.execute("DELETE FROM Assos_Utilisateurice_Utilisateurice Where ami_1 = %s and ami_2=%s", (id_1, id_2))
            self.cur.execute("DELETE FROM Assos_Utilisateurice_Utilisateurice Where ami_1 = %s and ami_2=%s", (id_2, id_1))
            print("Donnée supprimée avec succès.")

    def modification(self):
        pass


class Chanson() :
    def __init__(self, cur):
        self.cur = cur

    def insertion(self):
        artiste = input("Interprète de la chanson : ")
        self.cur.execute("SELECT Profil_Artiste.id from Profil_Artiste JOIN Compte ON Profil_Artiste.id = Compte.id where nom = %s",(artiste,))
        art = self.cur.fetchone()

        while not art:
            print("/!\ Le nom d'artiste renseigné n'appartient pas à la base de donnée.\n")
            artiste = input("Interprète de la chanson : ")
            self.cur.execute("SELECT Profil_Artiste.id from Profil_Artiste JOIN Compte ON Profil_Artiste.id = Compte.id where nom = %s",(artiste,))
            art = self.cur.fetchone()

        titre = input("Titre de la chanson : ")
        self.cur.execute("SELECT * from Chanson JOIN Profil_Artiste ON Chanson.createurice = Profil_Artiste.id JOIN Compte ON Profil_Artiste.id = Compte.id where Compte.nom = %s and Chanson.titre=%s ",(artiste, titre))
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

        titre = input("Titre de la chanson à supprimer : ")
        artiste = input("Nom de l'artiste de la chanson à supprimer : ")
        self.cur.execute("SELECT Profil_Artiste.id from Profil_Artiste JOIN Compte ON Profil_Artiste.id = Compte.id where nom = %s",(artiste,))
        art = self.cur.fetchone()

        while not art:
            print("/!\ Le nom d'artiste renseigné n'appartient pas à la base de donnée.\n")
            artiste = input("Nom de l'artiste de la chanson à supprimer : ")
            self.cur.execute("SELECT Profil_Artiste.id from Profil_Artiste JOIN Compte ON Profil_Artiste.id = Compte.id where nom = %s",(artiste,))
            art = self.cur.fetchone()

        self.cur.execute("SELECT Chanson.id from Chanson JOIN Profil_Artiste ON Chanson.createurice = Profil_Artiste.id  where Profil_Artiste.id = %s and Chanson.titre=%s ",(art[0], titre))
        chanson = self.cur.fetchone()

        if not chanson:
            print("L'artiste ne possède aucune chanson ayant ce nom pour titre.")
        else :
            self.cur.execute("DELETE FROM Assos_Playlist_Chanson WHERE chanson = %s " ,(chanson[0],))
            self.cur.execute("DELETE FROM DroitsAuteurs WHERE chanson = %s ",(chanson[0],))
            self.cur.execute("DELETE FROM Chanson WHERE createurice = %s AND titre=%s ", (art[0],titre))
            print("Donnée supprimée avec succès.")

    def modification(self):
        pass


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
            self.cur.execute("SELECT Profil_Artiste.id from Profil_Artiste JOIN Compte ON Profil_Artiste.id = Compte.id where nom = %s",(artiste,))
            art = self.cur.fetchone()

        titre = input("Titre de l'album : ")
        self.cur.execute("SELECT * from Album JOIN Profil_Artiste ON Album.artiste_principal = Profil_Artiste.id JOIN Compte ON Profil_Artiste.id = Compte.id where Compte.nom = %s and Album.titre=%s ",(artiste, titre))
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
        titre = input("Titre de l'album à supprimer : ")
        artiste = input("Nom de l'artiste principal•e de l'album à supprimer : ")
        self.cur.execute("SELECT Profil_Artiste.id from Profil_Artiste JOIN Compte ON Profil_Artiste.id = Compte.id where nom = %s",(artiste,))
        art = self.cur.fetchone()

        while not art:
            print("/!\ Le nom d'artiste renseigné n'appartient pas à la base de donnée.\n")
            artiste = input("Nom de l'artiste principal•e de l'album à supprimer : ")
            self.cur.execute("SELECT Profil_Artiste.id from Profil_Artiste JOIN Compte ON Profil_Artiste.id = Compte.id where nom = %s",(artiste,))
            art = self.cur.fetchone()

        self.cur.execute("SELECT Album.id from Album JOIN Profil_Artiste ON Album.artiste_principal = Profil_Artiste.id where Profil_Artiste.id= %s and Album.titre=%s ",(art[0], titre))
        album = self.cur.fetchone()

        if not album:
            print("L'artiste ne possède aucune album ayant ce nom pour titre.")
        else :
            self.cur.execute("DELETE FROM Assos_Playlist_Album WHERE id_Album =%s", (album[0],))
            self.cur.execute("DELETE FROM Chanson WHERE album =%s", (album[0],))
            self.cur.execute("DELETE FROM Album WHERE artiste_principal =%s AND titre=%s ", (art[0], titre))
            print("Donnée supprimée avec succès.")

    def modification(self):
        pass

class GenresMusicaux :
    def __init__(self, cur):
        self.cur = cur

    def insertion(self):
        genre = input("Genre musical à ajoutez : ")
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
        genre = input("Genre musical à supprimer : ")
        self.cur.execute("SELECT * from GenresMusicaux where nom = %s", (genre,))
        data = self.cur.fetchone()

        while not data :
            print("/!\ Le genre musical renseigné n'appartient pas à la base de donnée.\n")
            genre = input("Genre musical à supprimer : ")
            self.cur.execute("SELECT * from GenresMusicaux where nom = %s", (genre,))
            data = self.cur.fetchone()

        self.cur.execute("DELETE FROM Assos_Utilisateurice_GenresMusicaux WHERE genre =%s",(genre,))
        self.cur.execute("DELETE FROM Assos_Playlist_Chanson WHERE chanson IN (SELECT id FROM Chanson WHERE genre_musical =%s)", (genre,))
        self.cur.execute("DELETE FROM Chanson WHERE genre_musical =%s", (genre,))
        self.cur.execute("DELETE FROM GenresMusicaux WHERE nom=%s ", (genre,))
        print("Donnée suppprimée avec succès.")

    def modification(self):
        nom = input("Nom du genre musical à modifier : ")
        self.cur.execute("SELECT * from GenresMusicaux where nom = '%s' " % (nom))
        genre = self.cur.fetchone()

        while not genre:
            print(f"/!\ Le genre musical renseigné n'appartient pas à la base de donnée.\n")
            nom = input("Nom du genre musical à modifier : ")
            self.cur.execute("SELECT * from GenresMusicaux where nom = '%s' " % (nom))
            genre = self.cur.fetchone()

        new = input("Nouveau nom du genre musical : ")
        self.cur.execute("SELECT * from GenresMusicaux where nom = %s", (new,))
        data = self.cur.fetchone()
        if data:
            print("Un genre musical possède déjà ce nom. La modification n'est pas possible.")
        else:
            self.cur.execute("INSERT INTO GenresMusicaux VALUES (%s)", (new,))
            self.cur.execute("UPDATE Chanson set genre_musical = %s WHERE genre_musical = %s", (new, genre))
            self.cur.execute("UPDATE Assos_Utilisateurice_GenresMusicaux set genre = %s WHERE genre = %s", (new, genre))
            self.cur.execute("DELETE from GenresMusicaux where nom= %s", (genre,))
            print("Donnée modifié avec succès.")

class Playlist():
    def __init__(self,cur):
        self.cur = cur

    def insertion(self):
        titre = input("Titre de la playlist : ")
        compte = input("Compte dupuis lequel créer la playlist : ")
        self.cur.execute("SELECT id from Compte where nom = %s",(compte,))
        cre = self.cur.fetchone()

        while not cre :
            print("/!\ Le compte renseigné n'appartient pas à la base de donnée.\n")
            compte = input("Compte dupuis lequel créer la playlist :")
            self.cur.execute("SELECT id from Compte where nom = %s", (compte,))
            cre = self.cur.fetchone()

        self.cur.execute("SELECT * from Playlist  where createurice = %s and titre=%s ",(cre, titre))
        data = self.cur.fetchone()

        if data:
            print("/!\ Le compte possède dèjà une playlist du même nom.\n")

        else:
            des = input("Description de la playlist : ")
            aut = input("Paramètre d'autorisation de la playlist (privee/publique/partagee_aux_amies) : ")
            while aut not in ['privee', 'publique','partagee_aux_amies'] :
                print("/!\ Le paramètre d'autorisation de la playlist n'est pas valide.\n")
                aut = input("Paramètre d'autorisation de la playlist (privee/publique/partagee_aux_amies) : ")

            self.cur.execute("INSERT INTO Playlist VALUES(DEFAULT,%s,%s,%s,%s)", (titre, des, aut, cre))
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
        nom = input("Nom de le•a createur•ice de la playlist : ")
        self.cur.execute("SELECT id from Compte where Compte.nom='%s' "%(nom))
        cre = self.cur.fetchone()

        while not cre:
            print("/!\ Le compte renseigné n'appartient pas à la base de donnée.\n")
            nom = input("Nom de le•a createur•ice de la playlist : ")
            self.cur.execute("SELECT id from Compte where Compte.nom='%s' " % (nom))
            cre = self.cur.fetchone()

        self.cur.execute("SELECT id from Playlist where createurice=%s AND titre=%s", (cre, titre))
        playlist = self.cur.fetchone()

        if not playlist :
            print("/!\ Le profil ne possède aucune playlist ayant ce nom pour titre.\n")

        else :
            self.cur.execute("DELETE FROM Assos_Playlist_Album WHERE id_Playlist= %s", (playlist,))
            self.cur.execute("DELETE FROM Assos_Playlist_Chanson WHERE playlist =%s", (playlist,))
            self.cur.execute("DELETE FROM Playlist WHERE id='%s' "%(playlist,))
            print("Donnée supprimée avec succès.")


    def modification(self):

        titre = input("Titre de la playlist à modifier : ")
        compte = input("Compte dupuis lequel modifier la playlist : ")
        self.cur.execute("SELECT id from Compte where nom = %s", (compte,))
        cre = self.cur.fetchone()

        while not cre:
            print("/!\ Le compte renseigné n'appartient pas à la base de donnée.\n")
            compte = input("Compte dupuis lequel modifier la playlist : ")
            self.cur.execute("SELECT id from Compte where nom = %s", (compte,))
            cre = self.cur.fetchone()

        self.cur.execute("SELECT id from Playlist where createurice=%s AND titre=%s", (cre, titre))
        playlist = self.cur.fetchone()

        if not playlist:
            print("/!\ Le profil ne possède aucune playlist ayant ce nom pour titre.\n")

        else :
            self.cur.execute("SELECT description, autorisation_acces FROM Playlist where id = %s", (playlist[0],))
            des, aut = self.cur.fetchone()
            print("Les modifications enregistrées ci-dessous seront prises en compte, si aucune donnée n'est insérée pour un attribut, la valeur restera inchangée.\n")

            t = input("Titre de la playlist : ")
            if t == '' :
                t = titre

            c = input("Créateur•ice de la playlist : ")
            self.cur.execute("SELECT id from Compte where nom = %s", (c,))
            c_ = self.cur.fetchone()

            while c != '' and not c_:
                print("/!\ Le compte renseigné n'appartient pas à la base de donné.\n")
                c = input("Créateur•ice de la playlist : ")
                self.cur.execute("SELECT id from Compte where nom = %s", (c,))
                c_ = self.cur.fetchone()

            if c == '':
                c_ = cre

            if t != titre or c_ != cre :
                self.cur.execute("SELECT * FROM Playlist where createurice = %s and titre = %s", (c_,t))
                data = self.cur.fetchone()

                if data:
                    print("/!\ Le compte possède dèjà une playlist du même nom.\n")
                    return

            d = input("Description de la playlist : ")
            if d == '' :
                d = des

            a = input("Paramètre d'autorisation de la playlist (privee/publique/partagee_aux_amies) : ")

            while a not in ['privee', 'publique', 'partagee_aux_amies', '']:
                print("/!\ Le paramètre d'autorisation de la playlist n'est pas valide.\n")
                a = input("Paramètre d'autorisation de la playlist (privee/publique/partagee_aux_amies) : ")

            if a == '':
                a = aut

            self.cur.execute("UPDATE Playlist set titre = %s, createurice = %s, description = %s, autorisation_acces = %s where id = %s", (t,c_,d,a, playlist))
            print("Donnée modifiée avec succès.")

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
        nom = input("Nom du pays à supprimer : ")
        self.cur.execute("SELECT * from Pays where nom = '%s' "%(nom))
        pays = self.cur.fetchone()

        while not pays :
            print(f"/!\ Le pays renseigné n'appartient pas à la base de donnée.\n")
            nom = input("Nom du pays à supprimer : ")
            self.cur.execute("SELECT * from Pays where nom = '%s' " % (nom))
            pays = self.cur.fetchone()

        self.cur.execute("DELETE FROM Assos_Playlist_Album WHERE id_Album IN (SELECT id from Album where artiste_principal IN (SELECT id from Profil_Artiste where pays = '%s')) " % (pays))
        self.cur.execute("DELETE FROM Assos_Playlist_chanson WHERE chanson IN (SELECT id from Chanson where createurice IN (SELECT id from Profil_Artiste where pays = '%s')) " % (pays))
        self.cur.execute("DELETE FROM DroitsAuteurs WHERE compte IN (SELECT id from Profil_Artiste where pays = '%s') " % (pays))
        self.cur.execute("DELETE FROM Chanson WHERE createurice IN (SELECT id from Profil_Artiste where pays = '%s') " % (pays))
        self.cur.execute("DELETE FROM Album WHERE artiste_principal IN (SELECT id from Profil_Artiste where pays = '%s') " % (pays))

        self.cur.execute("SELECT id FROM Profil_Artiste WHERE pays = '%s' " % (pays))
        artists = self.cur.fetchall()
        self.cur.execute("DELETE FROM Profil_Artiste WHERE pays = '%s' " % (pays))

        for artist in artists :
            self.cur.execute("DELETE FROM Compte WHERE id = %s " % (artist))

        self.cur.execute("DELETE FROM Pays WHERE nom='%s' " % (pays))
        print("Donnée supprimée avec succès.\n")

    def modification(self):

        nom = input("Nom du pays à modifier : ")
        self.cur.execute("SELECT * from Pays where nom = '%s' " % (nom))
        pays = self.cur.fetchone()

        while not pays:
            print(f"/!\ Le pays renseigné n'appartient pas à la base de donnée.\n")
            nom = input("Nom du pays à supprimer : ")
            self.cur.execute("SELECT * from Pays where nom = '%s' " % (nom))
            pays = self.cur.fetchone()

        new = input("Nouveau nom de pays : ")
        self.cur.execute("SELECT * from Pays where nom = %s", (new,))
        data = self.cur.fetchone()
        if data:
            print("Un pays possède déjà ce nom. La modification n'est pas possible.")
        else:
            self.cur.execute("INSERT INTO PAYS VALUES (%s)", (new,))
            self.cur.execute("UPDATE Profil_Artiste set pays = %s WHERE pays = %s",(new, pays))
            self.cur.execute("DELETE from Pays where nom= %s", (pays,))
            print("Donnée modifié avec succès.")


class Assos_Playlist_Chanson():
    def __init__(self, cur):
        self.cur = cur

    def insertion(self):
        playlist = input("Quel est le nom de la playlist ? ")
        utilisateurice = input("Quel est le nom de l'auteurice  de la playlist ? ")
        chanson = input("Quel est le nom de la chanson à ajouter ? ")
        artiste = input("Quel est le nom de l'auteurice de la chanson à ajouter ? ")
        self.cur.execute("SELECT * FROM playlist WHERE titre= '%s' AND createurice IN (SELECT id FROM Compte WHERE nom='%s') " % (playlist, utilisateurice))
        data = self.cur.fetchone()
        if not data:
            print(f"La playlist {playlist} par {utilisateurice} n'existe pas.")
        else :
            self.cur.execute("SELECT * FROM chanson WHERE titre='%s' AND createurice IN (SELECT id FROM Compte WHERE nom='%s') " % (chanson, artiste))
            data = self.cur.fetchone()
            if not data:
                print(f"La chanson {chanson} par {artiste} n'existe pas.")
            else :
                self.cur.execute("SELECT * from Assos_Playlist_Chanson WHERE playlist IN (SELECT id FROM playlist WHERE titre= '%s' AND createurice IN (SELECT id FROM Compte WHERE nom='%s')) AND chanson IN (SELECT id FROM chanson WHERE titre='%s' AND createurice IN (SELECT id FROM Compte WHERE nom='%s')) " %(playlist, utilisateurice, chanson, artiste ))
                data = self.cur.fetchone()
                if data:
                    print("Cette donnée est déjà présente dans la base de donnée.")
                else:
                    self.cur.execute("INSERT INTO Assos_Playlist_Chanson(playlist, chanson) VALUES((SELECT id FROM playlist WHERE titre= '%s' AND createurice IN (SELECT id FROM Compte WHERE nom='%s')),(SELECT id FROM chanson WHERE titre='%s' AND createurice IN (SELECT id FROM Compte WHERE nom='%s')));"%(playlist, utilisateurice, chanson, artiste ))
                    print("Donnée insérée avec succès.")

    def consultation(self):
        self.cur.execute("SELECT * FROM Assos_Playlist_Chanson")
        headers = [i[0] for i in self.cur.description]
        print(headers)
        data = self.cur.fetchall()
        for row in data:
            self.cur.execute("SELECT titre FROM Chanson where id='%s' "%(row[0]))
            chanson_a_afficher = self.cur.fetchall()
            self.cur.execute("SELECT titre FROM Playlist where id='%s' " % (row[0]))
            playlist_a_afficher = self.cur.fetchall()
            print(f"{chanson_a_afficher} - {playlist_a_afficher}")

    def suppression(self):
        nom = input("Nom du pays à supprimer : ")
        self.cur.execute("SELECT * from Pays where nom = '%s' "%(nom))
        pays = self.cur.fetchone()

        while not pays :
            print(f"/!\ Le pays renseigné n'appartient pas à la base de donnée.\n")
            nom = input("Nom du pays à supprimer : ")
            self.cur.execute("SELECT * from Pays where nom = '%s' " % (nom))
            pays = self.cur.fetchone()

        self.cur.execute("DELETE FROM Assos_Playlist_Album WHERE id_Album IN (SELECT id from Album where artiste_principal IN (SELECT id from Profil_Artiste where pays = '%s')) " % (pays))
        self.cur.execute("DELETE FROM Assos_Playlist_chanson WHERE chanson IN (SELECT id from Chanson where createurice IN (SELECT id from Profil_Artiste where pays = '%s')) " % (pays))
        self.cur.execute("DELETE FROM DroitsAuteurs WHERE compte IN (SELECT id from Profil_Artiste where pays = '%s') " % (pays))
        self.cur.execute("DELETE FROM Chanson WHERE createurice IN (SELECT id from Profil_Artiste where pays = '%s') " % (pays))
        self.cur.execute("DELETE FROM Album WHERE artiste_principal IN (SELECT id from Profil_Artiste where pays = '%s') " % (pays))

        self.cur.execute("SELECT id FROM Profil_Artiste WHERE pays = '%s' " % (pays))
        artists = self.cur.fetchall()
        self.cur.execute("DELETE FROM Profil_Artiste WHERE pays = '%s' " % (pays))

        for artist in artists :
            self.cur.execute("DELETE FROM Compte WHERE id = %s " % (artist))

        self.cur.execute("DELETE FROM Pays WHERE nom='%s' " % (pays))
        print("Donnée supprimée avec succès.\n")

    def modification(self):

        nom = input("Nom du pays à modifier : ")
        self.cur.execute("SELECT * from Pays where nom = '%s' " % (nom))
        pays = self.cur.fetchone()

        while not pays:
            print(f"/!\ Le pays renseigné n'appartient pas à la base de donnée.\n")
            nom = input("Nom du pays à supprimer : ")
            self.cur.execute("SELECT * from Pays where nom = '%s' " % (nom))
            pays = self.cur.fetchone()

        new = input("Nouveau nom de pays : ")
        self.cur.execute("SELECT * from Pays where nom = %s", (new,))
        data = self.cur.fetchone()
        if data:
            print("Un pays possède déjà ce nom. La modification n'est pas possible.")
        else:
            self.cur.execute("INSERT INTO PAYS VALUES (%s)", (new,))
            self.cur.execute("UPDATE Profil_Artiste set pays = %s WHERE pays = %s",(new, pays))
            self.cur.execute("DELETE from Pays where nom= %s", (pays,))
            print("Donnée modifié avec succès.")


class Droits():
    def __init__(self,cur):
        self.cur = cur

    def insertion(self):

        titre = input("Titre de la chanson à laquelle ajouter des droits d'auteurs : ")
        artiste = input("Interprète de la chanson : ")
        self.cur.execute(
            "SELECT Profil_Artiste.id from Profil_Artiste JOIN Compte ON Profil_Artiste.id = Compte.id where nom = %s",
            (artiste,))
        art = self.cur.fetchone()

        while not art:
            print("/!\ Le nom d'artiste renseigné n'appartient pas à la base de donnée.\n")
            artiste = input("Interprète de la chanson : ")
            self.cur.execute("SELECT Profil_Artiste.id from Profil_Artiste JOIN Compte ON Profil_Artiste.id = Compte.id where nom = %s",(artiste,))
            art = self.cur.fetchone()

        self.cur.execute("SELECT Chanson.id from Chanson JOIN Profil_Artiste ON Chanson.createurice = Profil_Artiste.id  where Profil_Artiste.id = %s and Chanson.titre=%s ",(art[0], titre))
        chanson = self.cur.fetchone()

        if not chanson:
            print("L'artiste n'interprète aucune chanson ayant ce nom pour titre.")
        else :
            compte = input("Compte ayant travaillé sur la chanson : ")
            self.cur.execute("SELECT Compte.id from Compte Join Profil_Artiste on Compte.id = Profil_Artiste.id where nom = %s", (compte,))
            cre = self.cur.fetchone()

            while not cre:
                print("/!\ Le compte renseigné n'appartient pas à la base de donnée ou n'est pas celui d'un artiste.\n")
                compte = input("Compte depuis lequel insérer des droits d'auteurs : ")
                self.cur.execute("SELECT Compte.id from Compte Join Profil_Artiste on Compte.id = Profil_Artiste.id where nom = %s", (compte,))
                cre = self.cur.fetchone()

            metier = input("Sous quel activité (editeur/compositeur/auteur) : ")
            while metier not in ['auteur', 'editeur', 'compositeur']:
                print("/!\ L'activité renseignée n'est pas valide.\n")

            self.cur.execute("SELECT * from DroitsAuteurs where metier = %s and compte = %s and chanson =%s", (metier, cre, chanson))
            data = self.cur.fetchone()

            if data :
                print(f"Ce compte est déjà crédité sur cette chanson sur ce métier là.")

            else :
                self.cur.execute("INSERT INTO DroitsAuteurs Values (%s,%s,%s)", (metier, cre, chanson))
                print("Donnée insérée avec succès.")

    def suppression(self):

        titre = input("Titre de la chanson pour laquelle supprimer des droits d'auteurs : ")
        artiste = input("Interprète de la chanson : ")
        self.cur.execute("SELECT Profil_Artiste.id from Profil_Artiste JOIN Compte ON Profil_Artiste.id = Compte.id where nom = %s",(artiste,))
        art = self.cur.fetchone()

        while not art:
            print("/!\ Le nom d'artiste renseigné n'appartient pas à la base de donnée.\n")
            artiste = input("Interprète de la chanson : ")
            self.cur.execute(
                "SELECT Profil_Artiste.id from Profil_Artiste JOIN Compte ON Profil_Artiste.id = Compte.id where nom = %s",
                (artiste,))
            art = self.cur.fetchone()

        self.cur.execute("SELECT Chanson.id from Chanson JOIN Profil_Artiste ON Chanson.createurice = Profil_Artiste.id  where Profil_Artiste.id = %s and Chanson.titre=%s ",(art[0], titre))
        chanson = self.cur.fetchone()

        if not chanson:
            print("L'artiste n'interprète aucune chanson ayant ce nom pour titre.")
        else:
            compte = input("Compte ayant travaillé sur la chanson : ")
            self.cur.execute("SELECT Compte.id from Compte Join Profil_Artiste on Compte.id = Profil_Artiste.id where nom = %s", (compte,))
            cre = self.cur.fetchone()

            while not cre:
                print("/!\ Le compte renseigné n'appartient pas à la base de donnée ou n'est pas celui d'un artiste.\n")
                compte = input("Compte depuis lequel insérer des droits d'auteurs : ")
                self.cur.execute(
                    "SELECT Compte.id from Compte Join Profil_Artiste on Compte.id = Profil_Artiste.id where nom = %s",
                    (compte,))
                cre = self.cur.fetchone()

            metier = input("Sous quel activité (editeur/compositeur/auteur) : ")
            while metier not in ['auteur', 'editeur', 'compositeur']:
                print("/!\ L'activité renseignée n'est pas valide.\n")

            self.cur.execute("SELECT * from DroitsAuteurs where metier = %s and compte = %s and chanson =%s",(metier, cre, chanson))
            data = self.cur.fetchone()

            if not data:
                print(f"Les crédits de cette chanson n'existe pas. La suppression n'est pas possible.")

            else:
                self.cur.execute("DELETE FROM DroitsAuteurs where metier = %s and compte = %s and chanson = %s ", (metier, cre, chanson))
                print("Donnée supprimée avec succès.")

    def consultation(self):
        self.cur.execute("SELECT * FROM DroitsAuteurs")
        headers = [i[0] for i in self.cur.description]
        print(headers)
        data = self.cur.fetchall()
        for row in data:
            self.cur.execute("SELECT nom FROM Compte where id='%s' " % (row[1]))
            compte = self.cur.fetchone()
            self.cur.execute("SELECT titre FROM Chanson where id='%s' " % (row[2]))
            chanson = self.cur.fetchone()
            print(row[0] +' | ' + compte[0] + ' | '+ chanson[0])

    def modification(self):
        print("La modification n'est pas disponible pour cette table. Si une information a changé merci de la supprimer puis d'inserer les nouvelles données.")

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
    cur.execute(open("Assos_Utilisateurice_GenresMusicaux/Assos_Utilisateurice_GenresMusicaux_TABLE.sql", "r").read())
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
    cur.execute(open("Assos_Utilisateurice_GenresMusicaux/Assos_Utilisateurice_GenresMusicaux_DATA.sql", "r").read())
    cur.execute(open("DroitsAuteurs/DroitsAuteurs_DATA.sql", "r").read())

def suppression_bdd(cur):
    cur.execute(open("Assos_Playlist_Album/Assos_Playlist_Album_DELETE.sql", "r").read())
    cur.execute(open("Assos_Playlist_Chanson/Assos_Playlist_Chanson_DELETE.sql", "r").read())
    cur.execute(open("Assos_Utilisateurice_Utilisateurice/Assos_Utilisateurice_Utilisateurice_DELETE.sql", "r").read())
    cur.execute(open("Assos_Utilisateurice_GenresMusicaux/Assos_Utilisateurice_GenresMusicaux_DELETE.sql", "r").read())
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
    elif table == 'b':
        Chanson(cur).insertion()
    elif table == 'c':
        Album(cur).insertion()
    elif table == 'd':
        GenresMusicaux(cur).insertion()
    elif table == 'e':
        Playlist(cur).insertion()
    elif table == 'f':
        Pays(cur).insertion()
    elif table == 'g':
        Amitie(cur).insertion()
    elif table == 'h':
        Assos_Playlist_Chanson(cur).insertion()

    elif table == 'j':
        Droits(cur).insertion()

def modification(cur, table):
    if table == 'a':
        Compte(cur).modification()
    if table == 'b':
        Chanson(cur).modification()
    if table == 'c':
        Album(cur).modification()
    if table == 'd':
        GenresMusicaux(cur).modification()
    if table == 'e':
        Playlist(cur).modification()
    if table == 'f':
        Pays(cur).modification()
    if table == 'g':
        Amitie(cur).modification()
    if table == 'h':
        Assos_Playlist_Chanson(cur).modification()


    elif table == 'j':
        Droits(cur).modification

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
    if table == 'g':
        Amitie(cur).suppression()
    if table == 'h':
        Assos_Playlist_Chanson(cur).suppression()


    elif table == 'j':
        Droits(cur).suppression()

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
    if table == 'g':
        Amitie(cur).consultation()
    if table == 'h':
        Assos_Playlist_Chanson(cur).consultation()

    elif table == 'j':
        Droits(cur).consultation()

def requete(cur, req) :
    if req == 'a':
        duree_moyenne(cur)
    if req == 'b':
        artistes_prolifiques(cur)
    if req == 'c':
        chansons_longues(cur)
    if req == 'd':
        genre_prefere(cur)

def chansons_longues(cur):
    cur.execute(open("Interrogation/Artistes_chansons_longues.sql", "r").read())
    # Fetch data line by line
    print("Artiste")
    print('_______')
    raw = cur.fetchone()
    while raw:
        print(raw[0])
        raw = cur.fetchone()

def artistes_prolifiques(cur):
    cur.execute(open("Interrogation/Artistes_Prolifiques.sql", "r").read())
    # Fetch data line by line
    print("Artiste | Nombre de chansons")
    print('_______')
    raw = cur.fetchone()
    while raw:
        print(raw[0] + " | " + str(raw[1]))
        raw = cur.fetchone()

def duree_moyenne(cur):
    cur.execute(open("Interrogation/duree_moyenne_artiste.sql", "r").read())
    # Fetch data line by line
    print("Artiste | Durée moyenne de ses chansons")
    print('_______')
    raw = cur.fetchone()
    while raw:
        print(raw[0] + " | " + str(raw[1]))
        raw = cur.fetchone()

def genre_prefere(cur):
    cur.execute(open("Interrogation/genre_prefere_utilisateurice.sql", "r").read())
    print("Genre Musical | Nombre d'amateurice")
    print('_______')
    # Fetch data line by line
    raw = cur.fetchone()
    if raw :
        while raw:
            print(raw[0] + ' | '+  str(raw[1]))
            raw = cur.fetchone()

def main():
    try:
        print("\nBienvenue dans le programme d'accès à votre base de donnée de streaming musical !")
        type_connexion='z'
        while type_connexion != 'o' and type_connexion != 'n' :
            type_connexion=input("Souhaitez vous utiliser des identifiants personnalisés ? o/n : ")
        identifiants = Connexion()

        if type_connexion =='o':
            identifiants.HOST=input("Entrez le nom du serveur (HOST) : ")
            identifiants.USER = input("Entrez votre nom d'utilisteurice (USER) : ")
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

        while '1' <= choice <= '5':
            print("__________________________________________________")
            print("Pour effectuer une insertion dans la base de donnée, entrez 1")
            print("Pour effectuer une modification dans la base de donnée, entrez 2")
            print("Pour effectuer une suppression dans la base de donnée, entrez 3")
            print("Pour effectuer une consultation dans la base de donnée, entrez 4")
            print("Pour effectuer une requête spéciale, entrez 5")
            print("Pour quitter, entrez n'importe quel autre charactère")
            print("__________________________________________________")

            choice = input("Votre choix : ")
            if '1' <= choice <= '4':
                table = 'z'
                print("\nChoisissez la table concernée : Compte(a), Chanson(b), Album(c), GenreMusicaux(d), Playlist(e), Pays(f), Amitié(g), Chansons dans playlist(h), Droit d'auteurs (j) ")
                table = input("Table : ")
                print("-----\n")

                while 'a' <= table <= 'j':
                    if choice == '1':
                        insertion(cur, table)
                    if choice == '2':
                        modification(cur, table)
                    if choice == '3':
                        suppression(cur,table)
                    if choice == '4':
                        consultation(cur,table)
                    table = 'z'

            if choice == '5' :
                print("Pour afficher la durée moyenne des chansons de chaque artiste (plus de 5 chansons), entrez a")
                print("Pour afficher les 10 artistes les plus prolifiques de la base de donnée, entrez b")
                print("Pour afficher les artistes ayant les chansons les plus longues (> 10 min), entrez c")
                print("Pour afficher les 10 genres musicaux préférés des utilisateur•ice•s, entrez d")
                req = input("Requête : ")
                print("-----\n")

                while 'a' <= req <= 'd':
                    requete(cur, req)
                    req = 'z'

        conn.close()

    except Exception as error :
        print("Une erreur s'est produite : ", error)
        print("Type d'exception : ", type(error))


if __name__ == '__main__':
    main()