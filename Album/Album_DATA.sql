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