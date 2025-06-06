import pywhatkit


def play_on_yt(yt_prompt):

    yt_prompt = yt_prompt.lower()
    yt_prompt_list = yt_prompt.split()

    while (yt_prompt_list[0] != "play"):
        yt_prompt_list.pop(0)

    yt_prompt_list.pop(0)
        
    youtube_prompt = " ".join(yt_prompt_list)  

    pywhatkit.playonyt(youtube_prompt)

    reply = f"Playing {youtube_prompt}" 

    return reply





