CREATE TYPE PROFESSION AS ENUM('compositeur', 'editeur', 'auteur');

CREATE TABLE DroitsAuteurs(
    metier PROFESSION,
    compte INTEGER references Compte(id),
    chanson INTEGER references Chanson(id),
    PRIMARY KEY (metier,compte, chanson)
);