import pyttsx3
import threading

# Отримуємо список голосів один раз при запуску програми
# Використовуємо тимчасовий об'єкт, щоб не блокувати основний потік
temp_engine = pyttsx3.init()
voices = temp_engine.getProperty("voices")
del temp_engine

# Змінна для зберігання активного двигуна
current_engine = None

def speak_text(text, rate, voice_index, on_word_callback=None):
    if not text:
        return

    # Зупиняємо попередній голос
    stop_speech()

    def run_speech():
        global current_engine
        try:
            engine = pyttsx3.init()
            current_engine = engine

            # Налаштування
            engine.setProperty("rate", rate)
            engine.setProperty("volume", 1.0)

            if voice_index >= 0:
                engine.setProperty("voice", voices[voice_index].id)

            # --- ПІДКЛЮЧЕННЯ ПІДСВІЧУВАННЯ ---
            # Якщо передано функцію callback, підключаємо її до події 'started-word'
            if on_word_callback:
                engine.connect('started-word', on_word_callback)

            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"Error in speech thread: {e}")
        finally:
            current_engine = None

    # Запускаємо в окремому потоці
    t = threading.Thread(target=run_speech, daemon=True)
    t.start()

def stop_speech():
    """Зупиняє поточний активний двигун"""
    global current_engine
    if current_engine:
        try:
            current_engine.stop()
        except:
            pass
        current_engine = None

def save_audio(text, rate, voice_index, filename):
    if not text or not filename:
        return

    def run_save():
        save_engine = pyttsx3.init()
        save_engine.setProperty("rate", rate)
        if voice_index >= 0:
            save_engine.setProperty("voice", voices[voice_index].id)
        
        save_engine.save_to_file(text, filename)
        save_engine.runAndWait()
        del save_engine

    threading.Thread(target=run_save, daemon=True).start()

def get_voices():
    return voices