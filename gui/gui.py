import tkinter as tk
from tkinter import ttk, filedialog
from logic import speaker

class SpeakerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Text-to-Speech")

        self.text_box = tk.Text(
            root,
            width=90,   # ширина (символи)
            height=30,  # висота (рядки)
            wrap="word"
            )
        self.text_box.pack(pady=10)


        self.voice_combo = ttk.Combobox(root, values=[v.name for v in speaker.get_voices()], state="readonly")
        self.voice_combo.current(0)
        self.voice_combo.pack(pady=10)

        self.rate_label = tk.Label(root, text="Скорость речи")
        self.rate_label.pack()
        self.rate_scale = ttk.Scale(root, from_=100, to=250, orient="horizontal")
        self.rate_scale.set(150)
        self.rate_scale.pack(pady=10)

        # панель кнопок
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        self.btn_reset = tk.Button(button_frame, text="Сброс", command=self.reset_engine)
        self.btn_reset.pack(side="left", padx=5)

        self.btn_speak = tk.Button(button_frame, text="Воспроизвести", command=self.speak_text)
        self.btn_speak.pack(side="left", padx=5)

        self.btn_pause = tk.Button(button_frame, text="Пауза", command=self.pause_playback)
        self.btn_pause.pack(side="left", padx=5)

        self.btn_save = tk.Button(root, text="Сохранить в аудиофайл", command=self.save_audio)
        self.btn_save.pack(pady=10)

    def get_text(self):
        try:
            return self.text_box.selection_get().strip()
        except tk.TclError:
            return self.text_box.get("1.0", tk.END).strip()

    def speak_text(self):
        text = self.get_text()
        speaker.speak_text(text, int(self.rate_scale.get()), self.voice_combo.current())

    def pause_playback(self):
        pass  # пока не реализовано

    def reset_engine(self):
        self.voice_combo["values"] = [v.name for v in speaker.get_voices()]
        self.voice_combo.current(0)
        self.rate_scale.set(150)

    def save_audio(self):
        text = self.get_text()
        filename = filedialog.asksaveasfilename(
            defaultextension=".mp3",
            filetypes=[("MP3 files", "*.mp3"), ("WAV files", "*.wav")]
        )
        if filename:
            speaker.save_audio(text, int(self.rate_scale.get()), self.voice_combo.current(), filename)