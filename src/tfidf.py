import math

def build_tfidf(messages):
    tokenized = [msg.lower().split() for msg in messages]

    vocabulary = []
    for msg in tokenized:
        for word in msg:
            if word not in vocabulary:
                vocabulary.append(word)

    tf = []
    for msg in tokenized:
        tf_msg = {}
        for word in vocabulary:
            tf_msg[word] = msg.count(word)
        tf.append(tf_msg)

    df = {}
    for word in vocabulary:
        count = 0
        for msg in tokenized:
            if word in msg:
                count += 1
        df[word] = count

    idf = {}
    N = len(tokenized)
    for word, freq in df.items():
        idf[word] = math.log((N + 1) / (freq + 1)) + 1

    tfidf = []
    for msg in tf:
        vec = []
        for word in vocabulary:
            vec.append(msg[word] * idf[word])
        tfidf.append(vec)

    return tfidf, vocabulary, idf


def transform_tfidf(messages, vocabulary, idf):
    tokenized = [msg.lower().split() for msg in messages]

    tfidf = []
    for msg in tokenized:
        vec = []
        for word in vocabulary:
            vec.append(msg.count(word) * idf[word])
        tfidf.append(vec)

    return tfidf
