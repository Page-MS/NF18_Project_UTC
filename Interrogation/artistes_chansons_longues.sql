--Donner les artistes avec les chansons les plus longues. 
--(Identifier les artistes dont les chansons dépassent une durée spécifique, par exemple 10 minutes)

--Pour ce faire, on regroupe d'abord toutes les chansons de chaques artistes avec un JOIN et un GROUP BY
--Puis on calcule la durée maximale des chansons de chaques artistes, 
--On ajoute une condition (qui est factultative) pour ne considerer que les artistes ayant fait une chansons de 
--durée superieur a 600 secondes soit 10min 


SELECT Profil_Artiste.nom, MAX(Chanson.duree) AS duree_max
FROM Profil_Artiste
JOIN Chanson ON Chanson.createurice = Profil_Artiste.id
WHERE duree_max >= 600
GROUP BY Chanson.id 




