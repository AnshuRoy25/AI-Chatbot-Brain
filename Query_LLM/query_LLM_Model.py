import ollama
import pyttsx3

def QueryLLM(input):

    # Initialize TTS engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)

    print("Jarvis: ", end='', flush=True)

    # Stream from Ollama
    response = ollama.chat(
        model='dolphin-mistral',
        messages=[{'role': 'user', 'content': input}],
        stream=True
    )

    # Sentence-aware speaking
    buffer = ""
    sentence = ""
    end_punctuations = [".", "!", "?"]

    for chunk in response:
        text = chunk['message']['content']
        print(text, end='', flush=True)
        buffer += text

        # Process buffer into sentences
        while any(p in buffer for p in end_punctuations):
            # Find earliest sentence-ending punctuation
            min_index = min((buffer.find(p) for p in end_punctuations if p in buffer))
            sentence = buffer[:min_index + 1]
            buffer = buffer[min_index + 1:].lstrip()  # Keep rest, strip leading spaces

            # Speak the full sentence
            engine.say(sentence)
            engine.runAndWait()

    # Speak any final leftover sentence (if any)
    if buffer.strip():
        engine.say(buffer.strip())
        engine.runAndWait()
