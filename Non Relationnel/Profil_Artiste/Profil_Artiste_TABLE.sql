DROP TYPE IF EXISTS TYPE_PROFIL ;

CREATE TYPE TYPE_PROFIL AS ENUM(
    'Profil_Groupe',
    'Profil_Artiste_Solo',
    'Profil_Artiste');

CREATE TABLE NR_Profil_Artiste(
    id SERIAL PRIMARY KEY,
    nom VARCHAR(30) NOT NULL,
    bio varchar(500),
    type TYPE_PROFIL NOT NULL,
    groupe integer references Profil_Artiste(id),
    pays varchar(30), 
    CONSTRAINT check_solo_or_group CHECK (
        (type = 'Profil_Artiste_Solo')
        OR
        (type <> 'Profil_Artiste_Solo' AND groupe IS NULL)
    )
);