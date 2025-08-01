# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 22:38:33 2025

@author: RuKumar
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from nltk.chat.util import Chat, reflections
# Pairn is a list of patterns and response 
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is thecleverprogrammer, but you can just call me robot and I'm a chatbot .",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
       
    ],
    [
        r"(.*)created(.*)",
        ["prakash created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['hyderabad, India',]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["Virat Kohli"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['our customer service will reach you']
    ],
 ]
print("hi,i am thecleaverprogrammer and i like  to chat \nn please types lower case english language ")

chat=Chat(pairs,reflections)
          
chat.converse()
