README


I. Getting Started: 
1.first import sqlite3 and download the sqlite3 brower database
http://sqlitebrowser.org/

Note: this program can be run on cmd if you wish to run on anaconda please provide specific path for the db file. 

2. run AdminBMGT404.py -- python AdminBMGT404.py
this script allows user to pre populate database -> sqlite3 
bmgt404.db will be generated under your file path where you have AdminBMGT404.
if you run into any error please check your admin access.
Please remove the file if you want to run AdminBMGT404 again.



II. Use the application
1.Run userBMGT404.py - python userBMGT404.py
2.Enter keyword


# we do not have much tables. in real world there could be a lot of tables which we do not have.
# for example course can have Prerequisite. which we do not have. 
# rating to calculate rating for each professors. using complex sql which cause lots of work we will ommit.
# no password validation.