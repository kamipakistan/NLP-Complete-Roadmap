#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 10:06:32 2022

@author: kamipakistan
"""


"""
# ===============  Data Visualization for Text Data ============= #
To visualize text data, generally, we use the word cloud but there are some
 other techniques also, which we can try to visualize the data such as,
 
 1. frequency distribution
 2. frequency graph

Let’s discuss the word cloud in a more detailed manner:
    
# ==== Word Cloud 
Word Cloud is a data visualization technique in which words from a given text
 display on the main chart. Some properties associated with this chart are as
 follows:
     
     *In this technique, more frequent or essential words display in a 
     larger and bolder font,
     
     *While less frequent or essential words display in smaller or thinner
     fonts.
     
This data visualization technique gives us a glance at what text should 
be analyzed, so it is a very beneficial technique in NLP tasks."""

# Here, to draw the word cloud, we use the following text:

paragraph = """Mr. President (Quaid-e-Azam Mohammad Ali Jinnah): Ladies and 
Gentlemen, I cordially thank you, with the utmost sincerity, for the honour 
you have conferred upon me — the greatest honour that it is possible for this 
Sovereign Assembly to confer — by electing me as your first President. I also 
thank those leaders who have spoken in appreciation of my services and their 
personal references to me."""

# Importing libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS

# Creating Wordcloud object
word_cloud = WordCloud(stopwords=STOPWORDS)

# Generating the worldcloud
textVisulalize = word_cloud.generate(paragraph)

plt.figure(figsize=(12, 12))
plt.imshow(textVisulalize)

# To remove the axis value
plt.axis('off')
plt.show()

