import psycopg2
conn = psycopg2.connect(host = "localhost",dbname = "postgres", user = "postgres",password= "admin", port = 5432)

cur = conn.cursor()
cur.execute("""DROP TABLE IF EXISTS produkti""")
cur.execute("""DROP TABLE IF EXISTS person""")
cur.execute("""DROP TABLE IF EXISTS dobavitelji""")
cur.execute("""DROP TABLE IF EXISTS dobava""")
cur.execute("""DROP TABLE IF EXISTS prisli_prihodi""")
cur.execute("""DROP TABLE IF EXISTS dob_podjetja""")
cur.execute("""DROP TABLE IF EXISTS nar_podjetja""")
cur.execute("""DROP TABLE IF EXISTS odprema""")
cur.execute("""DROP TABLE IF EXISTS narocila""")

cur.execute ("""CREATE TABLE IF NOT EXISTS person (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            gender CHAR);""")

cur.execute ("""CREATE TABLE IF NOT EXISTS prisli_prihodi (
            prisli_prihodID INT PRIMARY KEY,
            ime_podjetja VARCHAR(255),
            ime_produkta VARCHAR(255),
            kolicina INT,
            datum VARCHAR(255),
            ura VARCHAR(255),
            opombe VARCHAR(255)
    
            );""")


cur.execute ("""CREATE TABLE IF NOT EXISTS dob_podjetja (
            ime_podjetja VARCHAR(255) PRIMARY KEY,
            telefonska_stevilka VARCHAR(15),
            naslov VARCHAR(100));""")

cur.execute ("""CREATE TABLE IF NOT EXISTS nar_podjetja (
            ime_podjetja VARCHAR(255) PRIMARY KEY,
            telefonska_stevilka VARCHAR(15),
            naslov VARCHAR(100));""")


cur.execute ("""CREATE TABLE IF NOT EXISTS produkti (
            ime_produkta VARCHAR(255) PRIMARY KEY,
            kolicina INT,
            enota VARCHAR(255)
            );""")
    #prihodi:
cur.execute ("""CREATE TABLE IF NOT EXISTS dobava (
            prihodID INT PRIMARY KEY,
            ime_podjetja VARCHAR(255),
            ime_produkta VARCHAR(255),
            kolicina INT,
            datum VARCHAR(255),
            ura VARCHAR(255),
            prislo VARCHAR(2)
            );""")
    #narocila:
cur.execute ("""CREATE TABLE IF NOT EXISTS odprema (
            narociloID INT PRIMARY KEY,
            ime_podjetja VARCHAR(255),
            ime_produkta VARCHAR(255),
            kolicina INT,
            datum VARCHAR(255),
            ura VARCHAR(255),
            prislo VARCHAR(2)
            );""")

cur.execute("""INSERT INTO dob_podjetja VALUES ('NIKE','123412346','Slovenska cesta 35, Ljubljana'),('Microsoft','234656895','Slovenska cesta 40, Ljubljana'),
('merkator','031 451 142','Pot do kranja, Kranj')""")

cur.execute("""INSERT INTO nar_podjetja VALUES ('Merkator','123412346','Slovenska cesta 35, Ljubljana'),('Lidl','234656895','Slovenska cesta 40, Ljubljana')""")


cur.execute("""INSERT INTO odprema VALUES (1,'Merkator','jabolka',20,'1.1.2024','13.30','ne'),(2,'Lidl','hruske',10,'1.4.2024','12.30','ne')""")

cur.execute("""INSERT INTO dobava VALUES (1,'NIKE','sandali',10,'18.11.2024','13.30','ne'),(2,'Microsoft','tipkovnice',20,'18.9.2024','13.30','ne'),
(3,'merkator','jabolka',1000,'18.1.2024','10.00','da'),(4,'merkator','jabolka',1340,'18.3.2024','9.50','da'),(5,'merkator','jabolka',250,'18.1.2025','12.50','ne'),(6,'NIKE','čevlji',50,'23.5.2024','7.00','ne')
,(7,'Microsoft','računalniki',10,'1.9.2024','14.00','ne')""")



cur.execute("""INSERT INTO produkti VALUES ('jabolka',30,'kg'),
('banane',20,'kg'),('hruške',10,'kg'),('steklene flaše',20,'kosov'),('leseni stoli',0,'kosov')""")








cur.execute("""UPDATE person
SET name = 'luka'
WHERE id = 1;""")


cur.execute("""SELECT * FROM person WHERE name ='mik';""")

a = cur.fetchone()



cur.execute("""SELECT * FROM person WHERE name = 'kayle';""")
#sprint(cur.fetchall())












conn.commit()
cur.close()
conn.close()
