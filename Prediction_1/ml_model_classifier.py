import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

df = pd.read_csv("training_data.csv")

vectorizer = TfidfVectorizer()

x = vectorizer.fit_transform(df['text'])
y = df['label']

model = LogisticRegression()

model.fit(x, y)

joblib.dump(vectorizer, 'vectorizer.pkl')
joblib.dump(model, 'model.pkl')


