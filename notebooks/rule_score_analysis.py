import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from rules.rule_engine import rule_score

df = pd.read_csv('data/raw/spam_dataset.csv')

score = []
for text in df['message_content']:
    s , _ = rule_score(text) 
    score.append(s)

df['rule_score'] = score

spam_scores = df[df['is_spam'] == 1]['rule_score']
ham_scores = df[df['is_spam'] == 0]['rule_score']

print("Spam Messages Rule Score Statistics:")
print(spam_scores.describe())

print("\nHam Messages Rule Score Statistics:")
print(ham_scores.describe())

print("\nSpam score counts")
print(spam_scores.value_counts().sort_index())

print("\nHam score counts")
print(ham_scores.value_counts().sort_index())


threshold = 1
preds = df['rule_score'] >= threshold
preds = preds.astype(int)

tp = ((preds == 1) & (df['is_spam'] == 1)).sum()
fp = ((preds == 1) & (df['is_spam'] == 0)).sum()
fn = ((preds == 0) & (df['is_spam'] == 1)).sum()

precision = tp / (tp + fp) 
recall = tp / (tp + fn) 

print("Threshold:", threshold)
print("TP:", tp)
print("FP:", fp)
print("FN:", fn)
print("Precision:", precision)
print("Recall:", recall)