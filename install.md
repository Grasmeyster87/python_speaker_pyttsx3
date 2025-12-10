
python -m venv venv
pip install -r requirements.txt
.\venv\Scripts\Activate

pip install pyttsx3

pip freeze > requirements.txt
deactivate


(venv) PS D:\python_speaker_pyttsx3> python -c "import sys; print(sys.executable)"
D:\python_speaker_pyttsx3\venv\Scripts\python.exe

python python_speaker_pyttsx3.py