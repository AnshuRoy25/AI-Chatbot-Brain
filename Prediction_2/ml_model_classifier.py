import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

df = pd.read_csv("real_normal_query.csv")

#df['text'] = df['text'].str.replace('’', "'", regex=False)
df = df.sample(frac=1, random_state=42).reset_index(drop=True)


vectorizer = TfidfVectorizer()

x = vectorizer.fit_transform(df['text'])
y = df['label']

model = LogisticRegression()

model.fit(x, y)

joblib.dump(vectorizer, 'vectorizer_2.pkl')
joblib.dump(model, 'model_2.pkl')


