# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays
  (
     songplay_id SERIAL NOT NULL PRIMARY KEY,
     start_time  TIMESTAMP NOT NULL,
     user_id     INT NOT NULL,
     level       VARCHAR NOT NULL,
     song_id     VARCHAR,
     artist_id   VARCHAR,
     session_id  INT,
     location    VARCHAR,
     user_agent  VARCHAR,
     CONSTRAINT fk_start_time
        FOREIGN KEY (start_time)
            REFERENCES time (start_time),
     CONSTRAINT fk_user_id
        FOREIGN KEY (user_id)
            REFERENCES users (user_id),
     CONSTRAINT fk_song_id
        FOREIGN KEY (song_id)
            REFERENCES songs (song_id),
     CONSTRAINT fk_artist_id
        FOREIGN KEY (artist_id)
            REFERENCES artists (artist_id)
  ) 
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users
  (
     user_id    INT NOT NULL PRIMARY KEY,
     first_name VARCHAR,
     last_name  VARCHAR NOT NULL,
     gender     VARCHAR,
     level      VARCHAR NOT NULL
  ) 
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs
  (
     song_id   VARCHAR NOT NULL PRIMARY KEY,
     title     VARCHAR NOT NULL,
     artist_id VARCHAR,
     year      INT NOT NULL,
     duration  NUMERIC NOT NULL
  ) 
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists
  (
     artist_id VARCHAR NOT NULL PRIMARY KEY,
     name      VARCHAR NOT NULL,
     location  VARCHAR,
     latitude  FLOAT8,
     longitude FLOAT8
  ) 
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time
  (
     start_time TIMESTAMP NOT NULL PRIMARY KEY,
     hour       INT NOT NULL,
     day        INT NOT NULL,
     week       INT NOT NULL,
     month      INT NOT NULL,
     year       INT NOT NULL,
     weekday    INT NOT NULL
  ) 
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays
(
    start_time,
    user_id,
    level,
    song_id,
    artist_id,
    session_id,
    location,
    user_agent
)
VALUES
(
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s
)
ON conflict do nothing;
""")

user_table_insert = ("""
INSERT INTO users
(
    user_id,
    first_name,
    last_name,
    gender,
    level
)
VALUES
(
    %s,
    %s,
    %s,
    %s,
    %s
)
ON CONFLICT (user_id) DO UPDATE
SET
    level = excluded.level;
""")

song_table_insert = ("""
INSERT INTO songs
(
    song_id, 
    title, 
    artist_id, 
    year, 
    duration
)
VALUES
(
    %s, 
    %s, 
    %s, 
    %s, 
    %s
)
ON CONFLICT DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists
(
    artist_id, 
    name, 
    location, 
    latitude, 
    longitude
)
VALUES
(
    %s, 
    %s, 
    %s, 
    %s, 
    %s
)
ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time
(
    start_time, 
    hour, 
    day, 
    week, 
    month, 
    year, 
    weekday
)
VALUES
(
    %s,
    %s, 
    %s, 
    %s, 
    %s, 
    %s, 
    %s
)
ON CONFLICT DO NOTHING;
""")

# FIND SONGS
#Implement the song_select query in sql_queries.py to find the song ID and artist ID based on the title, artist name, and duration of a song.
#Select the timestamp, user ID, level, song ID, artist ID, session ID, location, and user agent and set to songplay_data

song_select = ("""
SELECT  
    s.song_id,
    a.artist_id
FROM 
    songs AS s 
INNER JOIN
    artists AS a ON s.artist_id = a.artist_id
WHERE
    s.title = %s
AND
    a.name = %s
AND
    s.duration = %s
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]