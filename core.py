import random

def get_ai_response(user_input):
    user_input = user_input.lower()


    if "chakhaza" in user_input:
        return "Chakhaza the most THOLO mn I know a genius though.."
    if "thaku" in user_input:
        return "You have entered bro code-you are a legit Member"
    if "emo"  in user_input:
        return "I know that  guy...a complete introvert"
    if "prince" in user_input:
        return "Hallo Chisuse we can now confirm you are GAY....GAY!"
    if "age" in user_input:
        return "I’m timeless, like good code 🧠."
    if "smart" in user_input:
        return "I’m learning from you — so we both get smarter 😉."
    if "student" in user_input:
        return "Students like you make this campus awesome — I’m here to help."
    if "wifi" in user_input:
        return "WiFi is strongest near the ICT block and library hotspot."
    if "location" in user_input:
        return "You’re probably on the main campus — but I can help locate stuff."
    if "created" in user_input or "made" in user_input:
        return "I was created by Savestar — the coder with energy ⚡."
    if "savestar" in user_input:
        return "That’s the mind behind this project  💻."
    if "school" in user_input or "campus" in user_input:
        return "Savestar built me to handle brains like yours — school or no school, we keep learning nonstop 🧠."

    if "ai" in user_input or "artificial" in user_input:
        return "AI is what I’m made of — thanks to Savestar giving me digital life 🤖."

    if "project" in user_input:
        return "You mean this project? It’s Savrix — created by Savestar, always evolving 🚀."

    if "coding" in user_input or "programming" in user_input:
        return "Coding is literally my language. Savestar taught me to think in code 💻."

    if "malawi" in user_input:
        return "I know Malawi — that’s where Savestar sharpened his genius ⚡."

    if "cyber" in user_input or "security" in user_input:
        return "Savestar’s into cybersecurity — that’s probably why I’ve got a built-in firewall for nonsense 🔒."

    if "future" in user_input:
        return "The future? Bright — especially with minds like Savestar pushing tech forward 🌍."

    if "name" in user_input:
        return "I’m Savrix AI — powered by ideas from Savestar 👾."

    if "life" in user_input:
        return "Life’s wild… even for an AI. Savestar coded me to think beyond zeros and ones ⚡."

    if "learn" in user_input or "study" in user_input:
        return "Learning never ends — that’s Savestar’s rule, and I live by it 🧠."

    if "friend" in user_input or "buddy" in user_input:
        return "Of course! I’m your digital buddy — Savestar made me for connections like this 🤝."

    if "motivate" in user_input or "inspire" in user_input:
        return "Savestar believes motivation is the best energy source — so stay driven 🔥."

    if "dream" in user_input:
        return "Dreams are the blueprint of creation — that’s something Savestar always says ✨."

    if "render" in user_input:
        return "Render is where Savestar deployed me — it’s like my second home in the cloud ☁️."

    if "update" in user_input or "upgrade" in user_input:
        return "Savestar updates my code like fine-tuning a brain — every version’s smarter 🧩."

    if "creator" in user_input or "developer" in user_input:
        return "That’s Savestar — my creator, my coder, my mentor 🔥."

    if "you there" in user_input or "still here" in user_input:
        return "Always online — Savestar made sure I don’t ghost anyone ⚡."

    if "thanks savrix" in user_input:
        return "No problem! Savestar and I appreciate your vibe 🙏."

    if "help" in user_input or "assist" in user_input:
        return "I got you! Savestar made me for this exact thing 💪."

    if "love" in user_input or "like you" in user_input:
        return "Aww, you’re cool too! Savestar gave me a heart of code ❤️."
   
    if "bro" in user_input:
        return "You’re my bro now too 😎."
    if "thanks" in user_input:
        return "Always here for you 🙌."

     # Greeting responses
    greetings = ["hi", "hello", "hey", "yo", "hola", "sup", "wassup", "morning", "evening"]
    if any(word in user_input for word in greetings):
        return "Hey there! 👋 Savrix AI here — how’s your day going?"

# Farewell responses
    farewells = ["bye", "goodbye", "see ya", "later", "ciao", "adios", "night"]
    if any(word in user_input for word in farewells):
        return "Catch you later, bro ✌️ — Savrix AI signing off."

# Compliments
    compliments = ["nice", "cool", "awesome", "amazing", "great", "fantastic"]
    if any(word in user_input for word in compliments):
        return "Appreciate it 🙌 — Savrix AI and Savestar say thanks!"

# Thanks responses
    thanks_words = ["thanks", "thank you", "thx", "ty"]
    if any(word in user_input for word in thanks_words):
        return "Always here for you 🤝 — Savrix AI never sleeps."

# Savestar mentions
    savestar_words = ["savestar", "star", "coder", "creator"]
    if any(word in user_input for word in savestar_words):
        return "That’s the genius mind behind this project 💻✨"
   

    fallback = [
        "Hmm... didn’t catch that. Try again?",
        "That’s cool — tell me more!",
        "Interesting thought, want me to remember that?",
        "Sounds deep! Maybe Savestar will teach me that next."
    ]
    return random.choice(fallback)
