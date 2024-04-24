SELECT Profil_Artiste.nom 
FROM Album 
JOIN Profil_Artiste ON Album.artiste_principal = Profil_Artiste.id
WHERE Album.duree_totale > 10;