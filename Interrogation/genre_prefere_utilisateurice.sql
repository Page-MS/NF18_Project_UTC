-- Trouver les genres préférés des utilisateurs. (Analyser les genres les plus préférés pour chaque utilisateur)

-- Por ce faire, on effectue une requête permettant d'obtenir le genre préféré d'un utilisateur donné
-- Il serait possible d'itérer pour obtenir le genre préféré de chaque utilisateur

Select Compte.nom, Chanson.genre_musical, COUNT(Chanson.genre_musical) as "nombre_musiques_du_genre"
    from Compte
        JOIN Playlist ON playlist.createurice = Compte.id
        JOIN Assos_Playlist_Chanson ON Assos_Playlist_Chanson.playlist = Playlist.id
        JOIN Chanson ON Chanson.id = Assos_Playlist_Chanson.chanson
    WHERE nom = 'lau_fst'
    Group BY Compte.nom, Chanson.genre_musical
    ORDER BY nom, nombre_musiques_du_genre DESC
    LIMIT 1
