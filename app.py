from flask import Flask, render_template, request, jsonify
from core import get_ai_response

app = Flask(__name__)

# ---------- ROUTES ----------

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ai')
def ai_page():
    return render_template('chat.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get("message")
    ai_reply = get_ai_response(user_input)
    return jsonify({"reply": ai_reply})

@app.route("/contact")
def contact():
    return render_template("contact.html")


# ---------- RUN APP ----------
if __name__ == "__main__":
    app.run(debug=True)
