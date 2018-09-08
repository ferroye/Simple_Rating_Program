# run this file to pre populate DB on your PC
import sqlite3
# connect to DB and create tables
def openDB(dbname):
    conn=sqlite3.connect(dbname)
    c = conn.cursor()
    return c, conn
# this function will drop all the tables call it if you need to. or you can delete the db file.
def drop_allTables(tname):
    # Please do not use it
    print('****DELETING TABLES****...')
    conn=sqlite3.connect(tname)
    c = conn.cursor()
    c.execute('drop table crating')
    c.execute('drop table prating')
    c.execute('drop table comt')
    c.execute('drop table course')
    c.execute('drop table professor')
    c.execute('drop table user')
    c.close
    conn.close()
# this function will create all the tables
def creatingtables(tname):
    c, conn=openDB(tname)
    # tables for us to track informations
    c.execute('create table IF not EXISTS user(username TEXT PRIMARY KEY, password TEXT, major TEXT )')
    c.execute('CREATE TABLE IF NOT EXISTS course(CID INT PRIMARY KEY,cname TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS professor(PID INTEGER PRIMARY KEY,PName TEXT, CID INT,FOREIGN KEY (CID) REFERENCES course(CID) )')
    c.execute('CREATE TABLE IF NOT EXISTS comt(cmt TEXT, PID INTEGER not null , FOREIGN KEY (PID) REFERENCES professor(PID))')
    c.execute('CREATE TABLE IF NOT EXISTS prating(rating INTEGER,PID INTEGER not null, FOREIGN KEY (PID) REFERENCES professor(PID) )')
    c.execute('CREATE TABLE IF NOT EXISTS crating(rating INTEGER,CID INTEGER not null, FOREIGN KEY (CID) REFERENCES course(CID) )')
    #c.execute('CREATE TABLE IF NOT EXISTS taught(PID, CID,FOREIGN KEY (PID) REFERENCES professor(PID), FOREIGN KEY (CID) REFERENCES course(CID) )')
    c.close()
    conn.close()

def populate_tabales(db):
    c, conn=openDB(db)
    #populate course
    c.execute("INSERT INTO course VALUES(1,'CSAD402' )")
    c.execute("INSERT INTO course VALUES(2,'GASD403' )")
    c.execute("INSERT INTO course VALUES(3,'FLSJ404' )")
    c.execute("INSERT INTO course VALUES(4,'ZXVK302' )")
    
    #populate user
    c.execute("INSERT INTO user VALUES('username','password','Business')")
    c.execute("INSERT INTO user VALUES('mike123','123123','Business')")
    #populate professor
    c.execute("INSERT INTO professor VALUES(100,'Woei-Jyh Lee',1) ")
    c.execute("INSERT INTO professor VALUES(101,'Hassan Ibrahim',2) ")
    c.execute("INSERT INTO professor VALUES(102,'Wei Chen',3) ")
    c.execute("INSERT INTO professor VALUES(103,'Scott E. Hudson',4) ")
    #populate comt
    c.execute("INSERT INTO comt VALUES('I would skip class whenever there was not an in class quiz',100 )")
    c.execute("INSERT INTO comt VALUES('Pretty good professor. His lectures are not the most interesting but there not completely boring either.',100 )")
    c.execute("INSERT INTO comt VALUES('Fun class',102 )")
    c.execute("INSERT INTO comt VALUES('Professor Hudson is not the best teacher out there.',103 )")
    c.execute("INSERT INTO comt VALUES('Assignments were easy if you are computer friendly.',101 )")
    c.execute("INSERT INTO comt VALUES(' He makes the class enjoyable by telling jokes and relating course material to real life situations.',102 )")
    # populate professor rating
    c.execute("INSERT INTO prating VALUES(3,100)")
    c.execute("INSERT INTO prating VALUES(4,101)")
    c.execute("INSERT INTO prating VALUES(5,102)")
    c.execute("INSERT INTO prating VALUES(3,103)")
    #populate course rating 
    c.execute("INSERT INTO crating VALUES(4,1)")
    c.execute("INSERT INTO crating VALUES(4,2)")
    c.execute("INSERT INTO crating VALUES(5,3)")
    c.execute("INSERT INTO crating VALUES(4,4)")


    conn.commit()
    print("insert complete!")
    c.close()
    conn.close()
drop_allTables('xxx')
creatingtables('xxx')
populate_tabales('xxx')
