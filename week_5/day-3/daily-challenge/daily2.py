from googletrans import Translator

translater = Translator()

display = translater.translate("kayf haluk", dest="fr")

print(display)