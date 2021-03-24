# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:16:47 2021

@author: Hadar
"""
def revword(word:str) -> str:
    new=""
    for letter in word:
        nl=letter.lower()
        new=nl+new
    return new

def countword() -> int:
    text= open('C:/Users/Hadar/pythonCodes/matala2/text.txt')
    word=""
    for line in text:
        word=line.split()[0]
        break
    count=0
    for line in text:
        numWords=len(line.split())
        i=0
        while i<numWords:
            wrd=revword(line.split()[i]) 
            if wrd==word:
                count+=1
            i+=1
    return(count+1)
