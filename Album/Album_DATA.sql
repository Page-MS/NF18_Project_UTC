INSERT INTO Album VALUES (DEFAULT, 'SHADYXV', '2014-11-24', 7500, (SELECT id FROM Compte WHERE nom = 'Eminem'));
INSERT INTO Album VALUES (DEFAULT, 'The Marshall Mathers LP', '2000-05-23', 4320, (SELECT id FROM Compte WHERE nom = 'Eminem'));
INSERT INTO Album VALUES (DEFAULT, 'The Eminem Show', '2002-05-26', 4620, (SELECT id FROM Compte WHERE nom = 'Eminem'));

INSERT INTO Album VALUES (DEFAULT, 'Salad Days', '2014-04-01', 2086, (SELECT id FROM Compte WHERE nom = 'Mac DeMarco'));
INSERT INTO Album VALUES (DEFAULT, '2', '2012-10-16', 1886, (SELECT id FROM Compte WHERE nom = 'Mac DeMarco'));
