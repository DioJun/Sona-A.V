import pyttsx3

# Síntese de fala
engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-5)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

engine.say('Olá senhor. Como posso ajudar?')
engine.runAndWait()

def onStart(name):
   print('starting', name)
def onWord(name, location, length):
   print('word', name, location, length)
def onEnd(name, completed):
   print('finishing', name, completed)
engine = pyttsx3.init()
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()