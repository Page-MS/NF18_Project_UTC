CREATE OR REPLACE VIEW V_Chansons
AS SELECT
        a.id as id_album, a.titre as album ,CAST(c->>'id' as INTEGER) as id_chanson,
        c->>'titre' as titre, p.nom as interprète,
        CAST(c->>'duree' as INTEGER) as duree,
        c->>'genre_musical' as genre,
        c->'droit_auteurice'-> 'auteurs' as auteurices,
        c->'droit_auteurice'-> 'compositeurs' as compositeurices,
        c->'droit_auteurice'-> 'editeurs' as éditeurices
        FROM NR_Album a, JSON_ARRAY_ELEMENTS(a.chansons) c
        LEFT JOIN NR_Profil_Artiste p ON CAST(c->>'createurice' as INTEGER) = p.id;