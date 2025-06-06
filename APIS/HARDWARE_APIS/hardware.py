import ollama


def hardware_instruction(user_text):

    prompt = f"""
    You're Jarvis, a sarcastic AI. The user said: "{user_text}"

    Refuse to do it in the funniest, wittiest way possible. No help — just humor.
    """

    response = ollama.chat(
        model = "mistral:7b",
        messages= [
            {"role": "user", "content": user_text}
            ]
    )

    reply = response["message"]["content"]

    return reply
