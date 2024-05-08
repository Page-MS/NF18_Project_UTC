import psycopg2
from postgres import DATABASE, PASSWORD

HOST = "localhost"
USER = "postgres"

def entrer_donnees(conn):
    cur = conn.cursor()
    cur.execute(open("Pays\Pays_TABLE.sql", "r").read())
    cur.execute(open("Pays\Pays_DATA.sql", "r").read())
    cur.execute(open("Compte\Compte_TABLE.sql", "r").read())
    cur.execute(open("Compte\Compte_DATA.sql", "r").read())
    cur.execute(open("GenresMusicaux\GenresMusicaux_TABLE.sql", "r").read())
    cur.execute(open("GenresMusicaux\GenresMusicaux_DATA.sql", "r").read())
    cur.execute(open("Profil_Artiste\Profil_Artiste_TABLE.sql", "r").read())
    cur.execute(open("Profil_Artiste\Profil_Artiste_DATA.sql", "r").read())
    cur.execute(open("Profil_Utilisateurice\Profil_Utilisateurice_TABLE.sql", "r").read())
    cur.execute(open("Profil_Utilisateurice\Profil_Utilisateurice_DATA.sql", "r").read())
    cur.execute(open("Album\Album_TABLE.sql", "r").read())
    cur.execute(open("Album\Album_DATA.sql", "r").read())
    cur.execute(open("Chanson\Chanson_TABLE.sql", "r").read())
    cur.execute(open("Chanson\Chanson_DATA.sql", "r").read())
    cur.execute(open("Playlist\Playlist_TABLE.sql", "r").read())
    cur.execute(open("Playlist\Playlist_DATA.sql", "r").read())
    cur.execute(open("Assos_Playlist_Album\Assos_Playlist_Album_TABLE.sql", "r").read())
    cur.execute(open("Assos_Playlist_Album\Assos_Playlist_Album_DATA.sql", "r").read())
    cur.execute(open("Assos_Playlist_Chanson\Assos_Playlist_Chanson_TABLE.sql", "r").read())
    cur.execute(open("Assos_Playlist_Chanson\Assos_Playlist_Chanson_DATA.sql", "r").read())
    cur.execute(open("Assos_Utilisateurice_Utilisateurice\Assos_Utilisateurice_Utilisateurice_TABLE.sql", "r").read())
    cur.execute(open("Assos_Utilisateurice_Utilisateurice\Assos_Utilisateurice_Utilisateurice_DATA.sql", "r").read())
    cur.execute(open("Assos_Utilisateurice_GenreMusicaux\Assos_Utilisateurice_GenreMusicaux_TABLE.sql", "r").read())
    cur.execute(open("Assos_Utilisateurice_GenreMusicaux\Assos_Utilisateurice_GenreMusicaux_DATA.sql", "r").read())
    cur.execute(open("DroitsAuteurs\DroitsAuteurs_TABLE.sql", "r").read())
    cur.execute(open("DroitsAuteurs\DroitsAuteurs_DATA.sql", "r").read())
    conn.commit()

def Suppr_tout(conn):
    cur = conn.cursor()
    cur.execute(open("Assos_Playlist_Album\Assos_Playlist_Album_DELETE.sql", "r").read())
    cur.execute(open("Assos_Playlist_Chanson\Assos_Playlist_Chanson_DELETE.sql", "r").read())
    cur.execute(open("Assos_Utilisateurice_Utilisateurice\Assos_Utilisateurice_Utilisateurice_DELETE.sql", "r").read())
    cur.execute(open("Assos_Utilisateurice_GenreMusicaux\Assos_Utilisateurice_GenreMusicaux_DELETE.sql", "r").read())
    cur.execute(open("DroitsAuteurs\DroitsAuteurs_DELETE.sql", "r").read())
    cur.execute(open("Playlist\Playlist_DELETE.sql", "r").read())
    cur.execute(open("Chanson\Chanson_DELETE.sql", "r").read())
    cur.execute(open("Album\Album_DELETE.sql", "r").read())
    cur.execute(open("Profil_Utilisateurice\Profil_Utilisateurice_DELETE.sql", "r").read())
    cur.execute(open("Profil_Artiste\Profil_Artiste_DELETE.sql", "r").read())
    cur.execute(open("Compte\Compte_DELETE.sql", "r").read())
    cur.execute(open("GenresMusicaux\GenresMusicaux_DELETE.sql", "r").read())
    cur.execute(open("Pays\Pays_DELETE.sql", "r").read())

    conn.commit()

def Commande_perso(conn):
    cur=conn.cursor()
    commande=input("Entrez votre commande : ")
    cur.execute(commande)
    # Fetch data line by line
    raw = cur.fetchone()
    while raw:
        print("- %s (devoir n%s),  note : %s" % (raw[0], raw[1], raw[2]))
        raw = cur.fetchone()
    conn.commit()

def chansons_longues(conn):
    cur = conn.cursor()
    cur.execute(open("Interrogation\Artistes_chansons_longues.sql", "r").read())
    # Fetch data line by line
    raw = cur.fetchone()
    if raw :
        while raw:
            print("- Nom de l'auteur %s" % (raw[0]))
            raw = cur.fetchone()
    conn.commit()

def artistes_prolifiques(conn):
    cur = conn.cursor()
    cur.execute(open("Interrogation\Artistes_Prolifiques.sql", "r").read())
    # Fetch data line by line
    raw = cur.fetchone()
    if raw :
        while raw:
            print("- %s a sorti %s chansons" % (raw[0],raw[1]))
            raw = cur.fetchone()
    conn.commit()

def duree_moyenne(conn):
    cur = conn.cursor()
    cur.execute(open("Interrogation\Duree_moyenne_artiste.sql", "r").read())
    # Fetch data line by line
    raw = cur.fetchone()
    if raw :
        while raw:
            print("- Nom de l'auteur %s, durée moyenne %s : " % (raw[0], raw[1]))
            raw = cur.fetchone()
    conn.commit()

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
    conn.commit()

def main():
    try :
        conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
        print("Connexion réussie")
        choice = '1'

        while '1' <= choice <= '7':
            print("__________________________________________________")
            print("Pour entrer les données de la base de donnée tapez 1")
            print("Pour supprimer les données, entrez 2")
            print("Pour executer une commande de votre choix en SQL, entrez 3")
            print("Pour afficher les artistes aux chansons longues, entrez 4")
            print("Pour afficher les artistes prolifiques, entrez 5")
            print("Pour afficher la durée moyenne des chansons d'un artiste, entrez 6")
            print("Pour afficher le genre musical préféré d'un.e utilisateurice, entrez 7")
            print("Pour pour quitter entrez n'importe quel autre charactère")
            print("------------------------------\nVotre choix :",end='')

            choice = input()
            if choice == '1':
                entrer_donnees(conn)
            if choice == '2':
                Suppr_tout(conn)
            if choice == '3':
                Commande_perso(conn)
            if choice == '4':
                chansons_longues(conn)
            if choice == '5':
                artistes_prolifiques(conn)
            if choice == '6':
                duree_moyenne(conn)
            if choice == '7':
                genre_prefere(conn)


            print(choice)

    except Exception as error :
        print("Une erreur s'est produite : ", error)
        print("Type d'exception : ", type(error))



if __name__ == '__main__':
    main()