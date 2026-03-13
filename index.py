import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# کلیلەکەی تۆ لێرە جێگیر کرا
genai.configure(api_key="AIzaSyC04_c5G_xlZyhx5V0Dy2o7wuv7w8KrXFE")

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

model = genai.GenerativeModel(
  model_name="gemini-pro",
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
            return jsonify({"error": "No message provided"}), 400

        response = model.generate_content(user_message)
        return jsonify({"reply": response.text})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# زۆر گرنگە بۆ کارکردنی لەسەر Vercel
app = app

if __name__ == "__main__":
    app.run(debug=True)
