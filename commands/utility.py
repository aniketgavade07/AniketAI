from datetime import datetime


def get_utility_response(command):
    if "time" in command:
        now = datetime.now().strftime("%I:%M %p")
        return f"The time is {now}"

    if "date" in command:
        today = datetime.now().strftime("%d %B %Y")
        return f"Today is {today}"

    return None
