CREATE TYPE AUTORISATION AS ENUM('privée', 'publique', 'partagee_aux_amies');
CREATE TABLE Playlist(
    id SERIAL PRIMARY KEY,
    titre VARCHAR(30) NOT NULL,
    description VARCHAR(200),
    autorisation_acces AUTORISATION NOT NULL ,
    createurice INTEGER,
    chansons JSONB,
    albums JSONB,
    UNIQUE(titre,createurice)
);