import psycopg2
from datetime import date

from postgres import DATABASE, PASSWORD

HOST = "localhost"
USER = "postgres"

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
        nom = input("Identifiant du compte à ajouter : ")
        cur.execute("SELECT * from Compte where nom = %s", (nom,))
        data = cur.fetchone()
        if data:
            print("/!\ L'identifiant renseigné est déjà utilisé.\n")
        else:
            type = input("Type du compte à ajouter (utilisateurice/artiste) : ")
            while type not in ['utilisateurice', 'artiste']:
                print("/!\ Le type de compte renseigné n'est pas valide.\n")
                type = input("Type du compte à ajouter (utilisateurice/artiste) : ")

            cur.execute("INSERT INTO Compte(nom) VALUES (%s)", (nom,))
            cur.execute("SELECT id from Compte where nom = %s", (nom,))
            id = cur.fetchone()

            if type == "utilisateurice":
                mail = input("Mail : ")
                mdp = input("Mot de passe : ")
                statut = input("Statut (premium/regulier) : ")

                while statut not in ['premium', 'regulier'] :
                    print("/!\ Le statut renseigné n'est pas valide.\n")
                    statut = input("Statut (premium/regulier) : ")

                cur.execute("INSERT INTO Profil_Utilisateurice VALUES(%s,%s,%s,%s,%s)", (id,mail,mdp,date.today(), statut))
                print("Donnée insérée avec succès.")

            if type == "artiste":
                bio = input("Biographie : ")
                p = input("Pays : ")
                cur.execute("SELECT * from Pays where nom = %s", (p,))
                pays = cur.fetchone()
                while not pays :
                    print("/!\ Le pays renseigné n'appartient pas à la base de donnée.\n")
                    p = input("Pays : ")
                    cur.execute("SELECT * from Pays where nom = %s", (p,))
                    pays = cur.fetchone()

                type = input("Type (artiste/solo/groupe) : ")
                while type not in ['artiste', 'solo', 'groupe']:
                    print("/!\ Le type renseigné n'est pas valide.\n")
                    type = input("Type (artiste/solo/groupe) : ")

                if type == 'artiste' or type == 'groupe' :
                    type = 'Profil_' + type.capitalize()
                    cur.execute("INSERT INTO Profil_Artiste VALUES(%s,%s,%s,NULL,%s)", (id,bio,type,pays))
                    print("Donnée insérée avec succès.")

                if type == 'solo':
                    type = 'Profil_Artiste_Solo'
                    g = input("L'artiste appartient également à un groupe (y/n) : ")

                    while g not in ['y', 'n']:
                        print("/!\ La réponse à la question n'est pas valide.\n")
                        g = input("L'artiste appartient également à un groupe (y/n) : ")

                    if g == 'n' :
                        cur.execute("INSERT INTO Profil_Artiste VALUES(%s,%s,%s,NULL,%s)", (id, bio, type, pays))
                        print("Donnée insérée avec succès.")

                    else :
                        gr = input("Nom du groupe : ")
                        cur.execute("SELECT type,id from Profil_Artiste where id = (SELECT id from Compte where nom = %s)",(gr,))
                        data = cur.fetchone()
                        while not data or (data and data[0] != 'Profil_Groupe' ):
                            print("/!\ Le nom de groupe renseigné n'appartient pas à la base de donnée ou ne correspond pas au profil d'un groupe. \n")
                            gr = input("Nom du groupe : ")
                            cur.execute("SELECT type,id from Profil_Artiste where id = (SELECT id from Compte where nom = %s)",(gr,))
                            data = cur.fetchone()

                        cur.execute("INSERT INTO Profil_Artiste VALUES(%s,%s,%s,%s,%s)", (id, bio, type,data[1],pays))
                        print("Donnée insérée avec succès.")

    if table == 'b':
        artiste = input("Interprète de la chanson : ")
        cur.execute("SELECT Profil_Artiste.id from Profil_Artiste JOIN Compte ON Profil_Artiste.id = Compte.id where nom = %s", (artiste,))
        art = cur.fetchone()

        while not art:
            print("/!\ Le nom d'artiste renseigné n'appartient pas à la base de donnée.\n")
            artiste = input("Interprète de la chanson : ")
            cur.execute("SELECT Profil_Artiste.id from Profil_Artiste JOIN Compte ON Profil_Artiste.id = Compte.id where nom = %s",(artiste,))
            art = cur.fetchone()

        titre = input("Titre de la chanson : ")
        cur.execute("SELECT * from Chanson JOIN Profil_Artiste ON Chanson.createurice = Profil_Artiste.id JOIN Compte ON Profil_Artiste.id = Compte.id where Compte.nom = %s and Chanson.titre=%s ",(artiste,titre))
        data = cur.fetchone()

        if data:
            print("/!\ L'artiste possède dèjà une chanson du même nom.\n")

        else :
            album = input("Album de la chanson : ")
            cur.execute("SELECT id, duree_totale from Album where titre = %s",(album,))
            alb = cur.fetchone()

            while not alb:
                print("/!\ Le nom d'album renseigné n'appartient pas à la base de donnée.\n")
                album = input("Album de la chanson : ")
                cur.execute("SELECT id, duree_totale from Album where titre = %s", (album,))
                alb = cur.fetchone()

            genre = input("Genre musical de la chanson : ")
            cur.execute("SELECT * from GenresMusicaux where nom = %s", (genre,))
            gen = cur.fetchone()

            while not gen:
                print("/!\ Le genre musical renseigné n'appartient pas à la base de donnée.\n")
                genre = input("Genre musical de la chanson : ")
                cur.execute("SELECT * from GenresMusicaux where nom = %s", (genre,))
                gen = cur.fetchone()

            duree = int(input("Durée de la chanson (en seconde): "))
            while duree < 0 :
                print("/!\ La durée renseignée n'est pas valide.\n")
                duree = input("Durée de la chanson (en seconde): ")

            cur.execute("INSERT INTO Chanson VALUES(DEFAULT,%s,%s,%s,%s,%s)", (titre, duree, alb[0], art[0], genre))
            cur.execute("UPDATE Album SET duree_totale = %s where id = %s", (int(alb[1]) + duree, alb[0]))
            print("Donnée insérée avec succès.")


    if table == 'c':
        artiste = input("Artiste principal de l'album : ")
        cur.execute("SELECT Profil_Artiste.id from Profil_Artiste JOIN Compte ON Profil_Artiste.id = Compte.id where nom = %s",(artiste,))
        art = cur.fetchone()

        while not art:
            print("/!\ Le nom d'artiste renseigné n'appartient pas à la base de donnée.\n")
            artiste = input("Artiste principal de l'album : ")
            cur.execute("SELECT Profil_Artiste.id from Profil_Artiste JOIN Compte ON Profil_Artiste.id = Compte.id where nom = %s",(artiste,))
            art = cur.fetchone()

        titre = input("Titre de l'album : ")
        cur.execute("SELECT * from Album JOIN Profil_Artiste ON Album.artiste_principal = Profil_Artiste.id JOIN Compte ON Profil_Artiste.id = Compte.id where Compte.nom = %s and Album.titre=%s ",(artiste, titre))
        data = cur.fetchone()

        if data:
            print("/!\ L'artiste possède dèjà un album du même nom.\n")

        else:
            annee = int(input("Année de sortie de l'album : "))
            while annee < 1900 or annee > date.today().year :
                print("/!\ L'année de sortie renseignée n'est pas valide.\n")
                annee = int(input("Année de sortie de l'album : "))

            ads = str(annee) + '-01-01'
            cur.execute("INSERT INTO Album VALUES(DEFAULT,%s,%s,%s,%s)", (titre, ads, 0, art[0]))
            print("Donnée insérée avec succès.")

    if table == 'd':
        genre = input("Quel genre musical souhaitez vous ajoutez ? ")
        cur.execute("SELECT * from GenresMusicaux where nom = %s", (genre,))
        data = cur.fetchone()
        if data:
            print("Cette donnée est déjà présente dans la base de donnée.")
        else :
            cur.execute("INSERT INTO GenresMusicaux(nom) VALUES (%s)", (genre,))
            print("Donnée insérée avec succès.")

    if table == 'e':
        pass
        #playlist

    if table == 'f':
        pays = input("Quel pays souhaitez vous ajoutez ? ")
        cur.execute("SELECT * from Pays where nom = %s", (pays,))
        data = cur.fetchone()
        if data:
            print("Cette donnée est déjà présente dans la base de donnée.")
        else:
            cur.execute("INSERT INTO Pays(nom) VALUES (%s)", (pays,))
            print("Donnée insérée avec succès.")

