#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[8]:


df = pd.read_csv(r"C:\Users\risha\Downloads\final_dataset - final_dataset.csv")
df.head()


# # Stripping the tweets

# **To Strip the Links**

# In[9]:


import re,string

def strip_links(text):
    link_regex    = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    links         = re.findall(link_regex, text)
    for link in links:
        text = text.replace(link[0], ', ')    
    return text


# **To strip the Mentions and Hashtags**

# In[10]:


def strip_mentions_and_hashtags(text):
    entity_prefixes = ['@','#']
    for separator in  string.punctuation:
        if separator not in entity_prefixes :
            text = text.replace(separator,' ')
    words = []
    for word in text.split():
        word = word.strip()
        if word:
            if word[0] not in entity_prefixes:
                words.append(word)
    return ' '.join(words)


# **To Strip the Unnecessary Symbols and Numbers**

# In[18]:


def strip_symbols(text):
    listt=['\n','\r','\t',',','.','@',':']
    for i in listt:
        text = text.replace(i," ")

    text = " ".join(text.split())
    return text

def strip_numbers(text):
    resulted_text = ''.join(i for i in text if not i.isdigit())
    return resulted_text


# **Main Function**

# In[19]:


def strip_tweets(text):
    text = strip_links(text)
    text = strip_mentions_and_hashtags(text)
    text = strip_symbols(text)
    text = strip_numbers(text)
    
    return text


# In[20]:


stripped_text = []
for i in df['Text']:
    stripped_text.append(strip_tweets(i))


# In[22]:


print(stripped_text[3])
print(len(stripped_text))


# In[25]:


new_df = pd.DataFrame()

new_df['Text'] = stripped_text
new_df['Labels'] = [i for i in df['Label']]


# In[26]:


new_df.head()


# In[27]:


new_df.to_csv(r"C:\Users\risha\Downloads\final_dataset.csv",header=False,index=False,encoding = 'utf-16')


# In[ ]:




