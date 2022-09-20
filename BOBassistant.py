import speech_recognition as sr
import pyttsx3 as p
import datetime
import pywhatkit as pwt
import wikipedia
import webbrowser
import os 
import json

audios=p.init()

# to get the male voice 
vc=audios.getProperty('voices')
audios.setProperty('voice',vc[0].id)

# to set the speed of the voice 
speed=audios.getProperty('rate')
audios.setProperty('rate',150)

def speak(word):
    audios.say(word)
    audios.runAndWait()

# for wishing me accourding to the time
def greetme():      
    hour=int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Good Morning sir.")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir.")
    elif hour>=18 and hour<21:
        speak("Good Evening sir.")
    else:
        speak("Good night sir.")

greetme()

print("\n\n\t\t***********************************************\n")
print("\t\t\t WELCOME TO BANK OF BARODA   \n")
print("\t\t************************************************\n")
speak(" Myself BOB. Your voice assistant. tell me how may i help you?")

print("As this is a demo version, English is set as te default language....") 
r=sr.Recognizer()

# the main part of this program.
#From here we are taking the voice as a input command.
def take_input():
    try:    #using the microphone as a source for taking voice input
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 0.5)
            print("\n\tListening.....\n")
            voice = r.listen(source)
            # Converting from voice to text.
            text = r.recognize_google(voice)
            print("Your command : "+text)
    except:
        pass
    return text

# And here we are peforming the whole task.
def run():
    process=take_input()
    if "account balance" in process :
        tell="ok sir. Please enter your account number "
        speak("tell ")
        ac_no=input(" Please enter your account  number : ")
        p_w=int(input("Now, Enter your verification pin : "))
        abc="Your account balance is temporarily fixed to rupees 2000."
        print(abc)
        speak(abc)
        
    elif "invest" in process:
        Invest="Our officials shall contact you soon. This is a temporary version and it shall possible in our original software"
        print(Invest)
        speak(Invest)
        
    elif "create an account" in process:
        ans="Our officials shall contact you soon. This is a temporary version and it shall possible in our original software"
        print(ans)
        speak(ans)

    elif "apply for loan" in process:
        ann="Our officials shall contact you soon. This is a temporary version and it shall possible in our original software"
        print(ann)
        speak(ann)

    elif "pay my bills" in process :
        asp="Our officials shall contact you soon. This is a temporary version and it is possible in our original software"
        print(asp)
        speak(asp)       
 
    elif "thank" in process:
        print(" your welcome sir ! visit again ")
        speak("\nyour always welcome sir!\n")
        quit()

    elif 'exit' in process or "stop" in process:
        prnt=" thank you for using me. have a nice day"
        speak(prnt)
        print(prnt)
        quit()   
    else:
       #speak("Sorry sir. Can you please repeat again")
       with open("C:\VOICE ASSISTANT PROJECT/BOBinfo.py") as j_f:
            process=json.load(j_f)

#infinite loop for performing the operation countiniousally.
while True:
    run()