#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 11:18:53 2022
@author: kamipakistan
"""

"""
## Tokenization:
    is a process of splitting a text object into smaller units which are also 
    called tokens. Examples of tokens include words, numbers, engrams, or 
    even symbols.
    Tokenization can be performed at the sentence level or at the word level 
    or even at the character level. Based on it we discuss the following two 
    types of Tokenization:
        1. Sentence Tokenization
        2. Word Tokenization
"""

# importing Natural language tool kit
import nltk
from nltk.tokenize import sent_tokenize

paraghraph = """Mr. President (Quaid-e-Azam Muhammad Ali Jinnah): Ladies and 
Gentlemen, I cordially thank you, with the utmost sincerity, for the honour 
you have conferred upon me — the greatest honour that it is possible for this 
Sovereign Assembly to confer — by electing me as your first President. I also 
thank those leaders who have spoken in appreciation of my services and their 
personal references to me. I sincerely hope that with your support and your 
co-operation we shall make this Constituent Assembly an example to the world.
The Constituent Assembly has got two main functions to perform. 
The first is the very onerous and responsible task of
framing our future constitution of Pakistan and the second of 
functioning as a full and complete Sovereign body as the Federal Legislature
of Pakistan. We have to do the best we can in adopting a provisional 
constitution for the Federal Legislature of Pakistan. You know really 
that not only we ourselves are wondering but, I think, the whole world is 
wondering at this unprecedented cyclonic revolution which has brought about 
the plan of creating and establishing two independent Sovereign Dominions in 
this sub-continent. As it is, it has been unprecedented; there is no parallel 
in the history of the world. This mighty sub-continent with all kinds of 
inhabitants has been brought under a plan which is titanic, unknown, 
unparalleled. And what is very important with regards to it is that we have 
achieved it peacefully and by means of a revolution of the greatest 
possible character."""
 

# 1. Sentence Tokenization
"""Sentence tokenization, also known as Sentence Segmentation is the technique
 of dividing a string of written language into its component sentences. """
 
sentence = nltk.sent_tokenize(paraghraph)
 
# 2. Word Tokenization
"""Word tokenization, also known as Word Segmentation is the problem of 
dividing a string of written language into its component words."""

words = nltk.word_tokenize(paraghraph)
