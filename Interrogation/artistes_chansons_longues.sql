
-- Autre manière de faire

--Pour ce faire, on regroupe d'abord toutes les chansons de chaques artistes avec un JOIN et un GROUP BY
--Puis on cherche la chanson la plus longue de chaque artistes,
--On ajoute ensuite une condition pour ne considerer que les artistes ayant fait une chansons de durée superieur a par exemple 600 secondes soit 10min

SELECT Compte.nom
FROM Compte
JOIN Chanson ON Chanson.createurice = Compte.id
GROUP BY Compte.id
HAVING MAX(Chanson.duree) >= 600;