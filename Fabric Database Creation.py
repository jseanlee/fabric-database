#!/usr/bin/env python
# coding: utf-8

# In[36]:


import sqlite3
from sqlite3 import Error
import pandas as pd

get_ipython().system('pip install --upgrade SQLAlchemy==1.4.46')



# In[ ]:


# helper function to run SQL scripts
def execSQL(conn,query):
  conn.execute(query) # execute an SQL query
  conn.commit() # "commit" that query in order to make its action permanent
    
conn = sqlite3.connect("wardrobe_management.db") # creates the database if it is not already there.


# In[46]:


# This block contains all the queries used
# to create the tables in wardrobe_management.db
# Keep in mind that for efficiency purposes, may have to change data types
# Refer to notes for what each table is storing exactly

### table for user ###
# id: primary key for identifying unique individuals using the app, will increment as users are added
# created_at: timestamp of when account is created
createUser='''
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
createClothes='''
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
createLogs='''
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
execSQL(conn,createUser)
execSQL(conn,createClothes)
execSQL(conn,createLogs)

## methods i need to make ##

# add user
# remove clothing
# add clothing
# add log
# delete log
# print log


# In[ ]:




