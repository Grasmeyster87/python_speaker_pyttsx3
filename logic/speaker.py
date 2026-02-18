import pyttsx3
import threading

# Ініціалізуємо двигун один раз на рівні модуля
engine = pyttsx3.init()
voices = engine.getProperty("voices")

def speak_text(text, rate, voice_index):
    if not text:
        return

    def run_speech():
        # Налаштовуємо параметри перед запуском
        engine.setProperty("rate", rate)
        engine.setProperty("volume", 0.9)

        if voice_index >= 0:
            engine.setProperty("voice", voices[voice_index].id)

        # Якщо двигун уже щось говорить, зупиняємо, щоб почати нове
        engine.stop() 
        engine.say(text)
        engine.runAndWait()

    # Запускаємо в окремому потоці, щоб GUI не зависав
    threading.Thread(target=run_speech, daemon=True).start()

def stop_speech():
    """Функція для негайної зупинки мовлення"""
    engine.stop()

def save_audio(text, rate, voice_index, filename):
    if not text or not filename:
        return

    # Для збереження у файл краще використовувати окремий локальний об'єкт, 
    # щоб не конфліктувати з потоковим відтворенням
    save_engine = pyttsx3.init()
    save_engine.setProperty("rate", rate)
    if voice_index >= 0:
        save_engine.setProperty("voice", voices[voice_index].id)
    
    save_engine.save_to_file(text, filename)
    save_engine.runAndWait()

def get_voices():
    return voices