import pandas as pd
import numpy as np
import sklearn
from sklearn.metrics import confusion_matrix

ftable = pd.read_csv('ftable.csv')
#ftable = ftable[ftable['word'] != 'sad']
#ftable = ftable[ftable['word'] != 'sad,']
#ftable = ftable[ftable['word'] != ':(']
#ftable = ftable[ftable['word'] != 'fun']
#ftable = ftable[ftable['word'] != 'happy,']
#ftable = ftable[ftable['word'] != 'happy']
#ftable = ftable.drop_duplicates(subset = 'word')
#ftable.to_csv('ftable.csv', header=True, index=False, encoding='utf-8')
df=pd.read_csv('test.csv')
#df['pred']=0

for j in range(len(df)):
 #   test = 'i dont know what to do anymore'
    positive_instance = 2403.0
    negative_instance = 2397.0
    
    test_words = df.text.iloc[j]
#split all the words in my text
    test_words=test_words.split()
    
    prob_positive = float(positive_instance/(positive_instance+negative_instance))
    prob_negative = 1 - prob_positive

    pos_word = 1.0*prob_positive
    neg_word = 1.0*prob_negative
    
    for i in range(len(test_words)):
        word = test_words[i]
        print(word)
        index_val = ftable.index[ftable['word'] == word]
        if (len(index_val) > 0):
            print(index_val[0])
            pos_val = ftable['positive'].iloc[index_val[0]]
            neg_val = ftable['negative'].iloc[index_val[0]]
            pos_word = pos_word * pos_val/positive_instance #(pos_val+neg_val)
            neg_word = neg_word * neg_val/negative_instance #(pos_val+neg_val)
    if pos_word > neg_word:
        df.pred.iloc[j]=1  
        
y_true = df.type
y_pred = df.pred
confusion_matrix(y_true, y_pred)#, labels=["positive", "negative"]) 
tp, fp, fn, tn = confusion_matrix(y_true, y_pred).ravel() 

sklearn.metrics.accuracy_score(y_true, y_pred)
sklearn.metrics.precision_score(y_true, y_pred)    
        
df.to_csv('test.csv', header=True, index=False, encoding='utf-8')        

'''def removetext(text):
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
df['text'] = df['text'].apply(lambda x: x.replace('&amp',' '))
df['text'] = df['text'].apply(lambda x: x.replace(',',' '))
df['text'] = df['text'].apply(lambda x: x.replace("i'm","im"))
df['text'] = df['text'].apply(lambda x: x.replace("it's","its"))
'''