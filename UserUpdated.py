import sqlite3
import sys
print("Welcome to our application! ")
print("........")
print("This application will provide the rating for any course and professor.")
print()
# read me file
# open connection 
conn=sqlite3.connect('xxx.db')
c = conn.cursor()
# function to check if the user is existed or not
def check_user_occur(uname, pwd):
    # not working  dk why now....
    q = 'SELECT * FROM user where user.username =\"'+uname+'\"'
    c.execute(q)
    data = c.fetchall()
   
    if(len(data)!= 0):
        print('username existed')
        return 1
    else:
        return 0
# this function support to add new user
def add_new_Use(uname,pwd, major):
    ck = check_user_occur(uname,pwd)
    if(ck ==1):
        print('Please choose another username')
        return 1
    sql = '''INSERT INTO user(username, password, major) VALUES ( ?, ?, ?)'''
    c.execute(sql, (uname, pwd, major))
    conn.commit()
    return 0
# listing course rating for specific course
def check_course_rating(rd):
    print("Listing specific course : "+rd+'..')
    print('-------------------------------')
    print('Course  |  Rating ')
    q= '''select * from course c, crating r  where c.CID = r.CID AND  c.cname like (?) '''
    c.execute(q, ('%'+rd+'%',))
    data= c.fetchall()
    for x in data:
        print( x[1] ,"  ", x[2],'/5' )
    input("enter anything to continue")
    return 0 

def list_courses(rd):
    print("Listing all course: ")
    print('-----------------')
    print('Course  |  Rating ')
    q = 'select * from course c, crating r where c.CID = r.CID'
    c.execute(q)
    data = c.fetchall()
    for x in data:
        print( x[1] ,"  ", x[2],'/5' )
    input("enter anything to continue")
    return 0
# list specific professor rating
def check_prof_rating(rd):
    print("Listing specific course : "+rd+'..')
    print('-------------------------------')
    print('Course  |  Rating ')
    q= '''select * from professor c, prating r  where c.PID = r.PID AND  c.PName like (?)'''
    c.execute(q, ('%'+rd+'%',))
    data= c.fetchall()
    for x in data:
        print( x[1] ,"  ", x[3],'/5' )
    input("enter anything to continue")
    return 0 
# list all professor rating 
def list_professorsRat(rd):
    print("Listing all professors: ")
    print('-----------------------')
    q = 'select * from professor p, prating pr  where p.PID = pr.PID'
    c.execute(q)
    data = c.fetchall()
    for x in data:
        print(x[1] ,"  ", x[3],'/5'  )
    input("enter anything to continue")
    return 0
# list all professor comments
def list_professors_cmt(rd):
    print("Listing all professors: ")
    print('-----------------------')
    print('Professors  |  Comments ')
    q = 'select * from professor p, comt c where p.PID = c.PID '
    c.execute(q)
    data = c.fetchall()
    for x in data:
        print(x[1],'<=>', x[3])
    input("enter anything to continue")
    return 0

def check_prof_cmt(rd):
    print("Listing specific Professor : "+rd+'..')
    print('-------------------------------')
    print('Professor  |  Comments ')
    q= '''select * from professor c, comt r  where c.PID = r.PID AND  c.PName like (?)'''
    c.execute(q, ('%'+rd+'%',))
    data= c.fetchall()
    for x in data:
        print( x[1] ,"  :  ", x[3], )
    input("enter anything to continue")
    return 0 
def check_user(uname, pwd):
    # not working  dk why now....
    q = 'SELECT * FROM user where user.username =\"'+uname+'\"and user.password =\"'+pwd+'\" '
    c.execute(q)
    data = c.fetchall()

    if(len(data)!= 0):
        print()
        print('You have logged in')
        return 1
    else:
        print('login failed')
        print('Please signin with correct information..')
        return 0
#process when user entered professor
# then it will call other sub fucntion to do the actual tasks
def prof_func():
        while True:
            print()
            print()
            cursespec=input('Now Enter the letter for the following Options: Please Enter Letters A,B,C, etc...'
            '\nA: List all professor Rating  :'
            '\nB: View rating for specific professor: '
            '\nC: List all professor Comment'
            '\nD: Check specific professor Comment '
            '\nE: List all Courses Rating '
            '\nF: View rating for specific course'
            '\nX: Exit: ')
            cursespec=cursespec.lower()
            print()
            if 'a'==cursespec:
                list_professorsRat('')
            elif cursespec =='b':
                rd = input("Typed in a professor name that you want to search")
                check_prof_rating(rd)
            elif cursespec =='c':
                list_professors_cmt("")
            elif cursespec=='d':
                rd = input("Typed in a professor name that you want to search")
                check_prof_cmt(rd)
            elif cursespec=='e':
                list_courses("")
            elif cursespec =='f':
                rd = input("Typed in a specific course that you want to search. For example:BMGT404 ...  :  ")
                check_course_rating(rd)
            else:
                print('I was not quite sure what you have there. Can you type A letter? ')
               

# App starts here this part of the code is for user to enter their username and password
while True: 
    signup= input('Are you a new User? Please type Yes if you are new here or  press any key to login : ')
    # if the user is new here then register his username and password
    if(signup.lower() == 'yes'):
        # this is signup using insert 
        while True:
            username = input('Please create your username: ')
            password = input('Please create your password: ')
            major = input('Please enter your major: ')
            r = add_new_Use(username, password,major)
            if(r!=0):
                d = input('Press N to end of this program if you do not want to re-enter your info..  Press anything to continue')
                if(d.lower()=='n'):
                    sys.exit()
                else:
                    continue
            else:
                print('Good job! You have created an account!')
                # this is also have the part that the user need can do stuff
                break
        break
    else:
        username = input('Please enter your username: ')
        password = input('Please enter your password: ')
        ck = check_user(username, password)
        if(ck !=1):
            continue
        else:
            # task what the user want to do and check
            # success so to continue to allow program to preforme tasks
            print('Log in Successful..')
            print()
            break
# after they log in then do some task it will be in to TBC part
#close connection
print()
print('Hello, My name is Alice, I have been programed to help you'
    '\nI can help you with success at The University of Maryland')
while True:
    prof_func()
    rd = input('press anything to continue, \nplease enter exit if you wish to quit: ')
    if rd.lower()=='exit':
        sys.exit()
    else:
        continue
c.close()
conn.close()







