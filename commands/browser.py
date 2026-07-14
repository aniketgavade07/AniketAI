import os
import webbrowser


def open_browser(command):
    if "open chrome" in command:
        webbrowser.open("https://google.com")
        return "Opening Chrome"

    if "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    if "search google for" in command:
        query = command.replace("search google for", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searching Google for {query}"

    if "search youtube for" in command:
        query = command.replace("search youtube for", "").strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        return f"Searching YouTube for {query}"

    return None
