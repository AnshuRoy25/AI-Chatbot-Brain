import ollama

def LLMClassifier3(input):

    prompt = f"""
    You are an intent classifier. Your job is to classify whether a user message is a:

    - 'system' — asking the assistant to perform an action on the computer system (like opening an app, changing a file, or adjusting settings).
    - 'hardware' — asking the assistant to control or interact with physical hardware (like motors, sensors, or external devices).

    Only reply with one word: 'system' or 'hardware'.

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

    