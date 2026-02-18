import tkinter as tk
from gui.gui import SpeakerGUI

def main():
    root = tk.Tk()
    app = SpeakerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()