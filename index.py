from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "سڵاو! سێرڤەرەکە بەبێ کێشە کار دەکات."

@app.route('/test')
def test():
    return jsonify({"status": "success", "message": "ئەمە تاقیکردنەوەیە"})

app = app
