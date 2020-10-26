import pyttsx3
import time

score = 0
full_questions = 4


speak = pyttsx3.init()

speak.say("Please Enter your name here")
speak.runAndWait()
name = input("Enter your name here: ").lower()

print("Welcome to Cyberxploit simple text-based Game", name)
speak.say(f"{'Welcome to Cyberxploit simple text-based Game!'} {name}" )
speak.runAndWait()

speak.say("Are you going to play? yes or no")
speak.runAndWait()
wants_to_play = input("Are you going to play? (yes/no) ").lower()

if wants_to_play == "yes":

    #Question one
    speak.say("What is the output of 28 + 21 minus 20. ")
    speak.runAndWait()
    question = int(input("1. What is the output of 28 + 21 - 20 ? "))
    
    if question == 29:
        score += 1
        print("Correct")
        speak.say("Correct")
        speak.runAndWait()
      
    else:
        print("Incorrect")
        speak.say("Incorrect")
        speak.runAndWait()

    #Question two
    speak.say("Which is the best programming language. ")
    speak.runAndWait()
    question = input("2. Which is the best programming language? ").lower()
    
    if question == "python":
        score += 1
        print("Correct")
        speak.say("Correct")
        speak.runAndWait()
      
    else:
        print("Incorrect")
        speak.say("Incorrect")
        speak.runAndWait()

    #Question three
    speak.say("What is my full name. ")
    speak.runAndWait()
    question = input("3. What is my full name ? ").lower()
    
    if question == "yazeed ahmed" or question == "ahmed yazeed":
        score += 1
        print("Correct")
        speak.say("Correct")
        speak.runAndWait()
      
    else:
        print("Incorrect")
        speak.say("Incorrect")
        speak.runAndWait()

    #Question four
    speak.say("What is my channels name on youtube. ")
    speak.runAndWait()
    question = input("4. What is my channel's name on youtube ? ").lower()
    
    if question == "cyberxploit":
        score += 1
        print("Correct")
        speak.say("Correct")
        speak.runAndWait()
      
    else:
        print("Incorrect")
        speak.say("Incorrect")
        speak.runAndWait()

    time.sleep(1)
    print("You have got", score, "questions correctly")
    speak.say(f"{'You have got'} {score} {'questions correctly'}")
    speak.runAndWait()
    time.sleep(1)
    mark = (score/full_questions)*100
    print("Mark: ", mark, "%")

    if mark == 100:
        time.sleep(1)
        print("You won!!!")
        speak.say(f"{'Bum Bum Bum! Congratulations!'} {name} {'You won!!!'}")
        speak.runAndWait()
    else:
        time.sleep(2)
        print("Try again harder next time")
        speak.say("Try again harder next time")
        speak.runAndWait()
        



elif wants_to_play == "no":
    time.sleep(.3)
    print("Heyya mate. Thanks for your time...")
    speak.say("Heyya mate. Thanks for your time!")
    speak.runAndWait()
    time.sleep(.4)
    print("Quiting")
else:
    time.sleep(.5)
    print("If you change your mind")
    speak.say("If you change your mind")
    speak.runAndWait()

    time.sleep(.5)
    print("Re-run the program by pressing up arrow key and the return[Enter] key.")
    print("Bye!")
    speak.say("Re-run the program by pressing up arrow key and the return[Enter] key.")
    speak.runAndWait()
    

speak.runAndWait()