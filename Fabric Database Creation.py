#!/usr/bin/env python
# coding: utf-8

# In[29]:


import sqlite3
from sqlite3 import Error
import pandas as pd

get_ipython().system('pip install --upgrade SQLAlchemy==1.4.46')



# In[30]:


# helper function to run SQL scripts
def execSQL(conn,query):
  conn.execute(query) # execute an SQL query
  conn.commit() # "commit" that query in order to make its action permanent

def allrowsSelect(conn,query):
    cursor = conn.execute(query)
    for row in cursor:
        print(row)
    
conn = sqlite3.connect("wardrobe_management.db") # creates the database if it is not already there.


# In[101]:


# This block contains all the queries used
# to create the tables in wardrobe_management.db
# Keep in mind that for efficiency purposes, may have to change data types
# Refer to notes for what each table is storing exactly

### table for user ###
# id: primary key for identifying unique individuals using the app, will increment as users are added
# created_at: timestamp of when account is created
createUserTable='''
CREATE TABLE IF NOT EXISTS user (
    id integer PRIMARY KEY autoincrement,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL, 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
'''

createCMD='''
CREATE TABLE movie (
	id integer PRIMARY KEY autoincrement,
	title text,
	director text,
	year text,
	runtime integer,
	genre text,
	budget real,
	gross real
);
'''
# futureplans... will create another table containing secure login information that
# can be tagged using user ID



### table for clothes ###
# id: primary key for identifying unique uploads of clothing on the app, will increment as photos are added
# name: user-assigned name to clothing
# type: type of clothing (shirt, pants, accessories)
# material: material clothing is made of (cotton, wool, cashmere)
# fit: how does clothes "fit" (loose/oversized, tight, fitted)
# comfortability: user assigned comfortability rating of 1-5 (example: jacket might be hard to wear but looks nice)

## COLOR ##
# optional for user to input
# notes... not sure how to identify color of uploaded image yet, will look into it

# primary_color: most used color in the piece 
# secondary_color: additional color(s) used
 

# user_id: foreign key to connect between users to help identify whose clothes it is
# image_link: cloud hosted image link of uploaded clothing
createClothesTable='''
CREATE TABLE IF NOT EXISTS clothing (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    material TEXT,
    fit TEXT,
    comfortability INTEGER,
    primary_color TEXT,
    secondary_color TEXT,
    user_id INTEGER,
    image_link TEXT,
    FOREIGN KEY (user_id) REFERENCES user(id)
);
'''
## futureplans... type, material, fit, comfortability are all categorical, 
# so when implementing frontend, we can just have buttons for users to pick from them
# example: when asked to input fit, we can have categories like oversized,loose,fitted,tight

### table for daily logs ###
# id: log id, primary key for this table
# user_id: id of the user who made log, foreign key for 'user' table
# date: date of the log, can change to CURRENT TIMESTAMP !!!
# clothing_id: clothing worn in logs, reference as foreign key to 'clothing' table
# weather: weather data based on given location (NOT SURE HOW TO IMPLEMENT THIS YET)
# notes: user-inputted notes of their choosing
createLogsTable='''
CREATE TABLE IF NOT EXISTS daily_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    date DATE NOT NULL,
    clothing_id INTEGER,
    weather TEXT,
    notes TEXT,
    FOREIGN KEY (clothing_id) REFERENCES clothing(id)
    FOREIGN KEY (user_id) REFERENCES user(id)
    
);
'''
## plans... since clothes should already be inputted into wardrobe for it to be logged,
## give users options based on their existing wardrobe

## executes the code to create logs
execSQL(conn,createUserTable)
execSQL(conn,createClothesTable)
execSQL(conn,createLogsTable)

## methods i need to make ##

allrowsSelect(conn,"select * from pragma_table_info('clothing')")

# remove clothing
# add clothing
# add log
# delete log
# print log



# In[91]:


# these functions do their job but do not yet account for duplicate values, need to fix to prevent security flaws

# add user
def addUser(username, email, password):
    checkDuplicateQuery = f'''
    SELECT 1 from user
    WHERE username = '{username}' OR email = '{email}'
    LIMIT 1;
    '''
    userExists = execSQL(conn,checkDuplicateQuery)
    
    if userExists:
        print("error, user already exists")
        return
        
    query = f'''
    INSERT INTO user (username, email, password) 
    VALUES ( '{username}', '{email}', '{password}');
    '''
    execSQL(conn, query)
    
# delete user
def deleteUser(email):
    query = f'''
    DELETE from user 
    WHERE email = '{email}';
    '''
    try:
        execSQL(conn, query)
    except:
        print('User does not exist!')

# get user info 
def getUserInfo(username):
    query = f'''
    SELECT * from user
    WHERE username = '{username}';
    '''
    allrowsSelect(conn,query)

# test cases



# In[99]:


#addUser('username1','gmail','foobar')
#addUser('username2','yahoo','barfoo')
#print('\n')
#addUser('username1','hotmail','barfoo')
#allrowsSelect(conn,'select * from user')


# In[100]:


#deleteUser('hotmail')
#deleteUser('gmail')
#deleteUser('yahoo')
#allrowsSelect(conn,'select * from user')


# In[ ]:


# add clothing

def addClothing(name, clothingType, material, fit, comfortability, primary_color, secondary_color, image_link):
    query=f'''
    '''
    execSQL(conn,query)

