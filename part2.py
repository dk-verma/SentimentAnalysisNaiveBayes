'''
cleaning all tables
'''
import pandas as pd
import re

df = pd.read_csv('happy.csv')
#{sad,unsmile,happy,fun}
#Remove any rows with a "nan" in them
df = df.dropna(axis=0, how = 'any')

#Make it so that any non readable text gets converted into nothing
def removetext(text):
    return ''.join([i if ord(i) < 128 else '' for i in text])

#Here I am doing the actual removing
df['text'] = df['text'].apply(removetext)

#Make all my texts lower case
df['text'] = df['text'].apply(lambda x: x.lower())

#Get rid of all weird punctuation and extra lines
df['text'] = df['text'].apply(lambda x: x.replace('.',' '))
df['text'] = df['text'].apply(lambda x: x.replace('\n',' '))
df['text'] = df['text'].apply(lambda x: x.replace('?',' '))
df['text'] = df['text'].apply(lambda x: x.replace('!',' '))
df['text'] = df['text'].apply(lambda x: x.replace('"',' '))
df['text'] = df['text'].apply(lambda x: x.replace(';',' '))
df['text'] = df['text'].apply(lambda x: x.replace('#',' '))
df['text'] = df['text'].apply(lambda x: x.replace(',',' '))
df['text'] = df['text'].apply(lambda x: x.replace('&amp',' '))
df['text'] = df['text'].apply(lambda x: x.replace("i'm","im"))
df['text'] = df['text'].apply(lambda x: x.replace("it's","its"))

df.to_csv('fun.csv', header=True, index=False, encoding='utf-8')
#{sad,unsmile,happy,fun}