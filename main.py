from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    
    return f'{r}'

if __name__ == '__main__':
    app.run()