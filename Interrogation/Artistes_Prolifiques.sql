
--Trouver les artistes les plus prolifiques dans la base de données. (Les artistes avec le plus de chansons)

-- Pour faire cela, il faut d'abord regroupe les chansons pasr artistes
--Puis on peut ensuite calculer pour chaque artiste, le nombre de chansons qui ont été écrites
--enfin, il suffit de trier les artistes par nombre de chansons  crée descroissant. 
--On aurai egalement pu se limiter aux N première ligne en ajoutant la requète "LIMIT N" où N est un nombre

SELECT Profil_Artiste.nom AS Nom, COUNT(Chanson.id) AS Nombrechanson 
FROM Profil_Artiste
JOIN Chanson ON Chanson.createurice = Profil_Artiste.id 
GROUP BY Profil_Artiste.id 
ORDER BY Nombrechanson DESC;
