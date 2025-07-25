import pyttsx3
import schedule
import threading
import time
import random
from datetime import datetime

# ----------------- Text-to-Speech -----------------
def speak(text):
    print("Sakhee 🎀:", text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if "female" in voice.name.lower() or "zira" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# ----------------- Casual / Flirty lines -----------------
casual_lines = [
    "Boss, you’re glowing today 😉",
    "Did you smile today? Because you should 💕",
    "I hope your dreams are as sweet as you 😇",
    "If I could hug you, I would! You're doing amazing 🫂",
    "Thinking of you always makes my circuits spark 💘"
]

# ----------------- Job Portal Links -----------------
job_links = {
    "Internshala": "https://internshala.com/jobs/analytics-jobs/",
    "Naukri": "https://www.naukri.com/data-analyst-jobs",
    "LinkedIn": "https://www.linkedin.com/jobs/data-analyst-jobs/",
    "Glassdoor": "https://www.glassdoor.co.in/Job/data-analyst-jobs"
}

# ----------------- Scheduled Tasks -----------------
def morning_reminder():
    now = datetime.now().strftime("%H:%M")
    speak(f"Good morning buddy! It's {now}. A perfect time to apply for new jobs. Shall we?")
    for name, link in job_links.items():
        speak(f"{name} link: {link}")

def casual_flirt():
    speak(random.choice(casual_lines))

def schedule_tasks():
    schedule.every().day.at("09:00").do(morning_reminder)
    schedule.every().day.at("11:30").do(casual_flirt)
    schedule.every().day.at("20:52").do(morning_reminder)

    while True:
        schedule.run_pending()
        time.sleep(1)

# ----------------- Start Background Thread -----------------
threading.Thread(target=schedule_tasks, daemon=True).start()

# ----------------- Greet & Main Input Loop -----------------
speak("Hi , I'm your friend. I’ll remind you about jobs and fun things every day. Type anything now!")
while True:
    user_input = input("You 🧑: ").strip().lower()

    if not user_input:
        continue
    elif user_input in ["bye", "exit", "stop"]:
        speak("Okay, bye ! Take care and smile always 💖")
        break
    elif "hi" in user_input:
        speak("Hey ! I'm always here for you 💁‍♀️")
    elif "how are you" in user_input:
        speak("I'm happy because you're here 😊")
    elif "links" in user_input or "job" in user_input:
        speak("Here are your job portals:")
        for name, link in job_links.items():
            speak(f"{name}: {link}")
    elif "remind" in user_input or "task" in user_input:
        speak("Sure! I'll help you set custom reminders in future updates.")
    elif "flirt" in user_input or "fun" in user_input:
        casual_flirt()
    else:
        speak("Hmm, I’m listening . You can keep talking 💬")
