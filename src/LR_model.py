import numpy as np
import pandas as pd
import math
import os

from tfidf import build_tfidf, transform_tfidf

df = pd.read_csv(os.path.join(os.path.dirname(__file__), "../data/raw/spam_dataset.csv"))

messages = df["message_content"].tolist()
labels = df["is_spam"].tolist()

data = list(zip(messages, labels))
np.random.shuffle(data)

split_idx = int(0.7 * len(data))

train_data = data[:split_idx]
test_data  = data[split_idx:]

X_train_text, y_train = zip(*train_data)
X_test_text,  y_test  = zip(*test_data)

X_train_tfidf, vocabulary, idf = build_tfidf(X_train_text)

X_test_tfidf = transform_tfidf(X_test_text, vocabulary, idf)

X_train = np.array(X_train_tfidf)
X_test  = np.array(X_test_tfidf)

y_train = np.array(y_train)
y_test  = np.array(y_test)

w = np.zeros(len(vocabulary))
b = 0.0

lr = 0.0001
eps = 1e-5
max_epochs = 2000
lambda_reg = 0.01

previous_loss = float("inf")

for epoch in range(max_epochs):
    total_loss = 0.0

    for i in range(len(X_train)):
        x = X_train[i]
        y = y_train[i]

        z = np.dot(w, x) + b
        p = 1 / (1 + np.exp(-z))
        p = np.clip(p, 1e-15, 1 - 1e-15)

        loss = - (y * math.log(p) + (1 - y) * math.log(1 - p))
        total_loss += loss

        w = w - lr * ((p - y) * x + lambda_reg * w)
        b = b - lr * (p - y)

    avg_loss = total_loss / len(X_train)

    if abs(previous_loss - avg_loss) < eps:
        print(f"Converged at epoch {epoch}")
        break

    previous_loss = avg_loss

    if epoch % 50 == 0:
        print(f"Epoch {epoch}, Loss: {avg_loss}")

correct = 0

for i in range(len(X_test)):
    z = np.dot(w, X_test[i]) + b
    p = 1 / (1 + np.exp(-z))
    pred = 1 if p >= 0.5 else 0

    if pred == y_test[i]:
        correct += 1

accuracy = correct / len(y_test)

print("\nTest Accuracy:", accuracy)
