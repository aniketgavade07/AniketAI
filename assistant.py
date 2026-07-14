from core.listen import listen
from core.speak import speak
from core.ai import ask_ai
from core.memory import remember, show_memory
from commands import execute


def run_assistant():
    speak("Hello Aniket. I am online and ready to help.")

    while True:

        command = listen()

        if not command:
            continue

        print("Command:", command)

        # Exit
        if "exit" in command or "goodbye" in command or "bye" in command:
            speak("Goodbye Aniket. Have a nice day.")
            break

        # Memory
        elif command.startswith("remember "):
            text = command.replace("remember ", "")
            memory = show_memory()
            remember(f"note_{len(memory)+1}", text)
            speak("Okay. I will remember that.")
            continue

        elif "what do you remember" in command:
            memory = show_memory()

            if not memory:
                speak("I don't remember anything yet.")
            else:
                for value in memory.values():
                    speak(value)

            continue

        # Windows Commands
        response = execute(command)

        # If command not found, ask AI
        if response == "Sorry, I don't know that command yet.":
            response = ask_ai(command)

        speak(response)