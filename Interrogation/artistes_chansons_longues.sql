-- Donner les artistes avec les chansons les plus longues.
-- (Identifier les artistes dont les chansons dépassent une durée spécifique, par exemple 10 minutes)

-- Pour ce faire, on récuppère toutes les chansons de tous les artistes, en faisant une restriction sur la durée des chansons (par exemple supérieure à 600 secondes) et on ajoute l'atrribut DISTINCT pour ne pas avoir d'artistes en double

SELECT DISTINCT Compte.nom
FROM Chanson Join Compte ON Chanson.createurice = Compte.id
WHERE Chanson.duree >= (600);

-- Autre manière de faire

--Pour ce faire, on regroupe d'abord toutes les chansons de chaques artistes avec un JOIN et un GROUP BY
--Puis on cherche la chanson la plus longue de chaque artistes,
--On ajoute ensuite une condition pour ne considerer que les artistes ayant fait une chansons de durée superieur a par exemple 600 secondes soit 10min

SELECT Compte.nom
FROM Compte
JOIN Chanson ON Chanson.createurice = Compte.id
GROUP BY Compte.id
HAVING MAX(Chanson.duree) >= 600;