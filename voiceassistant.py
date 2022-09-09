import speech_recognition as sr
import pyttsx3 as p
import datetime
import pywhatkit as pwt
import wikipedia
import pyjokes
import webbrowser
import os 


audios=p.init()

# to get the voice 
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
print("\t\t\tyour's welcome sir YADAV here .\n")
print("\t\t************************************************\n")
speak(" myself yadav. your voice assistant. tell me how may i help you.")

#speak("\n IN which language are you comfortale with.? plz choose your language from the below option")

# for recoignizing the input voice 
r=sr.Recognizer()

# the main part of this program.
#From here we are taking the voice as a input command.
def take_input():
    try:    #using the microphone as a source for taking voice input
        with sr.Microphone() as source:
            print("\n\tlistening.....\n")
            voice = r.listen(source)
            # Converting from voice to text.
            text = r.recognize_google(voice)
            print("your command : "+text)
    except:
        pass
    return text

# And here we are peforming the whole task.
def run():
    process=take_input()
    if "time" in process :
        time=datetime.datetime.now().strftime('%I : %M %p')
        print(time)
        speak(" sir. The current time is "+time)

    elif "date" in process:
        Day = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today is {Day}")
        print(Day)

    elif "hey"  in process or "hello" in  process:
        ans=" hlo sir. how may i help you."
        #print(ans)
        speak(ans)

    elif "play" in process or "youtube" in process or "song" in process:
        tell=" sure sir opening youtube"
        speak(tell)
        pwt.playonyt(process)

    elif "tired" in process or "feeling" in process:
        s=" ok sir. playing your favorite song"
        speak(s)
        pwt.playonyt("https://www.youtube.com/watch?v=Aag8lBwCBK0")


    elif "who" in process or "what" in process:
        search=process.replace(" who is ","")
        info=wikipedia.summary(search,1)
        print(info)
        speak("accourding to wikipedia"+info)

    elif "love" in process:
        speak(" yes sir, i love you too. what's the command for me")
    
    elif "think" in process:
        speak(" sir i think you are a good person ")

    elif "google" in process or "search" in process:
        process= process.replace("open google and search","")
        do= " ok sir opening google"
        speak(do)
        url='https://google.com/search?q='+process[process.find('search')+6:]
        webbrowser.get().open(url)
        speak(" here is the some information about"+process)
        
    elif "tell" in process or "about" in process:
        answer=" my name is yadav. i am a voice assistant and i am designed by mister nitish yadav. and i'm here to serve you. tell me what can i do"
        print(answer)
        speak("sure sir. as you can see.` "+answer)

    elif  'show' in process or 'where' in process or 'location' in process:
        speak(" sure sir. opening map ")
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
    
    elif 'joke' in process:
        speak(pyjokes.get_joke())

    elif "how" in process or "are" in process:
        speak(" i am fine sir. thank you. tell me what's the command for me")  
    
    elif 'send' in process or 'whatsapp' in process:
        t='opening whatsapp'
        speak(t)
        process=process.replace("send a message"," ")
        pwt.sendwhatmsg("+919023292761","messages",15,11)

    elif "calculation" in process or "calculate" in process:
        speak("ok sir. plz enter the operator")
        opr =input(" operator = ")

        speak(" now enter the two numbers : ")
        n1=int(input())
        n2=int(input())
        if opr == '+' or 'plus':
            r=n1+n2
            speak(" here is the result ")
            print(r)
        elif opr == '-' or 'minus':
            r=n1-n2
            speak(" here is the result ")
            print(r)
        elif opr == 'multiply' or 'x':
            r=n1*n2
            speak(" here is the result ")
            print(r)
        elif opr == 'divide' or '/':
            r=n1/n2
            speak(" here is the result ")
            print(r)
        elif opr == 'power' or '^':
            r=n1**n2
            speak(" here is the result ")
            print(r)
        else:
            speak("Wrong Operator")
 
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
       speak("sorry sir.can you repeat again")

#infinite loop for performing the operation countiniousally.
while True:
    run()
