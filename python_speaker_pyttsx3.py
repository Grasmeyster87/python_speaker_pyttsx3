import tkinter as tk
from tkinter import ttk, filedialog
import pyttsx3
import threading

voices = pyttsx3.init().getProperty("voices")

def get_selected_or_all_text():
    try:
        return text_box.selection_get().strip()
    except tk.TclError:
        return text_box.get("1.0", tk.END).strip()

def speak_text():
    text = get_selected_or_all_text()
    if not text:
        return
    
    def run_speech():
        engine = pyttsx3.init()  # новый движок каждый раз
        engine.setProperty("rate", int(rate_scale.get()))
        engine.setProperty("volume", 0.9)

        selected_index = voice_combo.current()
        if selected_index >= 0:
            engine.setProperty("voice", voices[selected_index].id)

        engine.say(text)
        engine.runAndWait()
        engine.stop()

    threading.Thread(target=run_speech, daemon=True).start()

def pause_playback():
    # пауза = остановка, возобновить нельзя
    # поэтому просто ничего не делаем, если движок пересоздаётся каждый раз
    pass

def reset_engine():
    voice_combo["values"] = [voice.name for voice in voices]
    voice_combo.current(0)
    rate_scale.set(150)

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

    def run_save():
        engine = pyttsx3.init()
        engine.setProperty("rate", int(rate_scale.get()))
        engine.setProperty("volume", 0.9)

        selected_index = voice_combo.current()
        if selected_index >= 0:
            engine.setProperty("voice", voices[selected_index].id)

        engine.save_to_file(text, filename)
        engine.runAndWait()
        engine.stop()

    threading.Thread(target=run_save, daemon=True).start()

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
btn_speak.pack(pady=5)

btn_pause = tk.Button(root, text="Пауза (остановка)", command=pause_playback)
btn_pause.pack(pady=5)

btn_reset = tk.Button(root, text="Сброс", command=reset_engine)
btn_reset.pack(pady=5)

btn_save = tk.Button(root, text="Сохранить в аудиофайл", command=save_audio)
btn_save.pack(pady=10)

root.mainloop()