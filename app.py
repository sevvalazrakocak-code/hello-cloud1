from flask import Flask
app = Flask(__name_)

@app.route('/')
def home():
    return "Merhaba, Buluttan Selam!"
