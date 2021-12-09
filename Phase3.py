import sqlite3
from sqlite3 import Error


def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def Q0(conn):
    cursor = conn.execute('''SELECT Charachter.name AS Name,
    Franchise.fran_name AS 'Franchise'
    FROM Charachter,
    Franchise
    WHERE Franchise.fran_id = Charachter.fran_id;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],'|', Column_header[1])
    for item in queries:
        print(item[0],'|', item[1])


def Q1(conn, charname):
    print("++++++++++++++++++++++++++++++++++")
    #displays charachters and franchise
    cursor = conn.execute('''SELECT Charachter.name AS Name,
    Tier.tier AS 'Tier',
    Franchise.fran_name AS 'Franchise'
    FROM Charachter,
    Tier,
    Franchise
    WHERE Tier.tier_id = Charachter.tier_id
    AND Franchise.fran_id = Charachter.fran_id
    AND Charachter.name Like ?;''', ("{}%".format(charname),))
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],'|', Column_header[1],'|', Column_header[2])
    for item in queries:
        print(item[0],'|', item[1],'|', item[2])
            

    print("++++++++++++++++++++++++++++++++++")

def Q2(conn, charname):
    print("++++++++++++++++++++++++++++++++++")

    cursor = conn.execute('''SELECT Charachter.name AS Name,
    Franchise.fran_name AS 'From'
    FROM Charachter,
    Franchise
    WHERE Charachter.fran_id = Franchise.fran_id
    AND Franchise.fran_name LIKE ?;''', ("%{}%".format(charname),))
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],'|', Column_header[1])
    for item in queries:
        print(item[0],'|', item[1])
            


    print("++++++++++++++++++++++++++++++++++")


def Q3(conn):
    print("++++++++++++++++++++++++++++++++++")


    cursor = conn.execute('''SELECT Charachter.name AS Shadow,
    OG.name AS Original
    FROM Charachter,
    Charachter AS OG,
    Shadow_Fighter
    WHERE Charachter.char_id = Shadow_Fighter.shadow_id
    AND OG.char_id = Shadow_Fighter.og_id;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1])
    for item in queries:
        print(item[0] ,"|", item[1])
            

    print("++++++++++++++++++++++++++++++++++")


def Q4(conn):
    print("++++++++++++++++++++++++++++++++++")

    cursor = conn.execute('''SELECT fran_name AS 'Franchise',
    name AS 'Name',
    tier AS 'Tier'
    FROM DLC,
    Charachter,
    Tier,
    Franchise
    WHERE Charachter.char_id = DLC.char_id
    AND Franchise.fran_id = DLC.fran_id
    AND Charachter.tier_id = Tier.tier_id;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2])
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2])
            

    print("++++++++++++++++++++++++++++++++++")

def Q5(conn, tier):
    print("++++++++++++++++++++++++++++++++++")

    cursor = conn.execute('''SELECT Charachter.name AS Name,
    Tier.tier AS 'Tier',
    Franchise.fran_name AS 'Franchise'
FROM Charachter,
    Tier,
    Franchise
WHERE Tier.tier_id = Charachter.tier_id
  AND Franchise.fran_id = Charachter.fran_id
  AND Tier.tier LIKE ?;''', ("%{}%".format(tier),))
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2])
    for item in queries:
        print(item[0],'|',item[1],'|',item[2])
            

    print("++++++++++++++++++++++++++++++++++")


def Q6(conn, name):
    print("++++++++++++++++++++++++++++++++++")

    cursor = conn.execute('''SELECT Charachter.name AS 'Charachter',
    Tier.tier AS 'Tier',
    GSP.EGSP AS 'GSP'
    FROM Charachter,
    GSP,
    Tier
    WHERE Charachter.char_id = GSP.char_id
    AND Charachter.tier_id = Tier.tier_id
    AND Charachter.name LIKE ?''', ("{}%".format(name),))
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2])
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2])
            

    print("++++++++++++++++++++++++++++++++++")

def Q7(conn):
    print("++++++++++++++++++++++++++++++++++")

    cursor = conn.execute('''SELECT player AS 'Player',
    Charachter.name AS 'Main',
    Tier.tier AS 'Tier',
    OG.name AS 'Alt',
    alt_tier.tier AS 'Tier'
    FROM Pros,
    Charachter,
    Tier,
    Charachter AS OG,
    Tier AS alt_tier
    WHERE Charachter.char_id = Pros.main
    AND Tier.tier_id = Charachter.tier_id
    AND OG.char_id = Pros.Alt
    AND alt_tier.tier_id = OG.tier_id''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4])
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4])
            

    print("++++++++++++++++++++++++++++++++++")


