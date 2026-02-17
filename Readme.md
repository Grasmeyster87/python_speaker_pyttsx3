Here’s a bilingual English/Ukrainian version of your README, formatted cleanly so both languages are side by side:

---

# 🎙️ python_speaker_pyttsx3  

**Playing back text with voices built into the system**  
**Відтворення тексту голосами, вбудованими в систему**

---

## 📖 Description / Опис  
This project uses the **pyttsx3** library to convert text into speech.  
Цей проєкт використовує бібліотеку **pyttsx3** для перетворення тексту на мовлення.  

The program has a graphical interface built with **Tkinter**, allowing you to:  
Програма має графічний інтерфейс на **Tkinter**, що дозволяє:  
- Enter or paste text into an A5-format window  
  Вводити або вставляти текст у вікно формату A5  
- Select a voice from available system voices  
  Обирати голос із доступних системних  
- Adjust speech rate  
  Налаштовувати швидкість мовлення  
- Play back text  
  Відтворювати текст  
- Save speech to an audio file (MP3/WAV)  
  Зберігати мовлення в аудіофайл (MP3/WAV)  
- Reset settings  
  Скидати налаштування  

---

## 🚀 Installation / Установка  
```bash
# Clone the repository
git clone https://github.com/yourusername/python_speaker_pyttsx3.git
cd python_speaker_pyttsx3

# Install dependencies
pip install -r requirements.txt
```

**requirements.txt**:  
```
pyttsx3
```

---

## ▶️ Run / Запуск  
```bash
python main.py
```

---

## 📂 Project structure / Структура проєкту  
```
python_speaker_pyttsx3/
│
├── main.py                  # main program entry point / основний запуск програми
├── gui/
│   ├── __init__.py
│   └── gui.py               # interface logic / логіка інтерфейсу
└── logic/
    ├── __init__.py
    └── speaker.py           # pyttsx3 functions / функції роботи з pyttsx3
```

---

## 📝 Versions / Версії  
- **1.0.0** — Initial version  
  _Початкова версія_

---

## ⚖️ License / Ліцензія  
MIT License — free use and modification.  
MIT License — вільне використання та модифікація.  

---