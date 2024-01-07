import sqlite3

# create .db file or connect to it if it exists
conn = sqlite3.connect("database.db")

# A cursor is an object used to make the connection for executing SQL queries.
c = conn.cursor()

# Create the table, read the article below if you
create_table_statement = """CREATE TABLE IF NOT EXISTS users (
  user_id INTEGER PRIMARY KEY,
  fname VARCHAR(20),
  lname VARCHAR(30),
  gender CHAR(1),
  email VARCHAR(30),
  password VARCHAR(30),
  joining DATE
);"""
c.execute(create_table_statement)
create_table_statement = """CREATE TABLE IF NOT EXISTS movies (
  movie_id INTEGER PRIMARY KEY,
  title VARCHAR(30),
  release_year VARCHAR(30),
  genre CHAR(30)
);"""
c.execute(create_table_statement)
create_table_statement = """CREATE TABLE IF NOT EXISTS reviews (
  review_id INTEGER PRIMARY KEY,
  user_id INTEGER,
  movie_id INTEGER,
  rating VARCHAR(20),
  review_date DATE
);"""
c.execute(create_table_statement)
create_table_statement = """CREATE TABLE IF NOT EXISTS actors (
  actor_id INTEGER PRIMARY KEY,
  movie_id INTEGER,
  actor_stagename VARCHAR(30),
  gender CHAR(1),
  fname VARCHAR(30),
  lname VARCHAR(30)
);"""
c.execute(create_table_statement)
conn.commit()
conn.close()
