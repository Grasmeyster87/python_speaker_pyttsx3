
python -m venv venv
pip install -r requirements.txt
.\venv\Scripts\Activate

pip install pyttsx3

pip freeze > requirements.txt
deactivate
