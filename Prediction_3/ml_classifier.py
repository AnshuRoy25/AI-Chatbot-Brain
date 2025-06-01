
from Prediction_3.llm_classifier import LLMClassifier3
import joblib

def MLClassifier3(input):
     model_3 = joblib.load('model_3.pkl')
     vectorizer_3 = joblib.load('vectorizer_3.pkl')

     vectorized_user_input = vectorizer_3.transform([input])

     predict_3 = model_3.predict(vectorized_user_input)

     probability = model_3.predict_proba(vectorized_user_input)[0]

     a = probability[0]
     b = probability[1]

     if a > 0.8 or b > 0.8:
          print("Prediction: ", predict_3[0], "Probability: ", probability, "ML")
          return predict_3[0]     
     
     else:
          print("Prediction: ", predict_3[0], "Probability: ", probability, "LLM")
          classifier_response = LLMClassifier3(input)
          return classifier_response


