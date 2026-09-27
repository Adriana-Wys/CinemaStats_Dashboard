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

def get_favorites(sort_by="ID"):
    con, cur = connect_database()
    if sort_by == "title":
        SELECT_FAVORITE = "SELECT * FROM favorites ORDER BY TITLE ASC"
    elif sort_by == "rating":
        SELECT_FAVORITE = "SELECT * FROM favorites ORDER BY RATING DESC"
    elif sort_by == "release_date":
        SELECT_FAVORITE = "SELECT * FROM favorites ORDER BY RELEASE_DATE DESC"
    else:
        SELECT_FAVORITE = "SELECT * FROM favorites"
    cur.execute(SELECT_FAVORITE)
    favorites = cur.fetchall()
    con.close()
    return favorites

def is_favorite(movie):
    con, cur = connect_database()
    cur.execute("SELECT * FROM favorites WHERE TMDB_ID=?", (movie["tmdb_id"],))
    result = cur.fetchone()
    con.close()
    return result is not None

def delete_favorite(movie):
    con, cur = connect_database()
    cur.execute("DELETE FROM favorites WHERE TMDB_ID=?", (movie["tmdb_id"],))
    con.commit()
    con.close()

def count_favorites():
    con, cur = connect_database()
    cur.execute("SELECT COUNT(*) FROM favorites")
    result = cur.fetchone()
    con.close()
    return result[0]

def create_database():
    con, cur = connect_database()
    cur.execute("CREATE TABLE IF NOT EXISTS watchlist(" \
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

INSERT_WATCHLIST = "INSERT INTO watchlist(TMDB_ID, TITLE, RATING, RELEASE_DATE, LANGUAGE, POSTER, OVERVIEW)VALUES (?, ?, ?, ?, ?, ?, ?)"

def add_watchlist(movie):
    con, cur = connect_database()
    cur.execute(INSERT_WATCHLIST, (
        movie["tmdb_id"],
        movie["title"],
        movie["rating"],
        movie["release_date"],
        movie["language"],
        movie["poster"],
        movie["overview"],))
    con.commit()
    con.close()

def get_watchlist():
    con, cur = connect_database()
    cur.execute("SELECT * FROM watchlist")
    watchlist = cur.fetchall()
    con.close()
    return watchlist

def is_watchlist(movie):
    con, cur = connect_database()
    cur.execute("SELECT * FROM watchlist WHERE TMDB_ID=?", (movie["tmdb_id"],))
    result = cur.fetchone()
    con.close()
    return result is not None

def count_watchlist():
    con, cur = connect_database()
    cur.execute("SELECT COUNT(*) FROM watchlist")
    result = cur.fetchone()
    con.close()
    return result[0]

def delete_watchlist(movie):
    con, cur = connect_database()
    cur.execute("DELETE FROM watchlist WHERE TMDB_ID=?", (movie["tmdb_id"],))
    con.commit()
    con.close()

def create_database():
    con, cur = connect_database()
    cur.execute("CREATE TABLE IF NOT EXISTS watched(" \
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

INSERT_WATCHED = "INSERT INTO watched(TMDB_ID, TITLE, RATING, RELEASE_DATE, LANGUAGE, POSTER, OVERVIEW)VALUES (?, ?, ?, ?, ?, ?, ?)"

def add_watched(movie):
    con, cur = connect_database()
    cur.execute(INSERT_WATCHED, (
        movie["tmdb_id"],
        movie["title"],
        movie["rating"],
        movie["release_date"],
        movie["language"],
        movie["poster"],
        movie["overview"],))
    con.commit()
    con.close()

def get_watched():
    con, cur = connect_database()
    cur.execute("SELECT * FROM watched")
    watched = cur.fetchall()
    con.close()
    return watched

def is_watched(movie):
    con, cur = connect_database()
    cur.execute("SELECT * FROM watched WHERE TMDB_ID=?", (movie["tmdb_id"],))
    result = cur.fetchone()
    con.close()
    return result is not None

def count_watched():
    con, cur = connect_database()
    cur.execute("SELECT COUNT(*) FROM watched")
    result = cur.fetchone()
    con.close()
    return result[0]

def delete_watched(movie):
    con, cur = connect_database()
    cur.execute("DELETE FROM watched WHERE TMDB_ID=?", (movie["tmdb_id"],))
    con.commit()
    con.close()