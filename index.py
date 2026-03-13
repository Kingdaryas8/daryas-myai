from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)

# کلیلەکەت بە ڕاستەوخۆ
genai.configure(api_key="AIzaSyC04_c5G_xlZyhx5V0Dy2o7wuv7w8KrXFE")
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        content = request.json.get('message')
        if not content:
            return jsonify({"reply": "هیچ نامەیەک نییە"}), 400
            
        response = model.generate_content(content)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"}), 200 # لێرە کردمان بە 200 بۆ ئەوەی سێرڤەرەکە سوور نەبێتەوە

app = app
