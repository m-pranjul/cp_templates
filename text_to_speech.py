import win32com.client

say = win32com.client.Dispatch("SAPI.SpVoice")

speech = input()

say.speak(speech)