import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# کلیلەکەی تۆ لێرە بە ڕاستی جێگیر کراوە
API_KEY = "AIzaSyC04_c5G_xlZyhx5V0Dy2o7wuv7w8KrXFE"
genai.configure(api_key=API_KEY)

# ڕێکخستنی مۆدێلی Gemini
generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", # یان gemini-pro
    generation_config=generation_config
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message')
        
        if not user_message:
            return jsonify({"error": "نامەکە بەتاڵە"}), 400

        # ناردنی نامە بۆ زیرەکی دەستکرد
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(user_message)
        
        return jsonify({"reply": response.text})
    
    except Exception as e:
        # ئەگەر هەڵەیەک ڕوویدا لێرە دەردەکەوێت
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

# ئەم دوو دێڕە بۆ Vercel وەک ئۆکسجین وایە، دەبێت هەبێت
app = app

if __name__ == "__main__":
    app.run(debug=True)
