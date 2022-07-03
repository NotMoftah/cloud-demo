import flask
from math import sqrt

app = flask.Flask(__name__)


template = '''
<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <title>INSTA TIBCO</title>
    </head>

    <body>
        <h1>Welcome to instagram (tibco eddition)...</h1>
    </body>

</html>
'''


@app.route("/")
def index():
    # msg = 'wall is empty?'
    # return template.replace('@_@', msg)
    # <img src="" alt="feed">
    return template


app.run(host='0.0.0.0', port=80)
