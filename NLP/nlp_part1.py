# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 22:49:02 2025

@author: RuKumar
"""

from sklearn.feature_extraction.text import CountVectorizer

sentence="data science and ai has great carrier ahead"

vectorizer=CountVectorizer()
vector=vectorizer.fit_transform([sentence])
vector.toarray()    

from sklearn.feature_extraction.text import TfidfVectorizer
sentence="data science and ai has great carrier ahead"

vectorizer=TfidfVectorizer()
vector=vectorizer.fit_transform([sentence])
vector.toarray()   
