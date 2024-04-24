-- Pour trouver le genre musical prefereé d'un personne 
-- il faut tout d'abord selectionner les chansons des playlists crée par l'utilisateur. 
-- Puis rassembler les chanssons de ces playlists par genre musical, les compter et prende
-- le genre musical ayant le plus de chanson.

--On va donc utiliser des Join avec les tables Playlist, Profil_Utilisateurice, Chanson et GenreMisocaux

select Chanson.id FROM Chanson Join Playlist On 
