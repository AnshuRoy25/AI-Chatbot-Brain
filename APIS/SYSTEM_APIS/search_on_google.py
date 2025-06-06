import pywhatkit

def google_search(ggl_prompt):

    ggl_prompt = ggl_prompt.lower()
    ggl_prompt_list = ggl_prompt.split()

    while (ggl_prompt_list[0] != "search"):
        ggl_prompt_list.pop(0)

    ggl_prompt_list.pop(0)

    google_prompt = " ".join(ggl_prompt_list)

    pywhatkit.search(google_prompt)

    reply = f"Searching for {google_prompt}" 

    return reply