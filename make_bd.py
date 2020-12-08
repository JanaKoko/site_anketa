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
(pers_id int PRIMARY KEY, gender text, age text, eng text)
""")

conn.commit()


cur.execute("""
CREATE TABLE IF NOT EXISTS my_answers
(pers_id int PRIMARY KEY, one int, two text, three text)
""")


quest = [(1, 'Оцените предложение по шкале от 1 до 5. Предложение: Можете пожалуйста пройти опрос?'),
         (2, 'Выберите то, что наиболее правильно характеризует вас (о себе)'),
         (3, 'Выберите то, что наиболее правильно характеризует вас (о других)')]

cur.executemany("""
INSERT INTO my_questions VALUES (?, ?)""", quest)

conn.commit()


# In[ ]:




