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



def Q1(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q1: Prints the full Table")

    cursor = conn.execute('''SELECT name
    FROM Charachter;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0])
    for item in queries:
        print(item[0])
            

    print("++++++++++++++++++++++++++++++++++")

def Q2(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q2: Print all earthquakes in Greece")

    cursor = conn.execute('''SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    AND n_nationkey = 3
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|" ,Column_header[7],"|",Column_header[8],"|")
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")


def Q3(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q3: Prints all earthquakes in Italy")

    cursor = conn.execute('''SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    AND n_nationkey = 2
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|" )
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")


def Q4(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q4: Only prints earthquakes in Japan")

    cursor = conn.execute('''SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    AND n_nationkey = 1
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|" )
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")

def Q5(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q5: Prints all causes of an earthquake")

    cursor = conn.execute('''SELECT DISTINCT c_natural
    FROM CAUSE
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print("|",Column_header[0],"|")
    for item in queries:
        print(item[0])
            

    print("++++++++++++++++++++++++++++++++++")


def Q6(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q6: prints earthquakes based on date(new to old)")

    cursor = conn.execute('''SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    ORDER BY d_date DESC
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|" )
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")

def Q7(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q7: prints earthquakes based on date(old to new)")

    cursor = conn.execute('''SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    ORDER BY d_date ASC
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|",Column_header[7],"|",Column_header[8],"|" )
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")


def Q8(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q8: prints Earthquakes based on depth (hi to low)")

    cursor = conn.execute('''SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    ORDER BY s_depth ASC
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|",Column_header[7],"|",Column_header[8],"|" )
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")

def Q9(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q9: prints Earthquakes based on depth (low to hi)")

    cursor = conn.execute('''SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    ORDER BY s_depth DESC
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|",Column_header[7],"|",Column_header[8],"|" )
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")

def Q10(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q10: prints the location of earthquakes")

    cursor = conn.execute('''SELECT n_name as country, l_longitude as longitude, l_latitude as latitude
    FROM NATION, LOCATION
    WHERE l_nationKey = n_nationKey
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|")
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|")
            

    print("++++++++++++++++++++++++++++++++++")




def main():
    database = r"SSBU/smash.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        bru = 10
        while(bru == 10):
            print('''These are your Options:\n 
        1. Which Charachters have the same moves\n
        2. Charachter Search \n
        3. All charachters in a franchise\n
        ''')
            val = int(input())

            if(val == 1):
                Q1(conn)
            elif(val == 3):
                bru = 1
      
    closeConnection(conn, database)


if __name__ == '__main__':
    main()