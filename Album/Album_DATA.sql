INSERT INTO Album VALUES (DEFAULT, 'SHADYXV', '2014-11-24', 7500, (SELECT id FROM Compte WHERE nom = 'Eminem'));
INSERT INTO Album VALUES (DEFAULT, 'The Marshall Mathers LP', '2000-05-23', 4320, (SELECT id FROM Compte WHERE nom = 'Eminem'));
INSERT INTO Album VALUES (DEFAULT, 'The Eminem Show', '2002-05-26', 4620, (SELECT id FROM Compte WHERE nom = 'Eminem'));

INSERT INTO Album VALUES (DEFAULT, 'Salad Days', '2014-04-01', 2086, (SELECT id FROM Compte WHERE nom = 'Mac DeMarco'));
INSERT INTO Album VALUES (DEFAULT, '2', '2012-10-16', 1886, (SELECT id FROM Compte WHERE nom = 'Mac DeMarco'));

INSERT INTO Album VALUES (DEFAULT, 'AM', '2013-09-09', 2507, (SELECT id FROM Compte WHERE nom = 'Arctic Monkeys'));
INSERT INTO Album VALUES (DEFAULT, 'Favorite Worst Nightmare', '2007-04-22', 2285, (SELECT id FROM Compte WHERE nom = 'Arctic Monkeys'));

INSERT INTO Album VALUES (DEFAULT, 'Finally Rich', '2012-01-01', 2713, (SELECT id FROM Compte WHERE nom = 'Chief Keef'));
INSERT INTO Album VALUES (DEFAULT, 'Back from the Dead 2', '2016-06-16', 4740, (SELECT id FROM Compte WHERE nom = 'Chief Keef'));

INSERT INTO Album VALUES (DEFAULT, 'I Walk the Line', '1964-06-13', 1963, (SELECT id FROM Compte WHERE nom = 'Johnny Cash'));
INSERT INTO Album VALUES (DEFAULT, 'American IV: The Man Comes Around', '2002-01-01', 3110, (SELECT id FROM Compte WHERE nom = 'Johnny Cash'));

INSERT INTO Album VALUES (DEFAULT, 'Make The Music 2000', '1999-01-01', 3010, (SELECT id FROM Compte WHERE nom = 'Rahzel'));

INSERT INTO Album VALUES (DEFAULT, 'Motion', '2014-10-31', 3353, (SELECT id FROM Compte WHERE nom = 'Calvin Harris'));
INSERT INTO Album VALUES (DEFAULT, '18 Months', '2012-10-29', 2994, (SELECT id FROM Compte WHERE nom = 'Calvin Harris'));
INSERT INTO Album VALUES (DEFAULT, 'One Kiss', '2018-04-06', 214, (SELECT id FROM Compte WHERE nom = 'Calvin Harris'));

INSERT INTO Album VALUES (DEFAULT, 'Random Access Memories', '2013-05-20', 4440, (SELECT id FROM Compte WHERE nom = 'Daft Punk'));
INSERT INTO Album VALUES (DEFAULT, 'Discovery', '2001-03-12', 3660, (SELECT id FROM Compte WHERE nom = 'Daft Punk'));
INSERT INTO Album VALUES (DEFAULT, 'Homework', '1997-01-17', 4440, (SELECT id FROM Compte WHERE nom = 'Daft Punk'));

INSERT INTO Album VALUES (DEFAULT, 'Dangerously In Love', '2003-06-24', 3660, (SELECT id FROM Compte WHERE nom = 'Beyoncé'));
INSERT INTO Album VALUES (DEFAULT, 'I AM...SASHA FIERCE', '2008-11-17', 2501, (SELECT id FROM Compte WHERE nom = 'Beyoncé'));
