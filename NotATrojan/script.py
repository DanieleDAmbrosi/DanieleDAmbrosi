import win32ui

def WindowExists(classname):
    try:
        win32ui.FindWindow(classname, None)
    except win32ui.error:
        return False
    else:
        return True

if WindowExists("Shell_TrayWnd"):
    print("TRUE")
else:
    print("FALSE")

"""gets if the process is running or not"""