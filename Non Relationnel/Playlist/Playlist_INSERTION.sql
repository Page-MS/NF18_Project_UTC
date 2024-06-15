INSERT INTO NR_Playlist VALUES (DEFAULT, 'Top Hits 2010', 'Tous les meilleurs hits de 2010 rassemblés dans une seul playliste !','publique', (SELECT id FROM NR_Profil_Utilisateurice where nom = 'jump_max'),'[{"id": 24,"titre": "Cleanin out my pocket", "duree": 541, "createurice" : 27, "genre_musical": "Rap", "droit_auteurice" : {"auteurs" : [7], "compositeurs" : [7], "éditeurs" : [21]}},{"id": 12,"titre": "Giorgio by Morder", "duree": 207, "createurice" : 8, "genre_musical": "Souk", "droit_auteurice" : {"auteurs" : [5,7], "compositeurs" : [5], "éditeurs" : [5]}},{"id": 40,"titre": "Digital Love", "duree": 222, "createurice" : 8, "genre_musical": "Souk", "droit_auteurice" : {"auteurs" : [], "compositeurs" : [8,29], "éditeurs" : [30]}},{"id": 16,"titre": "Disappear", "duree": 278, "createurice" : 21, "genre_musical": "Pop", "droit_auteurice" : {"auteurs" : [11,23], "compositeurs" : [11,18], "éditeurs" : [4]}}]','[{"id" : 1, "titre" : "SHADYXV"}, {"id" : 11, "titre" : "Compilation Queen"}]');
INSERT INTO NR_Playlist VALUES (DEFAULT, 'beats to relax and study', 'Lofi beats to relax and study, lofi hip hop radio','publique', (SELECT id FROM NR_Profil_Utilisateurice where nom = 'lau_fst') ,'[{"id": 3,"titre": "Die Alone", "duree": 208, "createurice" : 27, "genre_musical": "Souk", "droit_auteurice" : {"auteurs" : [23], "compositeurs" : [12], "éditeurs" : [6]}},{"id": 39,"titre": "Aerodynamic", "duree": 144, "createurice" : 8, "genre_musical": "Electro", "droit_auteurice" : {"auteurs" : [19], "compositeurs" : [], "éditeurs" : []}},{"id": 30,"titre": "Cooking Up Something Good", "duree": 205, "createurice" : 26, "genre_musical": "Indie", "droit_auteurice" : {"auteurs" : [], "compositeurs" : [], "éditeurs" : []}},{"id": 37,"titre": "Let her go", "duree": 544, "createurice" : 26, "genre_musical": "Indie", "droit_auteurice" : {"auteurs" : [18,11], "compositeurs" : [18], "éditeurs" : [11]}},{"id": 10,"titre": "Give life back to music", "duree": 403, "createurice" : 8, "genre_musical": "Electro", "droit_auteurice" : {"auteurs" : [2], "compositeurs" : [20,23], "éditeurs" : [19]}}]','[{"id" : 10, "titre" : "Discovery"}]');
INSERT INTO NR_Playlist VALUES (DEFAULT, 'Coup de coeurs', 'Vos musiques préférés.', 'privee',(SELECT id FROM NR_Profil_Utilisateurice where nom = 'iris_gri') ,'[]','[{"id" : 6, "titre" : "The Eminem Show"}, {"id" : 3, "titre": "Random Access Memories"},{"id" : 4, "titre" : "I AM...SASHA FIERCE"}]');
INSERT INTO NR_Playlist VALUES (DEFAULT, 'A partager aux potes', 'Les musiques que mes amis doivent absolument écouter.','partagee_aux_amies',(SELECT id FROM NR_Profil_utilisateurice WHERE nom = 'jump_max'),'[{"id": 19,"titre": "R U Mine", "duree": 124, "createurice" : 10, "genre_musical": "Rock", "droit_auteurice" : {"auteurs" : [9], "compositeurs" : [], "éditeurs" : []}},{"id": 5,"titre": "Brianstorm", "duree": 148, "createurice" : 10, "genre_musical": "Rock", "droit_auteurice" : {"auteurs" : [7,9], "compositeurs" : [15], "éditeurs" : [25]}},{"id": 42,"titre": "Bohemian Rhapsody", "duree": 367, "createurice" : 1, "genre_musical": "Rock", "droit_auteurice" : {"auteurs" : [2,3], "compositeurs" : [2,3], "éditeurs" : [1]}},{"id": 34,"titre": "Salad Days", "duree": 470, "createurice" : 26, "genre_musical": "Indie", "droit_auteurice" : {"auteurs" : [], "compositeurs" : [], "éditeurs" : [1]}},{"id": 17,"titre": "broken-heart girl", "duree": 169, "createurice" : 21, "genre_musical": "Pop", "droit_auteurice" : {"auteurs" : [], "compositeurs" : [15], "éditeurs" : [14]}},{"id": 6,"titre": "Teddy Picker", "duree": 102, "createurice" : 10, "genre_musical": "Rock" , "droit_auteurice" : {"auteurs" : [], "compositeurs" : [19], "éditeurs" : []}}]','[]');
INSERT INTO NR_Playlist VALUES (DEFAULT, 'detruire les acquis sociaux', 'Playlist Motivation pour couper les fonds de l hopital publique','privee',(SELECT id FROM NR_Profil_utilisateurice WHERE nom = 'emmanuel_macron'),'[{"id": 35,"titre": "Blue Boy", "duree": 158, "createurice" : 26, "genre_musical": "Indie", "droit_auteurice" : [{"auteurs" : [{"id" : 4}]}, {"compositeurs" : []}, {"éditeurs" : [{"id" : 4 }]}]},{"id": 22,"titre": "white America", "duree": 274, "createurice" : 27, "genre_musical": "Rap", "droit_auteurice" : [{"auteurs" : []}, {"compositeurs" : []}, {"éditeurs" : []}]},{"id": 9,"titre": "Fluorescent Adolescent", "duree": 222, "createurice" : 10, "genre_musical": "Drill" , "droit_auteurice" : [{"auteurs" : [{"id" : 4 }]}, {"compositeurs" : [{"id" : 30}]}, {"éditeurs" : []}]},{"id": 4,"titre": "Vegas", "duree": 365, "createurice" : 27, "genre_musical": "Zumba", "droit_auteurice" : [{"auteurs" : []}, {"compositeurs" : []}, {"éditeurs" : []}]}]','[]');
INSERT INTO NR_Playlist VALUES (DEFAULT, 'Brigitte time', '...quality time avec Brigitte','publique',(SELECT id FROM NR_Profil_utilisateurice WHERE nom = 'emmanuel_macron'),'[{"id": 18,"titre": "Do I Wanna Know ?", "duree": 147, "createurice" : 10, "genre_musical": "Rock", "droit_auteurice" : {"auteurs" : [8], "compositeurs" : [8,9], "éditeurs" : []}},{"id": 29,"titre": "Who Knew", "duree": 202, "createurice" : 27, "genre_musical": "Drill", "droit_auteurice" : {"auteurs" : [15], "compositeurs" : [15], "éditeurs" : [3]}}]','[{"id" : 7, "titre" : "The Marshall Mathers LP"}, {"id" : 3, "titre" : "Random Access Memories"}, {"id" : 4, "titre" : "I AM...SASHA FIERCE"}]');
INSERT INTO NR_Playlist VALUES (DEFAULT, 'Musique cool', 'Pas cool moi ? on me l avait pas fait depuis longtemps celle là','publique',(SELECT id FROM NR_Profil_utilisateurice WHERE nom = 'Xxx_Hater_xxX'),'[{"id": 11,"titre": "The game of love", "duree": 125, "createurice" : 8, "genre_musical": "Electro", "droit_auteurice" : {"auteurs" : [7,5], "compositeurs" : [6], "éditeurs" : [28,12]}},{"id": 15,"titre": "Halo", "duree": 142, "createurice" : 21, "genre_musical": "Pop", "droit_auteurice" : {"auteurs" : [13], "compositeurs" : [13], "éditeurs" : [13,14]}},{"id": 21,"titre": "Arabella", "duree": 745, "createurice" : 10, "genre_musical": "Indie", "droit_auteurice" : {"auteurs" : [1], "compositeurs" : [], "éditeurs" : []}}]','[{"id" : 11, "titre" : "Compilation Queen"}]');
INSERT INTO NR_Playlist VALUES (DEFAULT, 'So Sad Saucisse', 'Pour quand je suis triste !','partagee_aux_amies',(SELECT id FROM NR_Profil_utilisateurice WHERE nom = 'chimpanze_combat'),'[{"id": 36,"titre": "Brother", "duree": 208, "createurice" : 26, "genre_musical": "Indie", "droit_auteurice" : {"auteurs" : [30], "compositeurs" : [30], "éditeurs" : [27]}},{"id": 16,"titre": "Disappear", "duree": 278, "createurice" : 21, "genre_musical": "Pop", "droit_auteurice" : {"auteurs" : [11,23], "compositeurs" : [11,18], "éditeurs" : [4]}}]','[]');