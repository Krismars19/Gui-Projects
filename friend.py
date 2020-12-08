import pyttsx3
friend = pyttsx3.init()
speech = input("Say Something: ")
friend.say(speech)
#friend.say("Fear is a reaction, courage is a Decision. Don't follow your passion, let your passion follow you")
friend.runAndWait()
