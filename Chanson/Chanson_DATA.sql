
--Musique Classique
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Symphonie n° 40', 1500, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Mozart'), 'Classique');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Eine kleine Nachtmusik', 1200, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Mozart'), 'Classique');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Le Nozze di Figaro', 10800, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Mozart'), 'Classique');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Nocturne en mi bémol majeur', 300, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Chopin'), 'Classique');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Ballade en sol mineur', 600, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Chopin'), 'Classique');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Polonaise héroïque', 420, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Chopin'), 'Classique');

--Autre
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Thriller', 358, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Michael Jackson'), 'Pop');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Billie Jean', 296, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Michael Jackson'), 'Pop');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Beat It', 258, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Michael Jackson'), 'Pop');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Can''t Help Falling in Love', 177, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Elvis Presley'), 'Rock');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Suspicious Minds', 250, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Elvis Presley'), 'Rock');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Jailhouse Rock', 146, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Elvis Presley'), 'Rock');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Like a Rolling Stone', 368, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Bob Dylan'), 'Rock');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Blowin'' in the Wind', 155, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Bob Dylan'), 'Folk');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'The Times They Are a-Changin', 184, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Bob Dylan'), 'Folk');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Like a Virgin', 224, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Madonna'), 'Pop');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Vogue', 314, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Madonna'), 'Pop');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Material Girl', 222, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Madonna'), 'Pop');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Imagine', 183, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'John Lennon'), 'Rock');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Jealous Guy', 243, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'John Lennon'), 'Rock');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Instant Karma!', 213, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'John Lennon'), 'Rock');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Space Oddity', 295, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'David Bowie'), 'Rock');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Heroes', 363, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'David Bowie'), 'Rock');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Let''s Dance', 287, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'David Bowie'), 'Rock');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Hey Jude', 431, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Paul McCartney'), 'Rock');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Yesterday', 157, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Paul McCartney'), 'Rock');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Live and Let Die', 197, (SELECT id FROM Album WHERE titre = 'Compliation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Paul McCartney'), 'Rock');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Superstition', 278, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Stevie Wonder'), 'Soul');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Isn''t She Lovely', 215, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Stevie Wonder'), 'Soul');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Signed, Sealed, Delivered', 179, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Stevie Wonder'), 'Soul');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Bohemian Rhapsody', 367, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Freddie Mercury'), 'Rock');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Somebody to Love', 296, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Freddie Mercury'), 'Rock');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'We Will Rock You', 122, (SELECT id FROM Album WHERE titre = 'Compilation Various Artists'), (SELECT id FROM Profil_Artiste WHERE nom = 'Freddie Mercury'), 'Rock');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Purple Rain', 497, (SELECT id FROM Album WHERE titre = 'Purple Rain'), (SELECT id FROM Profil_Artiste WHERE nom = 'Prince'), 'Pop');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'When Doves Cry', 221, (SELECT id FROM Album WHERE titre = 'Purple Rain'), (SELECT id FROM Profil_Artiste WHERE nom = 'Prince'), 'Pop');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Kiss', 224, (SELECT id FROM Album WHERE titre = 'Parade'), (SELECT id FROM Profil_Artiste WHERE nom = 'Prince'), 'Pop');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'What A Wonderful World', 143, (SELECT id FROM Album WHERE titre = 'What A Wonderful World'), (SELECT id FROM Compte WHERE nom = 'Louis Armstrong'), 'Jazz');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'La Vie en rose', 211, (SELECT id FROM Album WHERE titre = 'Satchmo Serenades'), (SELECT id FROM Compte WHERE nom = 'Louis Armstrong'), 'Jazz');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'When the Saints Go Marching In', 197, (SELECT id FROM Album WHERE titre = 'Louis Armstrong Of New Orleans'), (SELECT id FROM Compte WHERE nom = 'Louis Armstrong'), 'Jazz');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'California Love', 244, (SELECT id FROM Album WHERE titre = 'Greatest Hits'), (SELECT id FROM Compte WHERE nom = 'Tupac Shakur'), 'Hip-hop');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Changes', 271, (SELECT id FROM Album WHERE titre = 'Greatest Hits'), (SELECT id FROM Compte WHERE nom = 'Tupac Shakur'), 'Hip-hop');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Dear Mama', 272, (SELECT id FROM Album WHERE titre = 'Me Against The World'), (SELECT id FROM Compte WHERE nom = 'Tupac Shakur'), 'Hip-hop');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Crazy in Love', 235, (SELECT id FROM Album WHERE titre = 'Dangerously In Love'), (SELECT id FROM Compte WHERE nom = 'Beyoncé'), 'R&B');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Single Ladies (Put a Ring on It)', 201, (SELECT id FROM Album WHERE titre = 'I AM...SASHA FIERCE'), (SELECT id FROM Compte WHERE nom = 'Beyoncé'), 'R&B');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Halo', 230, (SELECT id FROM Album WHERE titre = 'I AM...SASHA FIERCE'), (SELECT id FROM Compte WHERE nom = 'Beyoncé'), 'R&B');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Get Lucky', 248, (SELECT id FROM Album WHERE titre = 'Random Access Memories'), (SELECT id FROM Compte WHERE nom = 'Daft Punk'), 'Electro');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Harder, Better, Faster, Stronger', 224, (SELECT id FROM Album WHERE titre = 'Discovery'), (SELECT id FROM Compte WHERE nom = 'Daft Punk'), 'Electro');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Around the World', (SELECT id FROM Album WHERE titre = 'Homework'), NULL, (SELECT id FROM Compte WHERE nom = 'Daft Punk'), 'Electro');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Summer', 223, (SELECT id FROM Album WHERE titre = 'Motion'), (SELECT id FROM Compte WHERE nom = 'Calvin Harris'), 'EDM');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Feel So Close', 220, (SELECT id FROM Album WHERE titre = '18 Months'), (SELECT id FROM Compte WHERE nom = 'Calvin Harris'), 'EDM');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'One Kiss', 214, (SELECT id FROM Album WHERE titre = 'One Kiss'), (SELECT id FROM Compte WHERE nom = 'Calvin Harris'), 'EDM');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'If Your Mother Only Knew', 157, (SELECT id FROM Album WHERE titre = 'Make The Music 2000'), (SELECT id FROM Compte WHERE nom = 'Rahzel'), 'Beatbox');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'All I Know', 220, (SELECT id FROM Album WHERE titre = 'Make The Music 2000'), (SELECT id FROM Compte WHERE nom = 'Rahzel'), 'Beatbox');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Make the Music 2000', 274, (SELECT id FROM Album WHERE titre = 'Make The Music 2000'), (SELECT id FROM Compte WHERE nom = 'Rahzel'), 'Beatbox');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'I Walk the Line', 165, (SELECT id FROM Album WHERE titre = 'I Walk the Line'), (SELECT id FROM Compte WHERE nom = 'Johnny Cash'), 'Country');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Folsom Prison Blues', 170, (SELECT id FROM Album WHERE titre = 'I Walk the Line'), (SELECT id FROM Compte WHERE nom = 'Johnny Cash'), 'Country');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Hurt', 219, (SELECT id FROM Album WHERE titre = 'American IV: The Man Comes Around'), (SELECT id FROM Compte WHERE nom = 'Johnny Cash'), 'Country');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Love Sosa', 229, (SELECT id FROM Album WHERE titre = 'Finally Rich'), (SELECT id FROM Compte WHERE nom = 'Chief Keef'), 'Drill');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Faneto', 265, (SELECT id FROM Album WHERE titre = 'Back from the Dead 2'), (SELECT id FROM Compte WHERE nom = 'Chief Keef'), 'Drill');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'I Don''t Like', 290, (SELECT id FROM Album WHERE titre = 'Finally Rich'), (SELECT id FROM Compte WHERE nom = 'Chief Keef'), 'Drill');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Do I Wanna Know?', 272, (SELECT id FROM Album WHERE titre = 'AM'), (SELECT id FROM Compte WHERE nom = 'Arctic Monkeys'), 'Indie');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Fluorescent Adolescent', 183, (SELECT id FROM Album WHERE titre = 'Favorite Worst Nightmare'), (SELECT id FROM Compte WHERE nom = 'Arctic Monkeys'), 'Indie');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'R U Mine?', 205, (SELECT id FROM Album WHERE titre = 'AM'), (SELECT id FROM Compte WHERE nom = 'Arctic Monkeys'), 'Indie');

INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Salad Days', 171, (SELECT id FROM Album WHERE titre = 'Salad Days'), (SELECT id FROM Compte WHERE nom = 'Mac DeMarco'), 'Lo-fi');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Chamber of Reflection', 251, (SELECT id FROM Album WHERE titre = 'Salad Days'), (SELECT id FROM Compte WHERE nom = 'Mac DeMarco'), 'Lo-fi');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Ode to Viceroy', 189, (SELECT id FROM Album WHERE titre = '2'), (SELECT id FROM Compte WHERE nom = 'Mac DeMarco'), 'Lo-fi');

INSERT INTO Chanson(id, titre, duree, album, createurice, genre_musical) VALUES(DEFAULT, 'Lose Yourself', 326, (SELECT id FROM Album WHERE titre = 'SHADYXV'), (SELECT id FROM Compte WHERE nom = 'Eminem'), 'Rap');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Stan', 370, (SELECT id FROM Album WHERE titre = 'The Marshall Mathers LP'), (SELECT id FROM Compte WHERE nom = 'Eminem'), 'Rap');
INSERT INTO Chanson(id, titre, duree, album, createurice, genremusical) VALUES(DEFAULT, 'Without Me', 290, (SELECT id FROM Album WHERE titre = 'The Eminem Show'), (SELECT id FROM Compte WHERE nom = 'Eminem'), 'Rap');
