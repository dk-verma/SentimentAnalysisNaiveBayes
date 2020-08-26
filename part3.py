#wordbag ( word -> frequency of this word in all 4 table's tweet data )
import pandas as pd

#import my csv files
happy = pd.read_csv('happy_words.csv')
sad = pd.read_csv('sad_words.csv')
unsmile = pd.read_csv('unsmile_words.csv')
fun = pd.read_csv('fun_words.csv')

wordbag = pd.concat([happy,sad,unsmile,fun]).drop_duplicates(subset = 'word').reset_index(drop=True)
wordbag=wordbag[['word','frequency']]
wordbag=wordbag.dropna(axis=0)

print(wordbag)

wordbag.to_csv('wordbag.csv')
