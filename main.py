import json
import openai
import pyttsx3
import speech_recognition as sr
import webbrowser
from openai_apikey import apikey

openai.api_key = apikey

YourName = "Ayush" 
VoiceAssistantName = "OogaBooga"


def OogaBooga(question):

    prompt=f'{YourName}: {question}\n {VoiceAssistantName}:'

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=['\Ayush']
    )

    with open('user_response_logs.json', 'w') as file:
        file.write(str(response))

    obj = json.loads(str(response))
    list = obj["choices"]

    for i in range(len(list)):
        text_response = list[i].get("text")

    return text_response


def speak(text):

    engine.say(text)
    engine.runAndWait()


def take_Commands():
    r = sr.Recognizer()

    with sr.Microphone() as mic:

        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(mic)

    try:

        print("Recognizing...")
        text = r.recognize_google(audio, language='en-in')
        text = text.lower()
        print(f"{YourName} Said: {text} \n")

    except Exception as e:

        print("Say That Again...")
        speak("Say That Again...")
        return "say I can't hear you"

    return text


engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)


if __name__ == '__main__':

    speak("Welcome back sir. How can i help you?")

    while True:

        user = take_Commands()
        response = OogaBooga(user)
        
        if 'open browser' in user:
            webbrowser.open("www.google.com")

        if 'open youtube' in user:
            webbrowser.open("www.youtube.com")

        if 'open google' in user:
            webbrowser.open("www.google.com")

        if 'open ai website' in user:
            webbrowser.open("https://openai.com/")

        if 'exit' in user:
            speak("It was nice talking with you Sir")
            break
        else:
            print(f'{VoiceAssistantName} Said: {response}')
            speak(response)

