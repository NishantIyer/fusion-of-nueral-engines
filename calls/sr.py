import speech_recognition as sr
import playsound  # to play saved mp3 file
from gtts import gTTS  # google text to speech
import os  # to save/open files
import openai
import requests
num = 1
openai.api_key = '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'
def assistant_speaks(output):
    global num
    num += 1
    print("Proxie : ", output)
    toSpeak = gTTS(text=output, lang='en', slow=False)
    file = str(num) + ".mp3"
    toSpeak.save(file)
    playsound.playsound(file, True)
    os.remove(file)
def get_audio():
    rObject = sr.Recognizer()
    audio = ''
    with sr.Microphone() as source:
        print("Speak...")
        # recording the audio using speech recognition
        audio = rObject.listen(source, phrase_time_limit=5)
    print("Stop.")  # limit 5 secs
    try:
        text = rObject.recognize_google(audio, language='en-US')
        print("You : ", text)
        return text
    except:
        assistant_speaks("Could not understand your audio, PLease try again !")
        return 0
def sarcasm():
    globals()['sa'] = get_audio().lower()
    response = response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"Marv is a chatbot that reluctantly answers questions with sarcastic responses:\n\nYou:{str(sa)}",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    stop = ["\n", " Human:", ]
    answer = response.choices[0].text.strip()
    assistant_speaks(answer)
def grammar():
    g = get_audio().lower()
    response = response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"Correct this to standard English:\n\n{str(g)}",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    stop = ["\n", " Human:", ]
    answer = response.choices[0].text.strip()
    assistant_speaks(answer)
def qanda():
    globals()['q'] = get_audio().lower()
    response = response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"Q: {str(q)}",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    stop = ["\n", " Human:", ]

    answer = response.choices[0].text.strip()
    assistant_speaks(answer)
def summarise():
    globals()['s'] = get_audio().lower()
    response = response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"Summarize this for a second-grade student:\n\n{str(s)}",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    stop = ["\n", " Human:", ]
    answer = response.choices[0].text.strip()

    assistant_speaks(answer)
def dall():
    globals()['dal'] = get_audio().lower()
    response = openai.Image.create(
        prompt=str(dal),
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    assistant_speaks(image_url)
if __name__ == "__main__":
    assistant_speaks("Hello, I am Proxie. The most advanced voice assistant at your service")
    while 1==1:
        text = get_audio().lower()
        if text == 0:
            continue
        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
            assistant_speaks("Ok bye, ")
            break
        if "grammar correction" in str(text) or "grammar" in str(text) or "grammer" in str(text):
            grammar()
        if "q and a" in str(text) or "qanda" in str(text) or "Q and A" in str(text):
            qanda()
        if "summarize" in str(text) or "summarise" in str(text) or "sumarise" in str(text) or "suma rice" in str(text) :
            summarise()
        if "Sarcasm" in str(text) or "sarcasm" in str(text) or "sir casm" in str(text):
            sarcasm()
        if "dall e" in str(text) or "dail" in str(text) or "daile" in str(text):
            dall()
        else:
            if str(text) != grammar or str(text) != q and a or str(text) != summarise:
                ur = f"http://api.brainshop.ai/get?bid=170226&key=qje9vuLTq5llXvvE&uid=[uid]&msg={str(text)}"
                r = requests.get(ur)
                json_data = r.json()
                message = json_data['cnt']
                assistant_speaks(message)
