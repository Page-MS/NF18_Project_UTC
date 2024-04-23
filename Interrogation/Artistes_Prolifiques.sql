
SELECT Profil_Artiste.nom AS Nom, COUNT(Chanson.id) AS Nombrechanson 
FROM Profil_Artiste
JOIN Chanson ON Chanson.createurice = Profil_Artiste.id 
GROUP BY Profil_Artiste.id 
ORDER BY Nombrechanson DESC;
