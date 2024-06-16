DROP TYPE IF EXISTS NR_TYPE_PROFIL ;

CREATE TYPE NR_TYPE_PROFIL AS ENUM(
    'Profil_Groupe',
    'Profil_Artiste_Solo',
    'Profil_Artiste');

CREATE TABLE IF NOT EXISTS NR_Profil_Artiste(
    id SERIAL PRIMARY KEY,
    nom VARCHAR(30) NOT NULL,
    bio varchar(500),
    type NR_TYPE_PROFIL NOT NULL,
    groupe integer references NR_Profil_Artiste(id),
    pays varchar(30), 
    CONSTRAINT check_solo_or_group CHECK (
        (type = 'Profil_Artiste_Solo')
        OR
        (type <> 'Profil_Artiste_Solo' AND groupe IS NULL)
    )
);