def Q8(conn):
    print("++++++++++++++++++++++++++++++++++")
    print('What is the charachters name?')
    name = input()
    print('insert charachter ID:')
    charid = int(input())
    print('insert Franchise ID:')
    franid = int(input())
    print('insert tier ID:')
    tierid = int(input())

    conn.execute('''INSERT INTO Character(name, char_id, fran_id, tier_id) VALUES(:name, :charid, :franid, :tierid);''', 
    {'name': name, 'charid': charid, 'franid': franid, 'tierid': tierid})
    conn.commit()
            

    print("++++++++++++++++++++++++++++++++++")

def Q9(conn):
    print("++++++++++++++++++++++++++++++++++")

    print('What is the charachters name?')
    name = input()
    print('insert Franchise ID:')
    franid = int(input())

    conn.execute('''INSERT INTO Franchise(fran_name, fran_id) VALUES(:name, :franid);''', 
    {'name': name,'franid': franid})
    conn.commit()
            

    print("++++++++++++++++++++++++++++++++++")

def Q10(conn):
    print("++++++++++++++++++++++++++++++++++")
    print('insert Franchise ID:')
    name = input()
    print('insert franchise ID:')
    franid = int(input())

    conn.execute('''INSERT INTO Franchise(fran_name, fran_id) VALUES(:name, :franid);''', 
    {'name': name,'franid': franid})
    conn.commit()

    print("++++++++++++++++++++++++++++++++++")

def option1(conn):
  exit = True
  while(exit):
    print('''Welcome to Charachters\n
    1. search for a charachter based on name\n
    2. search for a charachter based on franchise\n
    3. see which charachters have the same moves\n
    4. see which charachters are DLC specific\n
    5. Look for charachters in a specific tier (S-F)\n
    6. return to Main Menue\n''')

    choice = int(input())
    
    if (choice == 1):
      print("What is the name of the charachter your looking for?")
      charname = input()
      Q1(conn, charname)

    if(choice == 2):
        print("What Franchise would you like to search for?")
        franName = input()
        Q2(conn, franName)

    if(choice == 3):
        Q3(conn)

    if(choice == 4):
        Q4(conn)
    
    if(choice == 5):
        print("What Tier would you like to see?")
        tier = input()
        Q5(conn, tier)

    if(choice == 6):
      exit = False
  
  exit = True

def option2(conn): 
  exit2 = True
  while(exit2):
    print('''Welcome to Elite Smash\n
    Elite Smash is a special mode of online play reserved\n
    for the top 10% players.\n
    1. Search for a charachters GSP requirement for elite Smash\n
    2. Show Pros and who they play\n
    3. return to Main Menue\n''')

    choice2 = int(input())
    
    if (choice2 == 1):
        print("What Charachter are you looking for?")
        name = input()
        Q6(conn, name)

    if(choice2 == 2):
        Q7(conn)

    if(choice2 == 3):
      exit2 = False
  
  exit2 = True



def option3(conn):#1. has 2 queries in one option 
  exit3 = True
  while(exit3):
    print('''You now have access to the database\n
    you can\n
    1. Add a Charachter to the database\n  
    2. Add a new franchise\n
    3. return to Main Menue\n
    ''') 

    choice3 = int(input())
    
    if (choice3 == 1):
        Q8(conn)

    if(choice3 == 2):
        Q9(conn)

    if(choice3 == 3):
      exit3 = False
  
  exit3 = True

#if(answer is yes):
#  switch to a query with requirments;
#else:
#  use og query

def main():
    database = r"smash.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        bru = 10
        while(bru == 10):
            Q0(conn)
            print('''Welcome to the Main Menue your Options are:\n 
        1. Charachters
        2. Pros's and Elite Smash
        3. ADD to database
        4. Exit  
        ''')
            val = int(input())

            if(val == 1):
                option1(conn)

            elif(val == 2):
                option2(conn)

            elif(val == 3):
                option3(conn)

            elif(val ==4 ):
              bru = 1

      
    closeConnection(conn, database)


if __name__ == '__main__':
    main()