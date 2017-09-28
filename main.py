from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

import caesar

@app.route("/")
def index():
    return form.format("(type anything here)")

form = """<!DOCTYPE html>
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <form method='post' action='/'>
            <label>Offset Rotation? </label><input type='number' name='rot'/ value='0'><p>
            <label>Please type any message: </label><textarea name='text'>{0}</textarea><p>
            <label>Now click submit and watch the action!</label><input type='submit' name='button'/>
            </form>
        </body>
    </html>
    """

@app.route("/", methods=['POST'])
def post():
    text = request.form['text']
    rot = int(request.form["rot"])
    encrypted_message = caesar.encrypt(text.strip(), rot)

    return form.format(encrypted_message)

app.run()
