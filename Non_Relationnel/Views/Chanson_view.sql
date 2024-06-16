CREATE OR REPLACE VIEW V_Chansons
AS SELECT
        a.id as id_album, a.titre as album ,CAST(c->>'id' as INTEGER) as id_chanson,
        c->>'titre' as titre, CAST(c->>'duree' as INTEGER) as duree,
        c->>'createurice' as interprète, c->>'genre_musical' as genre,
        c->'droit_auteurice'-> 'auteurs' as auteurices,
        c->'droit_auteurice'-> 'compositeurs' as compositeurices,
        c->'droit_auteurice'-> 'éditeurs' as éditeurices
        FROM NR_Album a, JSON_ARRAY_ELEMENTS(a.chansons) c ;