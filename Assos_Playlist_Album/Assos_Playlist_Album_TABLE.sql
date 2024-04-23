CREATE TABLE Assos_Playlist_Album(
    id_Playlist INTEGER REFERENCES Playlist(id),
    id_Album INTEGER REFERENCES Album(id),
    PRIMARY KEY (id_Playlist, id_Album)
);