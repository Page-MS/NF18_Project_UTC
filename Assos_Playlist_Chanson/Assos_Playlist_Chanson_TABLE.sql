CREATE TABLE IF NOT EXISTS Assos_Playlist_Chanson(
    playlist INTEGER REFERENCES Playlist(id),
    chanson INTEGER REFERENCES Chanson(id),
    PRIMARY KEY(playlist, chanson)
);