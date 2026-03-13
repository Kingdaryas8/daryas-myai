import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# بەستنەوەی کلیلەکەت بە مێشکی Gemini
genai.configure(api_key="AIzaSyC04_c5G_xlZyhx5V0Dy2o7wuv7w8KrXFE")

# هەڵبژاردنی مۆدێلی ژیری دەستکرد
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def home():
    # ناردنی بەکارهێنەر بۆ لاپەڕە سەرەکییەکە
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # وەرگرتنی نامەکە لە وێبسایتەکەوە
        data = request.json
        user_message = data.get('message')

        if not user_message:
            return jsonify({"reply": "تکایە شتێک بنووسە..."})

        # ناردنی نامەکە بۆ Gemini و وەرگرتنی وەڵام
        response = model.generate_content(user_message)
        bot_reply = response.text

        return jsonify({"reply": bot_reply})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"reply": "ببوورە، کێشەیەک لە پەیوەندی بە سێرڤەر هەبوو. دڵنیابە ئینتەرنێتەکەت یان VPNـەکەت کار دەکات."})

if __name__ == '__main__':
    # دەستپێکردنی بەرنامەکە
    app.run(debug=True)
