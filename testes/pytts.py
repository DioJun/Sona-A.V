import pyttsx3

# Síntese de fala
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

engine.say('Olá senhor. Como posso ajudar?')
engine.runAndWait()