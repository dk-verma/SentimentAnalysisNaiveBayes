#Create your frequency table
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
#Read the files with the tweets
fun = pd.read_csv('fun.csv')
happy = pd.read_csv('happy.csv')
unsmile = pd.read_csv('unsmile.csv')
sad = pd.read_csv('sad.csv')
#Get the wordbag
wordbag = pd.read_csv('wordbag.csv')
wordbag = wordbag.drop_duplicates()
#Classify tweets that had the word fun or happy in them as 1 (positive)
#and the others as 0 (negative)
fun['type'] = 1
happy['type'] = 1
unsmile['type'] = 0
sad['type'] = 0   
#Join all of the dataframes into one big one for easier manipulation of a test/train split
df = pd.concat([happy,sad,unsmile,fun]).reset_index(drop=True)
#Create a test and train set by using the sklearn function train_test_split
train, test = train_test_split(df, test_size=0.2)
test.to_csv('test.csv', header=True, index=False, encoding='utf-8')

train_positive = train[train['type'] ==1]
train_negative = train[train['type'] ==0]

train_positive.to_csv('train_positive.csv', header=True, index=False, encoding='utf-8')
train_negative.to_csv('train_negative.csv', header=True, index=False, encoding='utf-8')

#Create your frequency table
word_bank = [0]*len(wordbag)
positive = [0]*len(wordbag)
negative = [0]*len(wordbag)
#train_positive['text']=train_positive['text'].str.split()
#train_negative['text']=train_negative['text'].str.split()
#Go over all the words in the frequency table
for i in range(len(wordbag)):    
    #Get the word in the frequency table at a given row
    word = wordbag['word'].iloc[i]
    word_bank[i] = word
    count = 0  #Count the number of instances that have the word at least once    
    #this iterates through each of the tweets in the positive train set
    for j in range(len(train_positive)):
        #This checks to see the number of time the said word appears in a given tweet
        appears = train_positive['text'].iloc[j].count(word)#check)
        if appears > 0:
            count = count + 1            
    positive[i] = count            
    #Does the same thing but for negative numbers
    count = 0  
    for j in range(len(train_negative)):
        appears = train_negative['text'].iloc[j].count(word)
        if appears > 0:
            count = count + 1 
    negative[i] = count        

d = {'word': word_bank, 'positive': positive, 'negative': negative}
ftable = pd.DataFrame(data = d)
ftable.to_csv('ftable.csv', header=True, index=False, encoding='utf-8')
print(positive_instance)
print(negative_instance)
