-- Trouver les genres préférés des utilisateurs. (Analyser les genres les plus préférés pour chaque utilisateur)

-- Por ce faire, on effectue une requête permettant d'obtenir le genre préféré d'un utilisateur donné
-- Il serait possible d'itérer pour obtenir le genre préféré de chaque utilisateur

SELECT GenresMusicaux.nom AS genre_musical, COUNT(Profil_Utilisateurice.id) AS nombre_utilisateurs
FROM GenresMusicaux
JOIN Assos_Utilisateurice_GenreMusicaux ON GenresMusicaux.nom = Assos_Utilisateurice_GenreMusicaux.genre
JOIN Profil_Utilisateurice ON Assos_Utilisateurice_GenreMusicaux.utilisateurice = Profil_Utilisateurice.id
GROUP BY GenresMusicaux.nom
ORDER BY nombre_utilisateurs DESC;

-- Genre préféré par tout les utilisateur (en gros les genres les plus populaires.)