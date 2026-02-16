import random
import pyttsx3

frases = [
    "El éxito es disciplina repetida.",
    "Haz lo que otros no quieren hacer.",
    "La constancia vence al talento.",
    "Cada día cuenta.",
    "No negocies con tu debilidad."
]

frase_aleatoria = random.choice(frases)
print(frase_aleatoria)
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
engine.say(frase_aleatoria)
engine.runAndWait()
