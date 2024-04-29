SELECT Compte.nom as Nom, AVG(Chanson.duree) as Durree_Moyenne
FROM Chanson
JOIN Compte ON Chanson.createurice = Compte.id
GROUP BY Compte.id
HAVING Count(Chanson.id) >= 5;
