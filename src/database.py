import sqlite3

def connect_database():
    con = sqlite3.connect("data/database.db")
    cur = con.cursor()
    return con, cur

def create_database():
    con, cur = connect_database()
    cur.execute("CREATE TABLE IF NOT EXISTS favorites(" \
    "ID INTEGER PRIMARY KEY AUTOINCREMENT," \
    "TMDB_ID INTEGER UNIQUE," \
    "TITLE TEXT NOT NULL," \
    "RATING REAL," \
    "RELEASE_DATE TEXT NOT NULL," \
    "LANGUAGE TEXT NOT NULL," \
    "POSTER TEXT," \
    "OVERVIEW TEXT NOT NULL)")
    con.commit()
    con.close()

INSERT_FAVORITE = "INSERT INTO favorites(TMDB_ID, TITLE, RATING, RELEASE_DATE, LANGUAGE, POSTER, OVERVIEW)VALUES (?, ?, ?, ?, ?, ?, ?)"

def add_favorite(movie):
    con, cur = connect_database()
    cur.execute(INSERT_FAVORITE, (
        movie["tmdb_id"],
        movie["title"],
        movie["rating"],
        movie["release_date"],
        movie["language"],
        movie["poster"],
        movie["overview"],))
    con.commit()
    con.close()

def get_favorites():
    con, cur = connect_database()
    SELECT_FAVORITES = "SELECT * FROM favorites"
    cur.execute(SELECT_FAVORITES)
    favorites = cur.fetchall()
    con.close()
    return favorites