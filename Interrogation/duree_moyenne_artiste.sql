SELECT  Profil_Artiste.nom as Nom, AVG(Chanson.duree) as Durree_Moyenne 
FROM Chanson 
JOIN Profil_Artiste ON Chanson.createurice = Profil_Artiste.id 
GROUP BY Profil_Artiste.id HAVING Count(Chanson.id) >= 5;

