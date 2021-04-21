# import speech_recognition as sr
# #
# def speech_text(file):
#
#     recognizer = sr.Recognizer()
#     audioFile = sr.AudioFile(file)
#     with audioFile as source:
#         data = recognizer.record(source)
#     transcript = recognizer.recognize_google(data, key=None)