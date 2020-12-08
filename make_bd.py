#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[3]:


conn = sqlite3.connect('anketa.db')
cur = conn.cursor()


# In[4]:


cur.execute("""
CREATE TABLE IF NOT EXISTS my_questions 
(qu_id int PRIMARY KEY, qu_text text)
""")

conn.commit()

cur.execute("""
CREATE TABLE IF NOT EXISTS my_people 
(pers_id int PRIMARY KEY, gender text, age text)
""")

conn.commit()


cur.execute("""
CREATE TABLE IF NOT EXISTS my_answers
(id int PRIMARY KEY, qu_id int, answ text, person_id int)
""")

conn.commit()


# In[ ]:




