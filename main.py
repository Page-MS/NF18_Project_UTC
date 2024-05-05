import psycopg2


HOST = "localhost"
USER = "postgres"
PASSWORD = ""
DATABASE = "postgres"


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


def main():
    try :
        conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
        print("Connexion réussie")
        choice = '1'

        while choice == '1' or choice=='2' :
            print("__________________________________________________")
            print("Pour entrer les données de la base de donnée tapez 1")
            print("Pour supprimer les données, entrez 2")
            print("Pour pour quitter entrez n'importe quel autre charactère")

            choice = input()
            if choice == '1':
                entrer_donnees(conn)
            if choice == '2':
                Suppr_tout(conn)


            print(choice)

    except Exception as error :
        print("Une erreur s'est produite : ", error)
        print("Type d'exception : ", type(error))



if __name__ == '__main__':
    main()