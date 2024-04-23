CREATE TABLE Assos_Utilisateurice_Utilisateurice(
    ami_1 INTEGER REFERENCES Profil_utilisateurice(id),
    ami_2 INTEGER REFERENCES Profil_Utilisateurice(id),
    PRIMARY KEY(ami_1, ami_2),
    CHECK (ami_1 <> ami_2)
);