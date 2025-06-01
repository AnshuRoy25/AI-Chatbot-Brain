import ollama

def LLMClassifier1(input):

    prompt = f"""
    You are an intent classifier. Your job is to classify whether a user message is a:

    - 'instruction' — asking the assistant to **do** something on the system (like open an app).
    - 'query' — asking a **question** or for **information**.

    Only reply with one word: 'instruction' or 'query'.

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

    