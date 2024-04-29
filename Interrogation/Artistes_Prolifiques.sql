-- Séléctionne les 10 artistes avec le plus de chansons dans la base de données

SELECT Compte.nom AS Nom, COUNT(Chanson.id) AS Nombrechanson
FROM Compte
JOIN Chanson ON Chanson.createurice = Compte.id
GROUP BY Compte.id
ORDER BY Nombrechanson DESC
LIMIT 10;

