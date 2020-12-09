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
    age = db.Column('age', db.Integer)
    english = db.Column('eng', db.Text)


# In[5]:


class Answers(db.Model):

    __tablename__ = "my_answers"
    pers_id = db.Column('pers_id', db.Integer, primary_key=True)
    one = db.Column('one', db.Integer)
    two = db.Column('two', db.Text)
    three = db.Column('three', db.Text)


# In[ ]:



