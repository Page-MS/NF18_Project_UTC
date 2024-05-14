-- Trouver les genres préférés des utilisateurs. (Analyser les genres les plus préférés pour chaque utilisateur)

-- Por ce faire, on effectue une requête permettant d'obtenir le genre préféré d'un utilisateur donné
-- Il serait possible d'itérer pour obtenir le genre préféré de chaque utilisateur

SELECT GenresMusicaux.nom AS "genre_musical", COUNT(GenresMusicaux.nom) AS nombre_utilisateur  
    FROM GenresMusicaux, Profil_Utilisateurice
        JOIN Assos_Utilisateurice_GenreMusicaux ON Profil_Utilisateurice.id = Assos_Utilisateurice_GenreMusicaux.utilisateurice
        JOIN GenresMusicaux ON Assos_Utilisateurice_GenreMusicaux.genre = GenreMusicaux.nom 
GROUP BY GenreMusicaux.nom
ORDER BY nombre_utilisateur DESC

-- Genre préféré par tout les utilisateur (en gros les genres les plus populaires.)