def modification(cur, table):
    pass

def suppression(cur, table):
    pass

def consultation(cur, table):
    if table == 'a':
        type = input("Quel type de compte souhaitez vous visualiser (utilisateurice/artiste/tous) ? ")
        if type == "utilisateurice":
            cur.execute("SELECT * FROM Compte JOIN Profil_Utilisateurice on Compte.id = Profil_Utilisateurice.id")
        if type == "artiste":
            cur.execute("SELECT * FROM Compte JOIN Profil_Artiste on Compte.id = Profil_Artiste.id")
        if type == "tous":
            cur.execute("SELECT * FROM Compte")

    if table == 'b':
        cur.execute("SELECT * FROM Chanson")
    if table == 'c':
        cur.execute("SELECT * FROM Album")
    if table == 'd':
        cur.execute("SELECT * FROM GenresMusicaux")
    if table == 'e':
        cur.execute("SELECT * FROM Playlist")
    if table == 'f':
        cur.execute("SELECT * FROM Pays")

    data = cur.fetchall()
    for row in data :
        print(row)

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
        conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
        conn.autocommit = True
        cur = conn.cursor()
        print("Connexion réussie")
        choice = '1'

        # A exécuter si la base de donnée n'est pas déjà crée
        # creation_table(cur)
        # insertion_donnee(cur)

        # A exécuter pour supprimer l'entièreté de la base de donnée
        # suppression_bdd(cur)

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