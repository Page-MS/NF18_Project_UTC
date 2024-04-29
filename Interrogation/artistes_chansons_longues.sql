-- La durée des chansons est mesurée en seconde donc cette requête cherche les artistes différents ayant des chansons de plus de 10 minutes

SELECT DISTINCT Compte.nom
FROM Chanson Join Compte ON Chanson.createurice = Compte.id
WHERE Chanson.duree > (600);