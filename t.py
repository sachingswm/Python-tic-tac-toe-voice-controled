import pyttsx3
import speech_recognition as sr 
import pyaudio as p
import os
import datetime


engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(q):
    engine.say(q)
    engine.runAndWait()
    
def InputSpeech():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio)
        print("You said..:",query)
    except Exception as e:
        print(e)
        print("Sorry say again")
        return InputSpeech() 
    return query



print("Sir ,I Am Maryion What can I Do For You")
speak("Sir ,I Am Maryion What can I Do For You")

List=[['','',''],['','',''],['','','']]
print("Speak first player character:")
s=("Speak first player character:")
speak(s)
a=InputSpeech()
print(a)
print("Speak second player character:")
s=("Speak second player character:")
speak(s)
b=InputSpeech()
print(b)

print("You can place your character according to this Matrix:")
print("7 8 9\n4 5 6\n1 2 3")

c=0
while(c<8):
       
    r=0
    win=0
    print("Enter the location")
    speak("Enter the location")
    L=(InputSpeech())
    if L=='1' or L=='2' or L=='3' or L=='4' or L=='5' or L=='6' or L=='7' or L=='8' or L=='9':
        L=int(L)
    else:
        print("Invalid Location enterd by You")
        speak("Invalid Location enterd by You")
        continue
        
    if c%2==0:
        if L==7:
            if List[0][0]==a or List[0][0]==b:
                continue
            List[0][0]=a
            c=c+1
        elif L==8:
            if List[0][1]==a or List[0][1]==b:
                continue
            List[0][1]=a
            c=c+1
        elif L==9:
            if List[0][2]==a or List[0][2]==b:
                continue
            List[0][2]=a
            c=c+1
        elif L==4:
            if List[1][0]==a or List[1][0]==b:
                continue
            List[1][0]=a
            c=c+1
        elif L==5:
            if List[1][1]==a or List[1][1]==b:
                continue
            List[1][1]=a
            c=c+1
        elif L==6:
            if List[1][2]==a or List[1][2]==b:
                continue
            List[1][2]=a
            c=c+1
        elif L==1:
            if List[2][0]==a or List[2][0]==b:
                continue
            List[2][0]=a
            c=c+1
        elif L==2:
            if List[2][1]==a or List[2][1]==b:
                continue
            List[2][1]=a
            c=c+1
        elif L==3:
            if List[2][2]==a or List[2][2]==b:
                continue
            List[2][2]=a
            c=c+1
        for i in range(3):
            for j in range(3):
                if List[i][j]==a:
                    r=r+1
            if r==3:
                print("Player 1 wins")
                speak("yehh Player 1 wins")
                win=1
                break
            else:
                r=0
            

        for i in range(3):
            for j in range(3):
                if List[j][i]==a:
                    r=r+1
            if r==3:
                print("Player 1 wins")
                speak("yehh Player 1 wins")
                win=1
                break
            else:
                r=0


        for i in range(3):
            if List[i][i]==a:
                r=r+1
        if r==3:
            print("Player 1 wins")
            speak("yehh Player 1 wins")
            win=1
            
        else:
            r=0

        u=2
        for i in range(3):
            if List[i][u]==a:
                r=r+1
            u=u-1
        if r==3:
            print("Player 1 wins")
            speak("yehh Player 1 wins")
            win=1
            
        else:
            r=0
            

        


        if win==1:
            for i in List:
                print(i)
            break

        for i in List:
            print(i)

            
 
    
    else:
        if L==7:
            if List[0][0]==a or List[0][0]==b:
                continue
            List[0][0]=b
            c=c+1
        elif L==8:
            if List[0][1]==a or List[0][1]==b:
                continue
            List[0][1]=b
            c=c+1
        elif L==9:
            if List[0][2]==a or List[0][2]==b:
                continue
            List[0][2]=b
            c=c+1
        elif L==4:
            if List[1][0]==a or List[1][0]==b:
                continue
            List[1][0]=b
            c=c+1
        elif L==5:
            if List[1][1]==a or List[1][1]==b:
                continue
            List[1][1]=b
            c=c+1
        elif L==6:
            if List[1][2]==a or List[1][2]==b:
                continue
            List[1][2]=b
            c=c+1
        elif L==1:
            if List[2][0]==a or List[2][0]==b:
                continue
            List[2][0]=b
            c=c+1
        elif L==2:
            if List[2][1]==a or List[2][1]==b:
                continue
            List[2][1]=b
            c=c+1
        elif L==3:
            if List[2][2]==a or List[2][2]==b:
                continue
            List[2][2]=b
            c=c+1
        for i in range(3):
            for j in range(3):
                if List[i][j]==b:
                    r=r+1
            if r==3:
                print("Player 2 wins")
                speak("Player 2 wins")
                win=1
                break
            else:
                r=0
            

        for i in range(3):
            for j in range(3):
                if List[j][i]==b:
                    r=r+1
            if r==3:
                print("Player 2 wins")
                speak("yehh Player 2 wins")
                win=1
                break
            else:
                r=0


        for i in range(3):
            if List[i][i]==b:
                r=r+1
        if r==3:
            print("Player 2 wins")
            speak("yehh Player 2 wins")
            win=1
            
        else:
            r=0

        u=2
        for i in range(3):
            if List[i][u]==b:
                r=r+1
            u=u-1
        if r==3:
            print("Player 2 wins")
            speak("yehh Player 2 wins")
            win=1
            
            
        else:
            r=0
        
        
        
        
        if win==1:
            for i in List:
                print(i)
            break

        for i in List:
            print(i)
        
        
if c==9:
    print("Filled Totally Draw")
    speak("Filled Totally Draw")
            
                
    
        
        

    


    

