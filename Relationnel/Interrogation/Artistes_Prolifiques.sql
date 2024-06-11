-- Trouver les artistes les plus prolifiques dans la base de données. (Les artistes avec le plus de chansons)

-- Pour ce faire, il faut d'abord regrouper les chansons par artistes

-- Séléctionne les 10 artistes avec le plus de chansons dans la base de données
-- Puis ensuite calculer le nombre de chansons de chaque artiste
-- Enfin, il suffit de trier les artistes par nombre de chansons décroissant.
-- On peut ajouter une limite pour avoir les N artistes les plus prolifiques


SELECT Compte.nom AS Nom, COUNT(Chanson.id) AS Nombrechanson
FROM Compte
JOIN Chanson ON Chanson.createurice = Compte.id
GROUP BY Compte.id
ORDER BY Nombrechanson DESC
LIMIT 10;