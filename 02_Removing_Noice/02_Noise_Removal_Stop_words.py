#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 09:45:23 2022

@author: kamipakistan
"""
import nltk
from nltk.corpus import stopwords

# list of stop words
stWords = stopwords.words('english')

paragraph = """Mr. President (Quaid-e-Azam Mohammad Ali Jinnah): Ladies and 
Gentlemen, I cordially thank you, with the utmost sincerity, for the honour 
you have conferred upon me — the greatest honour that it is possible for this 
Sovereign Assembly to confer — by electing me as your first President. I also 
thank those leaders who have spoken in appreciation of my services and their 
personal references to me."""


# word tokenization 
word_tokens = nltk.word_tokenize(paragraph)


para_without_sw = [word for word in word_tokens if not word in stWords]
print(para_without_sw)

cleaned_paraghraph = " ".join(para_without_sw)
