CREATE OR REPLACE VIEW V_Albums
AS SELECT
        a.id, a.titre, p.nom as artiste_principale, EXTRACT(YEAR FROM a.annee_de_sortie) AS annee_de_sortie, jsonb_array_length(chansons::jsonb) AS nombre_de_chansons,
        a.chansons, SUM((c.chanson ->> 'duree')::integer) AS durée_totale
        FROM NR_Album a JOIN NR_Profil_Artiste p ON p.id = a.artiste_principal , LATERAL jsonb_array_elements(a.chansons::jsonb) AS c(chanson)
        GROUP BY a.id, a.titre, p.nom
        ORDER BY a.id;