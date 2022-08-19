
# Sparkify - Data Modeling with Postgres

## Summary
---------

This project analyzes the data collected on songs and user activity on the Sparkify music streaming app. The purpose of the project is understanding the songs users are listening to.

A Postgress database is used to store and collected analytics on the data collected.

## Running the scripts
-----------



## Files Description
---------------

### Song Dataset

The first dataset is a subset of real data from the [Million Song Dataset](http://millionsongdataset.com/). Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are file paths to two files in this dataset.

```
song_data/A/B/C/TRABCEI128F424C983.json
song_data/A/A/B/TRAABJL12903CDCF1A.json
```

This is an example of a song file:

```
{
    "num_songs": 1, 
    "artist_id": "ARXR32B1187FB57099", 
    "artist_latitude": null, 
    "artist_longitude": null, 
    "artist_location": "", 
    "artist_name": "Gob", 
    "song_id": "SOFSOCN12A8C143F5D", 
    "title": "Face the Ashes", 
    "duration": 209.60608, 
    "year": 2007
}
```

### Log Dataset
The second dataset consists of log files in JSON format generated by this [event simulator](https://github.com/Interana/eventsim) based on the songs in the dataset above. These simulate activity logs from a music streaming app based on specified configurations.

```
log_data/2018/11/2018-11-12-events.json
log_data/2018/11/2018-11-13-events.json
```

This is an example of an entry on a log file:
```
{
    "artist": "Muse",
    "auth": "Logged In",
    "firstName": "Harper",
    "gender": "M",
    "itemInSession": 1,
    "lastName": "Barrett",
    "length": 209.50159,
    "level": "paid",
    "location": "New York-Newark-Jersey City, NY-NJ-PA",
    "method": "PUT",
    "page": "NextSong",
    "registration": 1540685364796.0,
    "sessionId": 275,
    "song": "Supermassive Black Hole (Twilight Soundtrack Version)",
    "status": 200,
    "ts": 1541721977796,
    "userAgent": "\"Mozilla\/5.0 (Windows NT 6.3; WOW64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.143 Safari\/537.36\"",
    "userId": "42"
}
```

### Project Files

- `create_tables.py` drops and creates your tables.
- `sql_queries.py` contains all the sql queries.
- `etl.py` reads and processes files from `song_data` and `log_data` and loads them into the tables.
- `etl.pynb` reads and processes a single file from `song_data` and `log_data` and loads the data into the tables. This notebook contains detailed instructions on the ETL process for each of the tables.
- `test.pynb` contains testing on the database structure and data loaded.