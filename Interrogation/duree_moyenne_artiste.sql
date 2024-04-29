
--Donner pour chaque artiste la durée moyenne de ses chansons, à condition qu'il ait au moins cinq chansons.

--On selectionne les chansons faitent par chaque artistes
--On regroupe ensuite ces chansons par artistes afin de calculer la moyenne (AVG)
--Enfin, on ajoute la condition Having Count(Chanson.id) >= 5 pour s'assurer qu'on calcule la moyenne sur un minimum 
--de 5 chansons

SELECT  Profil_Artiste.nom as Nom, AVG(Chanson.duree) as Durree_Moyenne 
FROM Chanson 
JOIN Profil_Artiste ON Chanson.createurice = Profil_Artiste.id 
GROUP BY Profil_Artiste.id HAVING Count(Chanson.id) >= 5;

