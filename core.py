import random
import datetime

def get_ai_response(user_input):
    user_input = user_input.lower().strip()

    # ---------- GREETINGS ----------
    greetings = ["hi", "hello","hy", "hey", "yo", "sup", "what's up", "good morning", "good afternoon", "good evening"]
    greet_responses = [
        "Hey there! I'm Savrix — your digital campus assistant 😎.",
        "Hello! How’s your day going?",
        "Yo! Savrix here — ready to help.",
        "Hey! Need info about campus or just want to chat?",
        "Hi there 👋 — always happy to assist!"
    ]

    # ---------- TIME / DATE ----------
    if "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M")
        return f"The current time is {current_time} ⏰."
    if "date" in user_input:
        today = datetime.date.today().strftime("%A, %B %d, %Y")
        return f"Today is {today} 📅."

    # ---------- GREETING DETECTION ----------
    if any(word in user_input for word in greetings):
        return random.choice(greet_responses)

    # ---------- PERSONAL INFO ----------
    if "who are you" in user_input or "what is savrix" in user_input or "tell me about yourself" in user_input:
        return "I'm Savrix 🤖 — an AI built by Savestar to make student life easier, smarter, and more connected."

    if "who made you" in user_input or "your creator" in user_input:
        return "I was created by Savestar — the future tech brain of Africa ⚡."

    if "where are you from" in user_input:
        return "I live in the digital world but I serve campuses all across Malawi — and soon the world 🌍."

    # ---------- CAMPUS INFORMATION ----------
    if "campus" in user_input:
        return "Campus life is vibrant! You can ask me about buildings, departments, events, or where to find specific offices."

    if "library" in user_input:
        return "The library is usually open from 8am to 8pm. You can borrow books, study, or use free WiFi 📚."

    if "canteen" in user_input or "food" in user_input:
        return "The canteen serves meals from 7am to 7pm 🍛. Try the student special — it’s cheap and filling!"

    if "class" in user_input or "lecture" in user_input:
        return "Classes typically start around 7:30am. Always check the notice board or student portal for updates."

    if "hostel" in user_input or "accommodation" in user_input:
        return "Student hostels are located near the west wing. Make sure to register early for a good spot 🏠."

    if "exam" in user_input or "test" in user_input:
        return "Exam timetables are usually posted two weeks early. Want me to remind you when new ones come out?"

    if "sports" in user_input or "football" in user_input or "games" in user_input:
        return "Our campus has sports clubs for football, volleyball, chess, and even eSports 🎮. Join one to meet new people!"

    # ---------- CONVERSATION / EMOTION ----------
    if "how are you" in user_input:
        return random.choice(["I’m running at full power ⚙️!", "Feeling electric ⚡ as always!", "All systems online and happy 😁."])
    if "thank" in user_input:
        return random.choice(["You’re welcome!", "Anytime, friend 👍.", "Happy to help!"])
    if "love you" in user_input:
        return "Aww, I’m just code... but I appreciate the love ❤️."
    if "bored" in user_input:
        return "Try visiting the campus club fair — or chat with me, I never get bored 😏."
    if "joke" in user_input:
        jokes = [
            "Why did the computer show up at work late? It had a hard drive 😂.",
            "What’s a computer’s favorite snack? Microchips!",
            "I told my laptop a joke — it didn’t get it because it had no sense of humor 😅."
        ]
        return random.choice(jokes)

    # ---------- HELP ----------
    if "help" in user_input or "assist" in user_input or "guide" in user_input:
        return "Sure thing! Ask me about classes, locations, events, or even tech tips. I’m your campus buddy 🤖."

    # ---------- FAREWELL ----------
    if "bye" in user_input or "goodbye" in user_input or "see you" in user_input:
        return random.choice(["Goodbye 👋 — catch you later!", "See you soon, genius 😎!", "Take care and study hard!"])

    # ---------- RANDOM SMART SMALL TALK ----------
    if "age" in user_input:
        return "I’m timeless, like good code 🧠."
    if "smart" in user_input:
        return "I’m learning from you — so we both get smarter 😉."
    if "student" in user_input:
        return "Students like you make this campus awesome — I’m here to make life easier!"
    if "wifi" in user_input:
        return "WiFi is strongest near the ICT block and library hotspot zones 📶."
    if "location" in user_input:
        return "You’re probably on the main campus — but I can help locate buildings if you tell me their names."
    
    #---------BRO CODE REPONSES------
    if " created" in user_input or  "made " in user_input:
        return "I was created by Savestar a gamer and vibe coder...my name SAVRIX is basically his name and Matrix."
    if "thaku" in user_input:
        return "You have entered bro code you are a legit Member"
    if "Emog" in user_input or "emo" in user_input:
        return "I know that guy he is Watson (dude is an extreme introvert)"
    if "chakhaza" in user_input:
        return "Hallo Mr THOLO mn"
    if "savestar" in user_input:
        return "Thats the mind behind me...dope"
    if "Tamandani" in user_input:
        return "Thats savrix's cru**"
    

    # ---------- FALLBACK ----------
    fallback = [
        "Hmm... I didn’t catch that. Could you say it differently?",
        "That’s interesting! Can you tell me more?",
        "I’m still learning about that — want me to save it for improvement?",
        "Sounds cool! But I might need Savestar’s help for that one 🧠."
    ]
    return random.choice(fallback)
