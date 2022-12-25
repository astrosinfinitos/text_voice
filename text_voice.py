from gtts import gTTS

def tts(text_file, lang, name_file):
	with open(text_file, "r") as file:
		text = file.read()
	file = gTTS(text=text,lang=lang)
	filename = name_file
	file.save(filename)

tts("universo.txt", "es", "universo.mp3") #Cambia el contenido del archivo universo.txt y pon lo que quieras oir.
