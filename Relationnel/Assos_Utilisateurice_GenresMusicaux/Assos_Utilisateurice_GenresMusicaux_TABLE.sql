CREATE TABLE IF NOT EXISTS Assos_Utilisateurice_GenresMusicaux(
    utilisateurice INTEGER REFERENCES Profil_Utilisateurice(id),
    genre VARCHAR(30) REFERENCES GenresMusicaux(nom),
    PRIMARY KEY (utilisateurice, genre)
);