import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

df = pd.read_csv("query_instruction.csv")

df = df.sample(frac=1, random_state=42).reset_index(drop=True)

vectorizer = TfidfVectorizer()

x = vectorizer.fit_transform(df['text'])
y = df['label']

model = LogisticRegression()

model.fit(x, y)

joblib.dump(vectorizer, 'vectorizer.pkl')
joblib.dump(model, 'model.pkl')


