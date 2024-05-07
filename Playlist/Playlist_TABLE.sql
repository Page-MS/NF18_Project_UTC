CREATE TYPE IF NOT EXISTS AUTORISATION AS ENUM(
    'privée', 
    'publique', 
    'partagee_aux_amies'
    );

CREATE TABLE IF NOT EXISTS Playlist(
    id SERIAL PRIMARY KEY,
    titre VARCHAR(30) NOT NULL,
    description VARCHAR(200),
    autorisation_acces AUTORISATION NOT NULL ,
    createurice INTEGER REFERENCES Profil_Utilisateurice(id) NOT NULL,
    UNIQUE(titre,createurice)
);

