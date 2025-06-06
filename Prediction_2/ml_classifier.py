
from Prediction_2.llm_classifier import LLMClassifier2
import joblib
import os

current_dir = os.path.dirname(__file__)
model_path = os.path.abspath(os.path.join(current_dir, "..", "Models", "model_2.pkl"))
vectorizer_2_path = os.path.abspath(os.path.join(current_dir, "..", "Models", "vectorizer_2.pkl"))

def MLClassifier2(input):
     model_2 = joblib.load(model_path)
     vectorizer_2 = joblib.load(vectorizer_2_path)

     vectorized_user_input = vectorizer_2.transform([input])

     predict_2 = model_2.predict(vectorized_user_input)

     probability = model_2.predict_proba(vectorized_user_input)[0]

     a = probability[0]
     b = probability[1]

     if a > 0.75 or b > 0.75:
          print("Prediction: ", predict_2[0], "Probability: ", probability, "ML")
          return predict_2[0]     
     
     else:
          print("Prediction: ", predict_2[0], "Probability: ", probability, "LLM")
          classifier_response = LLMClassifier2(input)

          return classifier_response


