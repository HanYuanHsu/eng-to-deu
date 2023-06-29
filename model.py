import os
import openai

class NoKeyError(Exception):
    pass

api_key = os.getenv("OPENAI_API_KEY", "")
if api_key != "":
    openai.api_key = api_key
else:
    raise NoKeyError("OPENAI_API_KEY is not set")

ROLE_DESCRIPTION = "You are a native English and German speaker. Given the English sentence, translate it into German."

def gpt_eng_to_deu(eng_sentence): 

    msg=[
        {"role": "system", "content": ROLE_DESCRIPTION},
        {"role": "user", "content": "Good Morning!"},
        {"role": "assistant", "content": "Guten Morgen!"},
        {"role": "user", "content": "Good Morning! What are your plans today?"},
        {"role": "assistant", "content": "Guten Morgen! Was sind deine Pläne für heute?"},
        {"role": "user", "content": eng_sentence}
    ]
    
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=msg,
      temperature=0
    )


    return response.choices[0]['message']['content']


