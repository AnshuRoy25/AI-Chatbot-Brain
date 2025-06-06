
from Prediction_3.llm_classifier import LLMClassifier3
import joblib
import os

current_dir = os.path.dirname(__file__)
model_path = os.path.abspath(os.path.join(current_dir, "..", "Models", "model_3.pkl"))
vectorizer_3_path = os.path.abspath(os.path.join(current_dir, "..", "Models", "vectorizer_3.pkl"))

def MLClassifier3(input):
     model_3 = joblib.load(model_path)
     vectorizer_3 = joblib.load(vectorizer_3_path)

     vectorized_user_input = vectorizer_3.transform([input])

     predict_3 = model_3.predict(vectorized_user_input)

     probability = model_3.predict_proba(vectorized_user_input)[0]

     a = probability[0]
     b = probability[1]

     if a > 0.75 or b > 0.75:
          print("Prediction: ", predict_3[0], "Probability: ", probability, "ML")
          return predict_3[0]     
     
     else:
          print("Prediction: ", predict_3[0], "Probability: ", probability, "LLM")
          classifier_response = LLMClassifier3(input)
          return classifier_response


