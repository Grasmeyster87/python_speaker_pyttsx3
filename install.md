
python -m venv venv
pip install -r requirements.txt
.\venv\Scripts\Activate
deactivate

pip install pyttsx3

pip freeze > requirements.txt
pip install -r requirements.txt

(venv) PS D:\python_speaker_pyttsx3> python -c "import sys; print(sys.executable)"
D:\python_speaker_pyttsx3\venv\Scripts\python.exe

python python_speaker_pyttsx3.py

------------------------------------
Для того щоб перетворити ваш Python-проєкт на повноцінний Windows-додаток (файл `.exe`), найпопулярнішим і надійним інструментом є **PyInstaller**. Оскільки ваш проєкт має модульну структуру (`gui/`, `logic/`), важливо правильно налаштувати збірку.

Ось покрокова інструкція:

### 1. Підготовка оточення

Найкраще створювати `.exe` у віртуальному середовищі, щоб файл не став занадто важким через зайві бібліотеки.

Відкрийте термінал у папці проєкту та виконайте:

```bash
# Встановлення PyInstaller
pip install pyinstaller
python -m pip install pyinstaller

```

### 2. Створення EXE-файлу

Оскільки ваш головний файл — `main.py`, ви повинні запускати збірку саме для нього. Використовуйте наступну команду:

```bash
pyinstaller --noconsole --onefile --name "MyTTSApp" main.py
python -m PyInstaller --noconsole --onefile --icon=app_icon.ico --name "SpeakerApp" main.py
python -m PyInstaller --noconsole --onefile --hidden-import pyttsx3.drivers.sapi5 --name "SpeakerApp" main.py

```

**Розшифровка прапорців:**

* `--noconsole` (або `-w`): приховує чорне вікно термінала при запуску програми (залишається тільки ваш графічний інтерфейс).
* `--onefile` (або `-F`): збирає все в один єдиний файл `.exe` (зручно для перенесення).
* `--name "MyTTSApp"`: назва вашого майбутнього додатка.

---

### 3. Робота з модулями (`gui` та `logic`)

PyInstaller автоматично аналізує імпорти у вашому коді. Оскільки у `main.py` є рядок `from gui.gui import SpeakerGUI`, а в `gui.py` — `from logic import speaker`, PyInstaller сам знайде ці папки та упакує їх всередину додатка.

> **Важливо:** Якщо ви використовуєте іконки або картинки, їх потрібно додавати окремо за допомогою прапорця `--add-data`.

---

### 4. Де знайти результат?

Після завершення роботи команди у вашій папці з'являться нові каталоги:

1. **`dist/`** — тут лежить готовий файл **`MyTTSApp.exe`**. Саме його ви можете відправляти друзям.
2. **`build/`** — тимчасові файли для збірки (можна видалити).
3. **`MyTTSApp.spec`** — файл конфігурації збірки (можна видалити).

---

### Альтернативний спосіб (Графічний інтерфейс)

Якщо ви не хочете користуватися терміналом, встановіть **Auto-py-to-exe**. Це графічна оболонка для PyInstaller.

1. Встановіть: `pip install auto-py-to-exe`
2. Запустіть: введіть `auto-py-to-exe` у терміналі.
3. У вікні, що відкриється:
* Оберіть шлях до `main.py`.
* Виберіть "One File" та "Window Based" (щоб не було консолі).
* Натисніть кнопку "Convert .py to .exe".



---

### Можливі проблеми з `pyttsx3`

Бібліотека `pyttsx3` іноді потребує специфічних драйверів під час збірки. Якщо після запуску `.exe` виникає помилка "Driver not found", спробуйте створити файл `.spec` та переконатися, що приховані імпорти (hidden imports) включені, але зазвичай PyInstaller останніх версій справляється з цим автоматично.

Бажаєте, щоб я допоміг додати іконку (.ico) до вашого додатка або налаштувати автоматичне підсвічування тексту при запуску саме з EXE?