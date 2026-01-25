import pandas as pd
import math
import os

df = pd.read_csv(os.path.join(os.path.dirname(__file__), "../data/raw/spam_dataset.csv"))

messages = df['message_content']
labels = df['is_spam']

messages = messages.tolist()
labels = labels.tolist()

tokenized_messages = []

for message in messages:
    word = message.lower().split()
    tokenized_messages.append(word)

vocabulary = []

for message in tokenized_messages:
    for word in message:
        if word not in vocabulary:
            vocabulary.append(word)

tf = []

for message in tokenized_messages:
    tf_message = {}
    for word in vocabulary:
        tf_message[word] = message.count(word)
    tf.append(tf_message)


df = {}

for word in vocabulary:
    freq = 0
    for message in tokenized_messages:
        if word in message:
            freq += 1
    df[word] = freq


idf = {}

for word, freq in df.items():
    idf[word] = math.log((len(tokenized_messages) + 1) / freq + 1) + 1


tfidf = []

for message in tf:
    tfidf_message = []
    for word in vocabulary:
        tfidf_message.append(message[word] * idf[word])
    tfidf.append(tfidf_message)

if __name__ == "__main__":
    print(tfidf)