import os
import flask

# create flask app
app = flask.Flask(__name__)

# create http template
template = '''
<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <title>INSTA - TIBCO</title>
    </head>

    <body>
        <h1>Welcome to instagram (tibco eddition).</h1>
    </body>

</html>
'''


# main route
@app.route("/")
def index():
    return template


# run app
app.run(host='0.0.0.0', port=80)
