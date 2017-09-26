from flask import Flask, request, caesar
app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too
"""
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        add_form="""
        <form action="/action_page.php" method="post">
            <rotate by:<input type="text" name="rot" value="0">
            <input type="textarea" name="text">
            <input type="submit">
        </form>
    """    
    </body>
</html>
@app.route("/", methods=['POST'])
def encrypt():
    encrypt = request.form['encrypt'] 


def index():
    return form

app.run()