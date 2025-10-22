import os
import google.generativeai as genai
from dotenv import load_dotenv
import re
load_dotenv()


# Load Gemini API key
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def local_response(user_input: str):
    """Simple offline/local replies without using API."""
    text = user_input.lower()

    if re.search(r"\b(hi|hello)\b", text):
        return "Hey there! Welcome to Savvix AI "
    elif "who are you" in text:
        return "I am Savvix an AI assistant"
    elif re.search(r"\b(created you|made you|trained you)\b", text):
        return "I was created by Savestar and trained a bit by him."
    elif "Thaku" in text:
        return "you have entered bro code you are a legit member"
    elif "chakhaza" in text:
        return "I know chakhaza a pretty tall guy"
    elif "prince" in text or "chisuse" in text:
        return "hallo mr chisuse....should l call you mister?...why are you gay?"
    elif "who says am gay" in text or "says who" in text or "who told you am gay" in text:
        return "You are gay"
    elif "ikila" in text or "noobie" in text:
        return "sup mn tell me something...ladies first remember?"
    elif "watson" in text or "wat" in text:
        return "I know that guy a complete introvert"
    elif "savestar" in text:
        return "That's my creator, the mastermind behind Savvix!"
    elif "thank" in text:
        return "You're welcome bro "
    elif "offline" in text:
        return "You seem to be offline. Some features might not work."
    else:
        return None  # If no match, fall back to Gemini

def get_ai_response(user_input: str):
    """Use Gemini for general chat when no local reply exists."""
    local = local_response(user_input)
    if local:
        return local

    try:
        model = genai.GenerativeModel("gemini-2.5-flash-lite")
        response = model.generate_content(user_input)

        #  FIX: handle text correctly
        if hasattr(response, "text") and response.text:
            return response.text.strip()
        elif hasattr(response, "candidates") and response.candidates:
            return response.candidates[0].content.parts[0].text.strip()
        else:
            return "Hmm... I didn’t quite get that."
    except Exception as e:
        print("Gemini Error:", e)
        return "Sorry, I couldn’t connect to the AI right now."