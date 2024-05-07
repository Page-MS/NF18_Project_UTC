-- Donner les artistes avec les chansons les plus longues.
-- (Identifier les artistes dont les chansons dépassent une durée spécifique, par exemple 10 minutes)

-- Pour ce faire, on récuppère toutes les chansons de tous les artistes, en faisant une restriction sur la durée des chansons (par exemple supérieure à 600 secondes) et on ajoute l'atrribut DISTINCT pour ne pas avoir d'artistes en double

SELECT DISTINCT Compte.nom
FROM Chanson Join Compte ON Chanson.createurice = Compte.id
WHERE Chanson.duree >= (600);

