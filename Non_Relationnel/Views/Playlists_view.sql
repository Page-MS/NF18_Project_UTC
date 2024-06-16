CREATE OR REPLACE VIEW V_Playlists
AS SELECT
        p.id as id_playlist, p.titre, p.description,
        jsonb_agg(c.chanson) AS chansons_de_l_album,
        jsonb_array_length(p.chansons::jsonb) AS nombre_de_chansons
FROM  NR_Playlist p
    CROSS JOIN LATERAL jsonb_array_elements(p.albums::jsonb) AS ab(album)
    JOIN NR_Album a ON (ab.album ->> 'id')::INTEGER = a.id
    CROSS JOIN LATERAL jsonb_array_elements(a.chansons::jsonb) AS c(chanson)
    GROUP BY p.id;
