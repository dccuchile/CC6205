#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 15:14:55 2023

@author: fbravo
"""
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer('spanish')


texto = 'Me gustan los lenguajes humanos y los lenguajes de programación'
def stem_sentence(text):
    return ' '.join([stemmer.stem(i) for i in word_tokenize(text)])    
print(stem_sentence(texto))


# python -m spacy download es_core_news_sm
import spacy
nlp = spacy.load('es_core_news_sm')

def lemmatizer(text):  
  doc = nlp(text)
  return ' '.join([word.lemma_ for word in doc])

print(lemmatizer(texto))