import tkinter as tk
from tkinter import ttk
import pyttsx3

voices = pyttsx3.init().getProperty("voices")

def speak_text():
    text = entry.get()
    if not text.strip():
        return
    
    # каждый раз создаём новый движок
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 0.9)

    selected_index = voice_combo.current()
    if selected_index >= 0:
        engine.setProperty("voice", voices[selected_index].id)

    engine.say(text)
    engine.runAndWait()
    engine.stop()  # очищаем очередь

# GUI
root = tk.Tk()
root.title("Text-to-Speech")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

voice_combo = ttk.Combobox(root, values=[voice.name for voice in voices], state="readonly")
voice_combo.current(0)
voice_combo.pack(pady=10)

btn = tk.Button(root, text="Воспроизвести", command=speak_text)
btn.pack(pady=10)

root.mainloop()