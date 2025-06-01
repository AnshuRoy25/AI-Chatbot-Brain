from Prediction_1.ml_classifier import MLClassifier1
from Prediction_2.ml_classifier import MLClassifier2
from Prediction_3.ml_classifier import MLClassifier3

user_input = input("You: ")

prediction1 = MLClassifier1(user_input) #query / instruction

print(prediction1)

if prediction1 == "query":
    prediction2 = MLClassifier2(user_input) # real / normal
    print(prediction2)
    
elif prediction1 == "instruction":
    prediction3 = MLClassifier3(user_input)  # system / hardware
    print(prediction3)





