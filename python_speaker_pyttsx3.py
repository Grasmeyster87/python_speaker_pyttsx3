import tkinter as tk
from tkinter import ttk, filedialog
import pyttsx3

voices = pyttsx3.init().getProperty("voices")

def get_selected_or_all_text():
    try:
        # пробуем получить выделенный текст
        return text_box.selection_get().strip()
    except tk.TclError:
        # если ничего не выделено — берём весь текст
        return text_box.get("1.0", tk.END).strip()

def speak_text():
    text = get_selected_or_all_text()
    if not text:
        return
    
    engine = pyttsx3.init()
    engine.setProperty("rate", int(rate_scale.get()))
    engine.setProperty("volume", 0.9)

    selected_index = voice_combo.current()
    if selected_index >= 0:
        engine.setProperty("voice", voices[selected_index].id)

    engine.say(text)
    engine.runAndWait()
    engine.stop()

def save_audio():
    text = get_selected_or_all_text()
    if not text:
        return
    
    filename = filedialog.asksaveasfilename(
        defaultextension=".mp3",
        filetypes=[("MP3 files", "*.mp3"), ("WAV files", "*.wav")]
    )
    if not filename:
        return

    engine = pyttsx3.init()
    engine.setProperty("rate", int(rate_scale.get()))
    engine.setProperty("volume", 0.9)

    selected_index = voice_combo.current()
    if selected_index >= 0:
        engine.setProperty("voice", voices[selected_index].id)

    engine.save_to_file(text, filename)
    engine.runAndWait()
    engine.stop()

# GUI
root = tk.Tk()
root.title("Text-to-Speech")

text_box = tk.Text(root, width=60, height=10, wrap="word")
text_box.pack(pady=10)

voice_combo = ttk.Combobox(root, values=[voice.name for voice in voices], state="readonly")
voice_combo.current(0)
voice_combo.pack(pady=10)

rate_label = tk.Label(root, text="Скорость речи")
rate_label.pack()
rate_scale = ttk.Scale(root, from_=100, to=250, orient="horizontal")
rate_scale.set(150)
rate_scale.pack(pady=10)

btn_speak = tk.Button(root, text="Воспроизвести", command=speak_text)
btn_speak.pack(pady=10)

btn_save = tk.Button(root, text="Сохранить в аудиофайл", command=save_audio)
btn_save.pack(pady=10)

root.mainloop()