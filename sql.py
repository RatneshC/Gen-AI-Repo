#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sqlite3


# In[5]:


connection = sqlite3.connect("student.db")


# In[6]:


cursor=connection.cursor()


# In[7]:


table_info="""  CREATE TABLE STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT) """


# In[8]:


cursor.execute(table_info)


# In[9]:


cursor.execute('''INSERT INTO STUDENT VALUES ('RATNESH','DATA SC','A',60) ''')
cursor.execute('''INSERT INTO STUDENT VALUES ('RATNESH2','DATA SC2','A2',62) ''')
cursor.execute('''INSERT INTO STUDENT VALUES ('RATNESH3','DATA SC3','A3',63) ''')
cursor.execute('''INSERT INTO STUDENT VALUES ('RATNESH4','DATA SC4','A4',64) ''')
cursor.execute('''INSERT INTO STUDENT VALUES ('RATNESH5','DATA SC5','A5',65) ''')
cursor.execute('''INSERT INTO STUDENT VALUES ('RATNESH6','DATA SC6','A6',66) ''')
cursor.execute('''INSERT INTO STUDENT VALUES ('RATNESH7','DATA SC7','A7',67) ''')
cursor.execute('''INSERT INTO STUDENT VALUES ('RATNESH8','DATA SC8','A8',68) ''')


# In[14]:


print("Inserted data successfully")


# In[15]:


data = cursor.execute(''' select * from STUDENT''')


# In[16]:


for row in data:
    print(row)


# In[18]:


connection.commit()
connection.close()


# In[ ]:




