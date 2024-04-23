CREATE TABLE Chanson(
    id INTEGER PRIMARY KEY,
    titre VARCHAR(30) NOT NULL,
    duree INTEGER NOT NULL,
    album INTEGER REFERENCES Album(id) NOT NULL,
    createurice INTEGER REFERENCES Profil_Artiste(id) NOT NULL,
    genre_musical VARCHAR(30) REFERENCES GenresMusicaux(nom) NOT NULL,
    UNIQUE(titre, createurice)
);