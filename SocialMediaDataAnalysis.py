#!/usr/bin/env python
# coding: utf-8

# # Clean & Analyze Social Media

# ## Introduction
# 
# Social media has become a ubiquitous part of modern life, with platforms such as Instagram, Twitter, and Facebook serving as essential communication channels. Social media data sets are vast and complex, making analysis a challenging task for businesses and researchers alike. In this project, we explore a simulated social media, for example Tweets, data set to understand trends in likes across different categories.
# 
# ## Prerequisites
# 
# To follow along with this project, you should have a basic understanding of Python programming and data analysis concepts. In addition, you may want to use the following packages in your Python environment:
# 
# - pandas
# - Matplotlib
# - ...
# 
# These packages should already be installed in Coursera's Jupyter Notebook environment, however if you'd like to install additional packages that are not included in this environment or are working off platform you can install additional packages using `!pip install packagename` within a notebook cell such as:
# 
# - `!pip install pandas`
# - `!pip install matplotlib`
# 
# ## Project Scope
# 
# The objective of this project is to analyze tweets (or other social media data) and gain insights into user engagement. We will explore the data set using visualization techniques to understand the distribution of likes across different categories. Finally, we will analyze the data to draw conclusions about the most popular categories and the overall engagement on the platform.
# 
# ## Step 1: Importing Required Libraries
# 
# As the name suggests, the first step is to import all the necessary libraries that will be used in the project. In this case, we need pandas, numpy, matplotlib, seaborn, and random libraries.
# 
# Pandas is a library used for data manipulation and analysis. Numpy is a library used for numerical computations. Matplotlib is a library used for data visualization. Seaborn is a library used for statistical data visualization. Random is a library used to generate random numbers.

# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

# Membuat list kategori postingan
categories = ['Food', 'Travel', 'Fashion', 'Sports', 'Tech']

# Jumlah postingan yang ingin dibuat
num_posts = 100

# Membuat data dummy
data = {
    'Post_ID': range(1, num_posts + 1),
    'Category': [random.choice(categories) for _ in range(num_posts)],
    'Likes': [random.randint(20, 500) for _ in range(num_posts)]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menampilkan 5 baris pertama
df.head()

# Statistik deskriptif
df.describe()

# Visualisasi rata-rata likes
plt.figure(figsize=(8,5))
sns.barplot(x=avg_likes.index, y=avg_likes.values, palette='muted')
plt.title('Rata-Rata Likes per Kategori')
plt.xlabel('Kategori')
plt.ylabel('Rata-Rata Likes')
plt.show()


# In[ ]:




