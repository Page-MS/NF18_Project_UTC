-- Donner pour chaque artiste la durée moyenne de ses chansons, à condition qu'il ait au moins cinq chansons.

-- Pour ce faire, on selectionne les chansons faitent par chaque artistes
-- On regroupe ensuite ces chansons par artistes afin de calculer la moyenne (AVG)
-- Enfin, on ajoute la condition Having pour s'assurer qu'on calcule la moyenne seulement pour les artistes ayant au minimum 5 chansons

SELECT Compte.nom as Nom, AVG(Chanson.duree) as Durree_Moyenne
FROM Chanson
JOIN Compte ON Chanson.createurice = Compte.id
GROUP BY Compte.id
HAVING Count(Chanson.id) >= 5;