#Sample code for SMS decoder
import re, string
def chatDecoder():
    abr=['b1','141','AA','AAK','AAF','A3','LOL','IAAG','FR']
    longAbr=['be one','one for all and all for one','Ask about','Alive and kicking/Asleep at keyboard','As a friend/As a matter of fact','Anytime, Anywhere, Anyplace',\
            'laugh out loud','i am a Genuis','for real']
    message=input("What message do you want decoded? \n")
    translator = str.maketrans({key: None for key in string.punctuation})
    message=message.translate(translator)
    messageToList=message.split() # change a sentence into a list so that i can loop through the words.
    
    for i in messageToList:
        modifiedMessage=""
        for j in abr:
            #if i==j:
            if re.fullmatch(i, j, re.IGNORECASE):
                i=longAbr[abr.index(j)]  
                # here italicize i
            else:
                i=i
        modifiedMessage+=i 
        modifiedMessage=modifiedMessage.lower()
        print(modifiedMessage, end=" ") # The end=" ", prints the output horizontally
    print(".")
    return

chatDecoder()
