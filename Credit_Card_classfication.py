#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as ps
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default ="plotly_white"


# In[3]:


data=ps.read_csv("train.csv")


# In[4]:


print(data.head())


# In[5]:


print(data.info())


# In[6]:


print(data.isnull().sum())


# In[7]:


data["Credit_Score"].value_counts()


# In[8]:


fig1=px.box(data,
           x="Occupation",
           color="Credit_Score",
           title="Credit Scores Based on Occupation",
           color_discrete_map={"Poor":"red",
                              "Standard":"Yellow",
                              "Good":"green"})


# In[9]:


fig1.show()


# In[13]:


fig2=px.box(data,
           x="Credit_Score",
            y="Annual_Income",
           color="Credit_Score",
           title="Credit Scores Based on Annual Income",
           color_discrete_map={"Poor":"red",
                              "Standard":"Yellow",
                              "Good":"green"})


# In[14]:


fig2.update_traces(quartilemethod="exclusive")


# In[17]:


#Based on Montly Income


# In[19]:


fig3=px.box(data,
           x="Credit_Score",
            y="Monthly_Inhand_Salary",
           color="Credit_Score",
           title="Credit Scores Based on Monthly Income",
           color_discrete_map={"Poor":"red",
                              "Standard":"Yellow",
                              "Good":"green"})


# In[20]:


fig3.show()


# In[21]:


#Number of Bank Accounts Impact 


# In[24]:


fig4=px.box(data,
           x="Credit_Score",
           y="Num_Bank_Accounts",
           color="Credit_Score",
           title="Credit Score based on bank accounts",
           color_discrete_map={'Poor':'red',
                              'Standard':'yellow',
                              'Good':'green'})


# In[25]:


fig4.show()


# In[26]:


fig = px.box(data, 
             x="Credit_Score", 
             y="Num_Credit_Card", 
             color="Credit_Score",
             title="Credit Scores Based on Number of Credit cards", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()


# In[27]:


fig = px.box(data, 
             x="Credit_Score", 
             y="Interest_Rate", 
             color="Credit_Score",
             title="Credit Scores Based on the Average Interest rates", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()


# In[ ]:




