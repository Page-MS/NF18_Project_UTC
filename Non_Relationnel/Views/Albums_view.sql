CREATE OR REPLACE VIEW V_Albums
AS SELECT
        a.id, a.titre, EXTRACT(YEAR FROM a.annee_de_sortie) AS annee_de_sortie, jsonb_array_length(chansons::jsonb) AS nombre_de_chansons,
        a.chansons, SUM((c.chanson ->> 'duree')::integer) AS durée_totale
        FROM NR_Album a, LATERAL jsonb_array_elements(a.chansons::jsonb) AS c(chanson)
        GROUP BY a.id, a.titre
        ORDER BY a.id;