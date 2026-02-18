import tkinter as tk
from tkinter import ttk, filedialog
from logic import speaker

class SpeakerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Text-to-Speech")

        # --- БЛОК ТЕКСТУ ТА СКРОЛЛУ ---
        text_frame = tk.Frame(root)
        text_frame.pack(pady=10, padx=10)

        self.scrollbar = tk.Scrollbar(text_frame)
        self.scrollbar.pack(side="right", fill="y")

        self.text_box = tk.Text(
            text_frame,
            width=90,
            height=20,
            wrap="word",
            yscrollcommand=self.scrollbar.set 
        )
        self.text_box.pack(side="left", fill="both", expand=True)
        self.scrollbar.config(command=self.text_box.yview)

        # Налаштування стилю для підсвічування (жовтий фон, чорний текст)
        self.text_box.tag_config("highlight", background="yellow", foreground="black")

        # --- НАЛАШТУВАННЯ ---
        self.voice_combo = ttk.Combobox(root, values=[v.name for v in speaker.get_voices()], state="readonly", width=50)
        if speaker.get_voices():
            self.voice_combo.current(0)
        self.voice_combo.pack(pady=10)

        self.rate_label = tk.Label(root, text="Швидкість мовлення")
        self.rate_label.pack()
        self.rate_scale = ttk.Scale(root, from_=100, to=300, orient="horizontal")
        self.rate_scale.set(180)
        self.rate_scale.pack(pady=10, fill="x", padx=100)

        # --- КНОПКИ ---
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        self.btn_reset = tk.Button(button_frame, text="Скинути налаштування", command=self.reset_engine)
        self.btn_reset.pack(side="left", padx=5)

        self.btn_speak = tk.Button(button_frame, text="Відтворити", command=self.speak_text, bg="#e1f5fe")
        self.btn_speak.pack(side="left", padx=5)

        self.btn_pause = tk.Button(button_frame, text="Пауза", command=self.pause_playback, bg="#ffebee")
        self.btn_pause.pack(side="left", padx=5)

        self.btn_save = tk.Button(root, text="Зберегти в аудіофайл", command=self.save_audio)
        self.btn_save.pack(pady=10)

    def get_text(self):
        try:
            selected_text = self.text_box.get(tk.SEL_FIRST, tk.SEL_LAST).strip()
            # Якщо є виділення, повертаємо його, але для коректного підсвічування
            # краще працювати з повним текстом, або інакше рахувати індекси.
            # Поки що для простоти підсвічування працюватиме глобально по тексту.
            return selected_text if selected_text else self.text_box.get("1.0", tk.END).strip()
        except tk.TclError:
            return self.text_box.get("1.0", tk.END).strip()

    def speak_text(self):
        text = self.get_text()
        if text:
            speaker.stop_speech()
            # Передаємо callback функцію для підсвічування
            speaker.speak_text(
                text, 
                int(self.rate_scale.get()), 
                self.voice_combo.current(),
                on_word_callback=self.process_word
            )

    def process_word(self, name, location, length):
        """Цей метод викликається з потоку speaker, тому оновлюємо GUI через after"""
        self.root.after(0, lambda: self.highlight_word(location, length))

    def highlight_word(self, location, length):
        """Метод для виділення слова в текстовому полі"""
        # Видаляємо старе виділення
        self.text_box.tag_remove("highlight", "1.0", tk.END)
        
        # Обчислюємо позиції (Tkinter використовує формат "ряд.символ")
        # Оскільки ми передаємо весь текст, location - це індекс символу від початку
        start_index = f"1.0 + {location} chars"
        end_index = f"1.0 + {location + length} chars"
        
        # Додаємо тег
        self.text_box.tag_add("highlight", start_index, end_index)
        
        # Автоматична прокрутка до слова, яке читається
        self.text_box.see(start_index)

    def pause_playback(self):
        speaker.stop_speech()
        self.text_box.tag_remove("highlight", "1.0", tk.END) # Прибираємо виділення при паузі

    def reset_engine(self):
        speaker.stop_speech()
        self.text_box.tag_remove("highlight", "1.0", tk.END)
        self.rate_scale.set(180)
        if speaker.get_voices():
            self.voice_combo.current(0)

    def save_audio(self):
        text = self.get_text()
        if not text:
            return
        filename = filedialog.asksaveasfilename(
            defaultextension=".mp3",
            filetypes=[("MP3 files", "*.mp3"), ("WAV files", "*.wav")]
        )
        if filename:
            speaker.save_audio(text, int(self.rate_scale.get()), self.voice_combo.current(), filename)