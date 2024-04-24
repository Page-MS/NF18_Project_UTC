
--Musique Classique
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Symphonie n° 40', 1500, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Mozart'), 'Classique');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Eine kleine Nachtmusik', 1200, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Mozart'), 'Classique');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Le Nozze di Figaro', 10800, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Mozart'), 'Classique');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Nocturne en mi bémol majeur', 300, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Chopin'), 'Classique');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Ballade en sol mineur', 600, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Chopin'), 'Classique');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Polonaise héroïque', 420, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Chopin'), 'Classique');

--Autre
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Thriller', 358, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Michael Jackson'), 'Pop');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Billie Jean', 296, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Michael Jackson'), 'Pop');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Beat It', 258, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Michael Jackson'), 'Pop');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Can''t Help Falling in Love', 177, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Elvis Presley'), 'Rock');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Suspicious Minds', 250, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Elvis Presley'), 'Rock');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Jailhouse Rock', 146, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Elvis Presley'), 'Rock');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Like a Rolling Stone', 368, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Bob Dylan'), 'Rock');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Blowin'' in the Wind', 155, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Bob Dylan'), 'Folk');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'The Times They Are a-Changin', 184, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Bob Dylan'), 'Folk');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Like a Virgin', 224, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Madonna'), 'Pop');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Vogue', 314, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Madonna'), 'Pop');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Material Girl', 222, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Madonna'), 'Pop');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Imagine', 183, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'John Lennon'), 'Rock');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Jealous Guy', 243, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'John Lennon'), 'Rock');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Instant Karma!', 213, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'John Lennon'), 'Rock');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Space Oddity', 295, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'David Bowie'), 'Rock');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Heroes', 363, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'David Bowie'), 'Rock');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Let''s Dance', 287, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'David Bowie'), 'Rock');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Hey Jude', 431, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Paul McCartney'), 'Rock');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Yesterday', 157, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Paul McCartney'), 'Rock');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Live and Let Die', 197, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Paul McCartney'), 'Rock');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Superstition', 278, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Stevie Wonder'), 'Soul');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Isn''t She Lovely', 215, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Stevie Wonder'), 'Soul');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Signed, Sealed, Delivered', 179, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Stevie Wonder'), 'Soul');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Bohemian Rhapsody', 367, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Freddie Mercury'), 'Rock');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Somebody to Love', 296, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Freddie Mercury'), 'Rock');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'We Will Rock You', 122, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Freddie Mercury'), 'Rock');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Purple Rain', 497, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Prince'), 'Pop');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'When Doves Cry', 221, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Prince'), 'Pop');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Kiss', 224, NULL, (SELECT id FROM Profil_Artiste WHERE nom = 'Prince'), 'Pop');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'What a Wonderful World', 143, NULL, (SELECT id FROM Compte WHERE nom = 'Louis Armstrong'), 'Jazz');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'La Vie en rose', 211, NULL, (SELECT id FROM Compte WHERE nom = 'Louis Armstrong'), 'Jazz');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'When the Saints Go Marching In', 197, NULL, (SELECT id FROM Compte WHERE nom = 'Louis Armstrong'), 'Jazz');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'California Love', 244, NULL, (SELECT id FROM Compte WHERE nom = 'Tupac Shakur'), 'Hip-hop');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Changes', 271, NULL, (SELECT id FROM Compte WHERE nom = 'Tupac Shakur'), 'Hip-hop');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Dear Mama', 272, NULL, (SELECT id FROM Compte WHERE nom = 'Tupac Shakur'), 'Hip-hop');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Crazy in Love', 235, NULL, (SELECT id FROM Compte WHERE nom = 'Beyoncé'), 'R&B');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Single Ladies (Put a Ring on It)', 201, NULL, (SELECT id FROM Compte WHERE nom = 'Beyoncé'), 'R&B');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Halo', 230, NULL, (SELECT id FROM Compte WHERE nom = 'Beyoncé'), 'R&B');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Get Lucky', 248, NULL, (SELECT id FROM Compte WHERE nom = 'Daft Punk'), 'Electro');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Harder, Better, Faster, Stronger', 224, NULL, (SELECT id FROM Compte WHERE nom = 'Daft Punk'), 'Electro');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Around the World', 421, NULL, (SELECT id FROM Compte WHERE nom = 'Daft Punk'), 'Electro');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Summer', 223, NULL, (SELECT id FROM Compte WHERE nom = 'Calvin Harris'), 'EDM');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Feel So Close', 220, NULL, (SELECT id FROM Compte WHERE nom = 'Calvin Harris'), 'EDM');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'One Kiss', 214, NULL, (SELECT id FROM Compte WHERE nom = 'Calvin Harris'), 'EDM');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'If Your Mother Only Knew', 157, NULL, (SELECT id FROM Compte WHERE nom = 'Rahzel'), 'Beatbox');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'All I Know', 220, NULL, (SELECT id FROM Compte WHERE nom = 'Rahzel'), 'Beatbox');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Make the Music 2000', 274, NULL, (SELECT id FROM Compte WHERE nom = 'Rahzel'), 'Beatbox');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'I Walk the Line', 165, NULL, (SELECT id FROM Compte WHERE nom = 'Johnny Cash'), 'Country');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Folsom Prison Blues', 170, NULL, (SELECT id FROM Compte WHERE nom = 'Johnny Cash'), 'Country');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Hurt', 219, NULL, (SELECT id FROM Compte WHERE nom = 'Johnny Cash'), 'Country');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Love Sosa', 229, NULL, (SELECT id FROM Compte WHERE nom = 'Chief Keef'), 'Drill');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Faneto', 265, NULL, (SELECT id FROM Compte WHERE nom = 'Chief Keef'), 'Drill');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'I Don''t Like', 290, NULL, (SELECT id FROM Compte WHERE nom = 'Chief Keef'), 'Drill');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Do I Wanna Know?', 272, NULL, (SELECT id FROM Compte WHERE nom = 'Arctic Monkeys'), 'Indie');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Fluorescent Adolescent', 183, NULL, (SELECT id FROM Compte WHERE nom = 'Arctic Monkeys'), 'Indie');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'R U Mine?', 205, NULL, (SELECT id FROM Compte WHERE nom = 'Arctic Monkeys'), 'Indie');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Salad Days', 171, NULL, (SELECT id FROM Compte WHERE nom = 'Mac DeMarco'), 'Lo-fi');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Chamber of Reflection', 251, NULL, (SELECT id FROM Compte WHERE nom = 'Mac DeMarco'), 'Lo-fi');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Ode to Viceroy', 189, NULL, (SELECT id FROM Compte WHERE nom = 'Mac DeMarco'), 'Lo-fi');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Lose Yourself', 326, NULL, (SELECT id FROM Compte WHERE nom = 'Eminem'), 'Rap');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Stan', 370, NULL, (SELECT id FROM Compte WHERE nom = 'Eminem'), 'Rap');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Without Me', 290, NULL, (SELECT id FROM Compte WHERE nom = 'Eminem'), 'Rap');
