from flask import Flask
import random

html = f'''
        <h1> Random Number: </h1>
        <hr>
        <ul>
            <li>{random.randint(1, 5)}</li>
            <li>{random.randint(1, 5)}</li>
            <li>{random.randint(1, 5)}</li>
            <li>{random.randint(1, 5)}</li>
            <li>{random.randint(1, 5)}</li>
        </ul>
        <hr>
        <ol>
            <li>{random.randint(1, 5)}</li>
            <li>{random.randint(1, 5)}</li>
            <li>{random.randint(1, 5)}</li>
            <li>{random.randint(1, 5)}</li>
            <li>{random.randint(1, 5)}</li>
        </ol>

        '''

app = Flask(__name__)

@app.route('/')
def hello_world():
    return html

if __name__ == '__main__':
    app.run()