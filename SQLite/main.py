import sqlite3

# create .db file or connect to it if it exists
conn = sqlite3.connect("database.db")

# A cursor is an object used to make the connection for executing SQL queries.
c = conn.cursor()
Validity1 = "yes"
def printTable():
    result = c.fetchall()
    for r in result:
        print(r)
def showAllRows():
  c.execute("SELECT * FROM users")
  print("Users")
  printTable()
  c.execute("SELECT * FROM movies")
  print("Movies")
  printTable()
  c.execute("SELECT * FROM reviews")
  print("Reviews")
  printTable()
  c.execute("SELECT * FROM actors")
  print("Actors")
  printTable()

def specificmovies():
  c.execute("SELECT * FROM movies")
  print("Movies")
  printTable()
  try:
    chosenmovie = int(input("Input the number of the movie that you want to see the reviews for"))
  except ValueError:
    print("\nThat's not a number!\n")
    specificmovies()

  if chosenmovie == 1:
    c.execute("SELECT * FROM reviews WHERE movie_id = 1 ")
    printTable()
  if chosenmovie == 2:
    c.execute("SELECT * FROM reviews WHERE movie_id = 2 ")
    printTable()
  if chosenmovie == 3:
    c.execute("SELECT * FROM reviews WHERE movie_id = 3 ")
    printTable()


def averagerating():
  c.execute("SELECT * FROM movies")
  print("Movies")
  printTable()
  try:
    chosenmovie = int(input("Input the number of the movie that you want to see the reviews for"))
  except ValueError:
    print("\nThat's not a number!\n")
    averagerating()
  if chosenmovie == 1:
    c.execute("SELECT AVG(rating) FROM reviews WHERE movie_id = 1")
    printTable()
  if chosenmovie == 2:
    c.execute("SELECT AVG(rating) FROM reviews WHERE movie_id = 2")
    printTable()
  if chosenmovie == 3:
    c.execute("SELECT AVG(rating) FROM reviews WHERE movie_id = 3")
    printTable()

def specificusers():
  c.execute("SELECT * FROM users")
  print("Users")
  printTable()
  try:
    chosenuser = int(input("Input the number of the movie that you want to see the reviews for"))
  except ValueError:
    print("\nThat's not a number!\n")
    specificusers()
  if chosenuser == 1:
    c.execute("SELECT * FROM reviews WHERE user_id = 1 ")
    printTable()
  if chosenuser == 2:
    c.execute("SELECT * FROM reviews WHERE user_id = 2 ")
    printTable()
  if chosenuser == 3:
    c.execute("SELECT * FROM reviews WHERE user_id = 3 ")
    printTable()


while Validity1 == "yes":
  options = """What would you like to do?\n
	1. See all rows in the database
	
    2. See all the reviews for a certain movie
    
    3. See the average of the reviews for a certain movie
    
    4. See all the reviews made by a certain user"""

  print(options)
  inp = input()
  if inp == "1":
    showAllRows()
  if inp == "2":
    specificmovies()

  if inp == "3":
    averagerating()

  if inp == "4":
    specificusers()

  else:
    print("Invalid choice, please try again.")
  Validity1 = (input("would you like to do select another feature?")).casefold()

# Fetch the data
c.execute("SELECT * FROM users")
c.execute("SELECT * FROM movies")
c.execute("SELECT * FROM reviews")
c.execute("SELECT * FROM actors")