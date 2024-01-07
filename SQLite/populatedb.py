import sqlite3

# create .db file or connect to it if it exists
conn = sqlite3.connect("database.db")

# A cursor is an object used to make the connection for executing SQL queries.
c = conn.cursor()
# Insert a demo user into our database
insert_statement = """INSERT INTO users (fname,lname,gender,email,password,joining) VALUES ("Bat", "Man", "M", "batman@gmail.com" ,"ff6449b73d9d4dab8428cb731b926d99ceed3ab4","2014-03-28");"""
c.execute(insert_statement)

insert_statement = """INSERT INTO users (fname,lname,gender,email,password,joining) VALUES ("Spider", "Man", "M", "spiderman@gmail.com", "ddf714b52cfc85f22c2827f7040820f7f058ea57","2014-03-29");"""
c.execute(insert_statement)

insert_statement = """INSERT INTO users (fname,lname,gender,email,password,joining) VALUES ("Super", "Man", "M","superman@gmail.com" ,"431175673e6c3c8f0e53fd038349b2b845fd2a80","2014-03-30");"""
c.execute(insert_statement)

insert_statement = """INSERT INTO movies (title,release_year,genre) VALUES ("The Fellowship Of The Ring","2001","adventure");"""
c.execute(insert_statement)

insert_statement = """INSERT INTO movies (title,release_year,genre) VALUES ("The Two Towers","2002","adventure");"""
c.execute(insert_statement)

insert_statement = """INSERT INTO movies (title,release_year,genre) VALUES ("The Return Of The King","2003","adventure");"""
c.execute(insert_statement)

insert_statement = """INSERT INTO actors (movie_id,actor_stagename,gender,fname,lname) VALUES ("1","Frodo Baggins","M","Elijah", "Wood");"""
c.execute(insert_statement)

insert_statement = """INSERT INTO actors (movie_id,actor_stagename,gender,fname,lname) VALUES ("2","Samwise Gamgee","M","Sean", "Astin");"""
c.execute(insert_statement)

insert_statement = """INSERT INTO actors (movie_id,actor_stagename,gender,fname,lname) VALUES ("3","Aragorn","M","Viggo", "Mortensen");"""
c.execute(insert_statement)

insert_statement = """INSERT INTO reviews (user_id,movie_id,rating,review_date) VALUES ("1","1","4.5","01-01-2001");"""
c.execute(insert_statement)

insert_statement = """INSERT INTO reviews (user_id,movie_id,rating,review_date) VALUES ("2","1","5.0","01-01-2001");"""
c.execute(insert_statement)

insert_statement = """INSERT INTO reviews (user_id,movie_id,rating,review_date) VALUES ("3","1","4.5","01-01-2001");"""
c.execute(insert_statement)

insert_statement = """INSERT INTO reviews (user_id,movie_id,rating,review_date) VALUES ("1","2","4.0","02-01-2001");"""
c.execute(insert_statement)

insert_statement = """INSERT INTO reviews (user_id,movie_id,rating,review_date) VALUES ("2","2","4.5","02-01-2001");"""
c.execute(insert_statement)

insert_statement = """INSERT INTO reviews (user_id,movie_id,rating,review_date) VALUES ("3","2","4.0","02-01-2001");"""
c.execute(insert_statement)

insert_statement = """INSERT INTO reviews (user_id,movie_id,rating,review_date) VALUES ("1","3","5.0","03-01-2001");"""
c.execute(insert_statement)

insert_statement = """INSERT INTO reviews (user_id,movie_id,rating,review_date) VALUES ("2","3","5.0","03-01-2001");"""
c.execute(insert_statement)

insert_statement = """INSERT INTO reviews (user_id,movie_id,rating,review_date) VALUES ("3","3","5.0","03-01-2001");"""
c.execute(insert_statement)


conn.commit()
conn.close()