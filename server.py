from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello sir! I am Jarvis. Welcome home'

app.run(host='0.0.0.0', port=5000)
