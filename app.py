#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables


# In[2]:


import os


# In[3]:


import sqlite3


# In[4]:


import google.generativeai as genai


# In[5]:


genai.configure(api_key="AIzaSyAlTbZ1qTh6AW5Zi017yEWF_0sXykionvs")


# In[ ]:





# In[6]:


def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text


# In[7]:


def read_sql_query(sql,db):
    conn=sql.connect(db)
    cur=conn.cursor(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


# In[8]:


def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


# In[9]:


## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """


]


# In[10]:


## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")


# In[11]:


# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("The REsponse is")
    for row in response:
        print(row)
        st.header(row)


# In[ ]:





# In[ ]:




