
from Prediction_2.llm_classifier import LLMClassifier2
import joblib

def MLClassifier2(input):
     model_2 = joblib.load('model_2.pkl')
     vectorizer_2 = joblib.load('vectorizer_2.pkl')

     vectorized_user_input = vectorizer_2.transform([input])

     predict_2 = model_2.predict(vectorized_user_input)

     probability = model_2.predict_proba(vectorized_user_input)[0]

     a = probability[0]
     b = probability[1]

     if a > 0.8 or b > 0.8:
          print("Prediction: ", predict_2[0], "Probability: ", probability, "ML")
          return predict_2[0]     
     
     else:
          print("Prediction: ", predict_2[0], "Probability: ", probability, "LLM")
          classifier_response = LLMClassifier2(input)

          return classifier_response


