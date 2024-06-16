CREATE OR REPLACE VIEW V_Playlists
AS SELECT p.id, p.titre, p.description, p.autorisation_acces, u.nom as createurice,
       jsonb_array_length(jsonb_agg(DISTINCT c.chanson)) AS nb_chansons,
       SUM((c.chanson ->> 'duree')::integer) AS durée_totale,
       jsonb_agg(DISTINCT c.chanson) AS chansons

FROM NR_Playlist p JOIN NR_Profil_Utilisateurice u ON u.id = p.createurice
        LEFT JOIN

        (SELECT p.id , jsonb_agg(c.chanson) as chansons_albums
        FROM NR_Playlist p, jsonb_array_elements(p.albums::jsonb) AS ab(album)
        JOIN NR_Album a ON (ab.album ->> 'id')::INTEGER = a.id,
        jsonb_array_elements(a.chansons::jsonb) AS c(chanson)
        group by p.id) c_alb
        ON p.id = c_alb.id,
        jsonb_array_elements(p.chansons::jsonb || coalesce(c_alb.chansons_albums,
        '[]'::jsonb)) AS c(chanson)
        GROUP BY p.id, u.nom;
