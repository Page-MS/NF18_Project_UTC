INSERT INTO Playlist(id, titre, description, autorisation_acces, createurice) VALUES(DEFAULT, "Top Hits 2010", "Tous les meilleurs hits de 2010 rassemblés dans une seul playliste !",
'publique',(SELECT id FROM Compte WHERE nom = 'Xxx_Hater_xxX'));
INSERT INTO Playlist(id, titre, description, autorisation_acces, createurice) VALUES(DEFAULT, "beats to relax and study", "Lofi beats to relax and study, lofi hip hop radio",
'publique', (SELECT id FROM Compte WHERE nom = 'Lofi Girl'));
INSERT INTO Playlist(id, titre, description, autorisation_acces, createurice) VALUES(DEFAULT, "Coup de coeurs", "Vos musiques préférés.",
'private',(SELECT id FROM Compte WHERE nom = 'jump_max'));
INSERT INTO Playlist(id, titre, description, autorisation_acces, createurice) VALUES(DEFAULT, "A partager aux potes", "Les musiques que mes amis doivent absolument écouter.",
'partagee_aux_amies',(SELECT id FROM Compte WHERE nom = 'jump_max'));
INSERT INTO Playlist(id, titre, description, autorisation_acces, createurice) VALUES(DEFAULT, "Songs to detruire les acquis sociaux", "Playlist Motivation pour couper les fonds de l'hopital publique",
'private',(SELECT id FROM Compte WHERE nom = 'emmanuel_macron'));
INSERT INTO Playlist(id, titre, description, autorisation_acces, createurice) VALUES(DEFAULT, "Brigitte time", "...quality time aec Brigitte",
'publique',(SELECT id FROM Compte WHERE nom = 'emmanuel_macron'));
INSERT INTO Playlist(id, titre, description, autorisation_acces, createurice) VALUES(DEFAULT, "Musique cool", "Pas cool moi ? on me l'avait pas fait depuis longtemps celle là",
'publique',(SELECT id FROM Compte WHERE nom = 'Xxx_Hater_xxX'));
INSERT INTO Playlist(id, titre, description, autorisation_acces, createurice) VALUES(DEFAULT, "So Sad Saucisse", "Pour quand je suis triste !",
'partagee_aux_amies',(SELECT id FROM Compte WHERE nom = 'chimpanze_combat'));