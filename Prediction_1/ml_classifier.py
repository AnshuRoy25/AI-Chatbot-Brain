
from Prediction_1.llm_classifier import LLMClassifier1
import joblib
import os

current_dir = os.path.dirname(__file__)
model_path = os.path.abspath(os.path.join(current_dir, "..", "Models", "model.pkl"))
vectorizer_path = os.path.abspath(os.path.join(current_dir, "..", "Models", "vectorizer.pkl"))

def MLClassifier1(input):
     model_1 = joblib.load(model_path)
     vectorizer_1 = joblib.load(vectorizer_path)

     vectorized_user_input = vectorizer_1.transform([input])

     predict_1 = model_1.predict(vectorized_user_input)

     probability = model_1.predict_proba(vectorized_user_input)[0]

     a = probability[0]
     b = probability[1]

     if a > 0.75 or b > 0.75:
          print("Prediction: ", predict_1[0], "Probability: ", probability, "ML")
          return predict_1[0]     
     
     else:
          print("Prediction: ", predict_1[0], "Probability: ", probability, "LLM")
          classifier_response = LLMClassifier1(input)

          return classifier_response


