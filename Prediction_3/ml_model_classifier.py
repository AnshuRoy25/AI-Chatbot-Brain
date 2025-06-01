import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

df = pd.read_csv("system_hardware_instruction.csv")

df['text'] = df['text'].str.replace('’', "'", regex=False)


vectorizer = TfidfVectorizer()

x = vectorizer.fit_transform(df['text'])
y = df['label']

model = LogisticRegression()

model.fit(x, y)
joblib.dump(vectorizer, 'vectorizer_3.pkl')
joblib.dump(model, 'model_3.pkl')


