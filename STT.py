import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)


IBM_USERNAME = "apikey"
IBM_PASSWORD ='2gR3zWF95ZWBauh6hQfnZ71cISZ7Rpv62EOmCx8achiu'
result= r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)

try:
       print("IBM Speech to Text thinks you said " + result)
except sr.UnknownValueError:
    print("IBM Speech to Text could not understand audio")
except sr.RequestError as e:
    print("Could not request results from IBM Speech to Text service; {0}".format(e))

    
with open('my_result.txt',mode ='w') as file: 
   file.write("Recognized text:") 
   file.write("\n") 
   file.write(result) 
print("Exporting process completed!")