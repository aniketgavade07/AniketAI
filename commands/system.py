import os


def open_system_app(command):
    if "open calculator" in command:
        os.system("calc")
        return "Opening Calculator"

    if "open notepad" in command:
        os.system("notepad")
        return "Opening Notepad"

    if "open paint" in command:
        os.system("mspaint")
        return "Opening Paint"

    if "open command prompt" in command:
        os.system("start cmd")
        return "Opening Command Prompt"

    if "open powershell" in command:
        os.system("start powershell")
        return "Opening PowerShell"

    if "open file explorer" in command:
        os.system("explorer")
        return "Opening File Explorer"

    if "open task manager" in command:
        os.system("taskmgr")
        return "Opening Task Manager"

    if "open settings" in command:
        os.system("start ms-settings:")
        return "Opening Settings"

    if "open control panel" in command:
        os.system("control")
        return "Opening Control Panel"

    if "open camera" in command:
        os.system("start microsoft.windows.camera:")
        return "Opening Camera"

    if "lock computer" in command:
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return "Locking your computer"

    if "shutdown computer" in command:
        os.system("shutdown /s /t 10")
        return "Computer will shut down in 10 seconds"

    if "restart computer" in command:
        os.system("shutdown /r /t 10")
        return "Computer will restart in 10 seconds"

    if "cancel shutdown" in command:
        os.system("shutdown /a")
        return "Shutdown cancelled"

    return None
