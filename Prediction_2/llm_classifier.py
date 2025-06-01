import ollama

def LLMClassifier2(input):

    prompt = f"""
    You are a query classifier.

    Your job is to classify whether a user message is a:

    - 'real' — a **real-time query** that depends on current, live, or dynamic information (e.g., weather now, live scores, current events).
    - 'normal' — a **general query** that does not rely on real-time data (e.g., definitions, historical facts, how-to questions).

    Only reply with one word: 'real' or 'normal'.

    Message: "{input}"
    """



    classifier = ollama.chat(
        model="gemma3:4b",
        messages= [
            {"role": "user", "content": prompt}
        ]
    )

    classifier_response = classifier['message']['content'].strip().lower()

    return classifier_response

    