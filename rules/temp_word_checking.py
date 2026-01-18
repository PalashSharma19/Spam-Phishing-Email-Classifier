import pandas as pd

df = pd.read_csv('data/raw/spam_dataset.csv')
spam_df = df[df["is_spam"] == 1]

all_spam_text = " ".join(spam_df["message_content"])

all_spam_text = all_spam_text.lower()

words = all_spam_text.split()

stopwords = ["the", "is", "and", "to", "of", "a", "in", "for", "on", "at" , "our" , "you" , "your" , "we" , "be" , "this" , "that" , "it" , "as" , "are" , "with" , "by" , "an" , "from" , "or" , "have" , "not" , "all" , "if" , "but" , "they" , "my" , "so" , "me" , "no" , "do" , "just" , "like" , "about" , "what" , "there" , "when" , "get" , "can" , "will" , "would" , "us" , "more" , "your" , "now" , "one" , "out" , "how" , "up" , "time" , "new"]

filtered_words = []
for word in words:
    if word.isalpha() and word not in stopwords:
        filtered_words.append(word)

from collections import Counter

word_counts = Counter(filtered_words)

common_words = word_counts.most_common(20)

print("Most common words in spam messages:")
for word, count in common_words:
    print(f"{word}: {count}")