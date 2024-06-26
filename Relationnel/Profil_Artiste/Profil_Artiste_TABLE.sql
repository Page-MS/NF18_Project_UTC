DROP TYPE IF EXISTS TYPE_PROFIL ;

CREATE TYPE TYPE_PROFIL AS ENUM(
    'Profil_Groupe',
    'Profil_Artiste_Solo',
    'Profil_Artiste');

CREATE TABLE IF NOT EXISTS Profil_Artiste(
    id integer references Compte(id) PRIMARY KEY,
    bio varchar(500),
    type TYPE_PROFIL NOT NULL,
    groupe integer references Profil_Artiste(id),
    pays varchar(30) references Pays(nom) NOT NULL,
    CONSTRAINT check_solo_or_group CHECK (
        (type = 'Profil_Artiste_Solo')
        OR
        (type <> 'Profil_Artiste_Solo' AND groupe IS NULL)
    )
);