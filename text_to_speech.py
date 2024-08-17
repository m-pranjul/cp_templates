import win32com.client

say = win32com.client.Dispatch("SAPI.SpVoice")

# speech = input()
speech = "Hola Sir, buenos dias, mucho gusto"

voices = say.GetVoices()
say.speak(speech) # David Voice

say.Voice = voices.Item(1)

say.speak(speech) # Zira Voice



# Can check for available voices
# for i , voice in enumerate(voices):
#     print(f"Voice {i+1}: {voice.GetDescription()}")

