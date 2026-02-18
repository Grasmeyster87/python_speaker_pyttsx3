import pyttsx3
import threading

# Отримуємо список голосів один раз при запуску програми
# Використовуємо тимчасовий об'єкт, щоб не блокувати основний потік
temp_engine = pyttsx3.init()
voices = temp_engine.getProperty("voices")
del temp_engine

# Змінна для зберігання активного двигуна (щоб ми могли його зупинити)
current_engine = None

def speak_text(text, rate, voice_index):
    if not text:
        return

    # Зупиняємо попередній голос, якщо він ще звучить
    stop_speech()

    def run_speech():
        global current_engine
        try:
            # Створюємо НОВИЙ двигун для кожного запуску (це вирішує проблему зависання)
            engine = pyttsx3.init()
            current_engine = engine # Запам'ятовуємо його, щоб працювала Пауза

            # Налаштування
            engine.setProperty("rate", rate)
            engine.setProperty("volume", 1.0)

            if voice_index >= 0:
                engine.setProperty("voice", voices[voice_index].id)

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

    # Функція збереження працює окремо, тут теж створюємо свій екземпляр
    def run_save():
        save_engine = pyttsx3.init()
        save_engine.setProperty("rate", rate)
        if voice_index >= 0:
            save_engine.setProperty("voice", voices[voice_index].id)
        
        save_engine.save_to_file(text, filename)
        save_engine.runAndWait() # Це важливо для запису файлу
        del save_engine

    threading.Thread(target=run_save, daemon=True).start()

def get_voices():
    return voices