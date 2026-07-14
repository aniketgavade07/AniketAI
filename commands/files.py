def personal_response(command):
    if "who are you" in command:
        return "I am Aniket AI, your personal assistant."

    if "who created you" in command:
        return "I was created by Aniket Gavade."

    if "hello" in command:
        return "Hello Aniket! How can I help you today?"

    if "thank you" in command:
        return "You're welcome."

    return None
