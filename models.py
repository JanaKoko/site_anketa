#!/usr/bin/env python
# coding: utf-8

# In[6]:


from flask_sqlalchemy import SQLAlchemy


# In[7]:


db = SQLAlchemy()


# In[8]:


class Questions(db.Model):

    __tablename__ = "my_questions"
    type_id = db.Column('qu_id', db.Integer, primary_key=True)
    name = db.Column('qu_text', db.Text) # текстовое поле


# In[9]:


class People(db.Model):

    __tablename__ = "my_people"
    person_id = db.Column('pers_id', db.Integer, primary_key=True)
    gender = db.Column('gender', db.Text)
    age = db.Column('age', db.Text)


# In[5]:


class Answers(db.Model):
    
    __tablename__ = "my_answers"
    type_id = db.Column('id', db.Integer, primary_key=True)
    qu_id = db.Column('qu_id', db.Integer)
    answ = db.Column('answer', db.Text)
    person = db.Column('person_id', db.Integer)


# In[ ]:




