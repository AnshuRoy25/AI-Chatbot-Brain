from serpapi import GoogleSearch
import ollama
import pyttsx3

def google_search(text):

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)

    print("Jarvis: ", end='', flush=True)

    params = {
        "engine": "google",
        "q": text,
        "api_key" : "761bb92ff490aee44ed378416606065cae02e680f9870aba5fb032c5c5bc78ec" 
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    data = ""
    i=1

    for result in results.get("organic_results", [])[:10]:
        title = result.get("title")
        snippet = result.get("snippet")
        data += f"{i}.{title}\n{snippet}\n\n"
        i += 1

    prompt = f"""
    You are an expert news summarizer.

    The user searched for: "{text}"

    Please write a paragraph summarizing the top headlines and snippets below, in a way that answers the user's interest. Summarize as if you are speaking to the user.

    {data}
    """

    response = ollama.chat(
        model =  "mistral:7b",
        messages = [
            {"role": "user", "content": prompt}
        ],
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


