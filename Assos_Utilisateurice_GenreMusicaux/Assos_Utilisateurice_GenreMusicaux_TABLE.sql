CREATE TABLE Assos_Utilisateurice_GenreMusicaux(
    utilisateurice INTEGER REFERENCES Profil_Utilisateurice(id),
    genre VARCHAR(30) REFERENCES GenresMusicaux(nom),
    PRIMARY KEY (utilisateurice, genre)
);