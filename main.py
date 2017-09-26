from flask import Flask, request, caesar
app = Flask(__name__)

contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <meta content="text/html; charset=ISO-8859-1"
 http-equiv="content-type">
  <title>Web Caesar</title>
</head>
<body>
Web Caesar!
</body>
</html>
'''

def build_page(textarea_content):
    rot_label = "<label>Rotate by how many numbers? </label>"
    rotation_input = "<input type='number' name='rotation_number'/>"

    message_label = "<label>Please type any message: </label>"
    textarea = "<textarea name='message_textarea' style='height: 50px; width: 200px;'>" + textarea_content + "</textarea>"

    submit_label = "<label>Now click submit and watch the action! "
    submit = "<input type='submit' name='mess'/>"
    form =""" ("<form method='post' action='/'>" +
            rot_label + rotation_input + "<br><br>" +
            message_label + textarea + "<br><br>" +
            submit_label + submit +
            "</form>")"""

    return form
    

class MainHandler(webapp2.RequestHandler):

    # the initial place we go
    def get(self):
        content = build_page("(type anything in here)")
        self.response.write(content)

    # where we go to see the message via the form method
    def post(self):
        message = self.request.get("message_textarea")
        num = int(self.request.get("rotation_number"))
        encrypted_message = caesar.encrypt(message, num)
        escaped_message = cgi.escape(encrypted_message)

        content = build_page(escaped_message)
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler) # the only route I'm using for this app
], debug=True)

    # form {
    #             background-color: #eee;
    #             padding: 20px;
    #             margin: 0 auto;
    #             width: 540px;
    #             font: 16px sans-serif;
    #             border-radius: 10px;
    #         }
    #         textarea {
    #             margin: 10px 0;
    #             width: 540px;
    #             height: 120px;
#@app.route("/", methods=['POST'])
#def encrypt():
    #encrypt = request.form['encrypt'] 


#def index():
    #return form

#app.run()

app.config['DEBUG'] = True      # displays runtime errors in the browser, too