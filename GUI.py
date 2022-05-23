from __future__ import unicode_literals
import imp
from tkinter import *
from tashaphyne.stemming import ArabicLightStemmer
import nltk
import tkinter.messagebox
import pandas as pd

df = pd.read_excel('F:\ANLP\ANLP.xlsx','Sports',header=None,)

def lightstemmer(txt):
    tokenized = nltk.word_tokenize(txt)
    lightstem = ArabicLightStemmer()
    lightstemmed = [lightstem.light_stem(w) for w in tokenized]
    filtered = removeArabicStopWords(lightstemmed)
    return filtered

def rootstemmer(txt):
    tokenized = nltk.word_tokenize(txt)
    rootstemm = nltk.ISRIStemmer()
    stemmed = [rootstemm.stem(w) for w in tokenized]
    filtered = removeArabicStopWords(stemmed)
    return filtered


def removeArabicStopWords(txt):
    stopwords = []
    for line in open(r"stopwords.txt",'r',encoding='utf-8'):
        stopwords.append(line[:-1])
    for word in txt:
        if word in stopwords:
            txt.remove(word)
    return txt


def sel():
    out =[]
    selection =var.get()

    if(selection == 1):

        for line in open(r"Khaleej-2004\Economy\arc_Articlesww1a2c.txt",'r',encoding='utf-8'):
          out.append(line)
        tkinter.messagebox.showinfo('output',lightstemmer(str(out)))

    if(selection == 2):
        for line in open(r"Khaleej-2004\Local News\arc_Articlesww0abb.txt",'r',encoding='utf-8'):
          out.append(line) 
        tkinter.messagebox.showinfo('output',rootstemmer(str(out)))

    if(selection == 3):
        for line in open(r"Sports\arc_Articlesww0ace.txt",'r',encoding='utf-8'):
          out.append(line) 
        tkinter.messagebox.showinfo('output',lightstemmer(str(df)))



root = Tk()
root.geometry("300x300")
root.title("task window")


var = IntVar()
R1 = Radiobutton(root, text="Economy", variable=var, value='1',command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Local news", variable=var, value=2,command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Sports", variable=var, value=3,command=sel)
R3.pack( anchor = W)


root.mainloop()