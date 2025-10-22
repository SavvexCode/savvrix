
from flask import Flask, render_template, request, jsonify
from core import get_ai_response

app = Flask(__name__)

# ---------- ROUTES ----------

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/ai')
def ai_mode():
    return render_template('ai.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


# ---------- AI CHAT ENDPOINT ----------
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message', '')
    response = get_ai_response(user_input)
    return jsonify({'response': response})


# ---------- RUN ----------
if __name__ == '__main__':
    #app.run(debug=True)#
    app.run(host = "0.0.0.0", port=5000)
          