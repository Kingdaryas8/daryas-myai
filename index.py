import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# کلیلەکەت لێرە جێگیر کراوە
genai.configure(api_key="AIzaSyC04_c5G_xlZyhx5V0Dy2o7wuv7w8KrXFE")

# ڕێکخستنی مۆدێلەکە
generation_config = {
    "temperature": 0.7,
    "max_output_tokens": 1000,
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message')
        
        if not user_message:
            return jsonify({"reply": "تکایە نامەیەک بنووسە..."}), 400

        # ناردنی نامە بۆ جێمنی
        response = model.generate_content(user_message)
        
        if response.text:
            return jsonify({"reply": response.text})
        else:
            return jsonify({"reply": "ببورە، وەڵامێک نەبوو."})
            
    except Exception as e:
        return jsonify({"reply": f"هەڵەیەک ڕوویدا: {str(e)}"}), 500

# گرنگترین بەش بۆ Vercel
app = app

if __name__ == "__main__":
    app.run(debug=True)
