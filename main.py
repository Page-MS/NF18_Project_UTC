import psycopg2


HOST = "localhost"
USER = "postgres"
PASSWORD = "dIBH544%"
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
    conn.commit()

def Suppr_tout(conn):
    cur = conn.cursor()
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