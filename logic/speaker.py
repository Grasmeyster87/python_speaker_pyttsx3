import pyttsx3
import threading

voices = pyttsx3.init().getProperty("voices")

def speak_text(text, rate, voice_index):
    if not text:
        return

    def run_speech():
        engine = pyttsx3.init()
        engine.setProperty("rate", rate)
        engine.setProperty("volume", 0.9)

        if voice_index >= 0:
            engine.setProperty("voice", voices[voice_index].id)

        engine.say(text)
        engine.runAndWait()
        engine.stop()

    threading.Thread(target=run_speech, daemon=True).start()

def save_audio(text, rate, voice_index, filename):
    if not text or not filename:
        return

    def run_save():
        engine = pyttsx3.init()
        engine.setProperty("rate", rate)
        engine.setProperty("volume", 0.9)

        if voice_index >= 0:
            engine.setProperty("voice", voices[voice_index].id)

        engine.save_to_file(text, filename)
        engine.runAndWait()
        engine.stop()

    threading.Thread(target=run_save, daemon=True).start()

def get_voices():
    return voices