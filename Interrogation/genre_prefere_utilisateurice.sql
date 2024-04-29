-- Pour trouver le genre musical préféré d'un personne 

-- il faut tout d'abord selectionner les chansons des playlists crée par l'utilisateur. 
-- Puis rassembler les chansons de ces playlists par genre musical, les compter et prende
-- le genre musical ayant le plus de chanson.
--On va donc utiliser des Join avec les tables Playlist, Profil_Utilisateurice, Chanson et GenreMusicaux
--Par la suite on regroupe les genres musicaux en fonction des Utilisateurs.
--On peut ainsi savoir le nombre de chansons de chaque genre écouté par chaque utilisateur, 
--on trie ce resultat par nombre de chansons décroissant pour ensuite avoir le genre musical préféré pour chaque utilisateur




SELECT Utilisateur.nom, GenresMusicaux.nom, COUNT(Chanson.id)
FROM Chanson 
JOIN Assos_Playlist_Chanson AS Assos ON Assos.chanson = Chanson.id 
JOIN Playlist ON Assos.playlist = Playlist.id 
JOIN Utilisateur ON Utilisateur.id = Playlist.createurice 
JOIN GenresMusicaux ON GenresMusicaux.nom = Chanson.genre_musical 
GROUP BY Utilisateur.id, GenresMusicaux.nom
ORDER BY COUNT(Chanson.id) DESC
LIMIT 3

--Renvoie le nombre de chansons differentes associé à chaque combinaisons Utilisateur, Genre Musical
