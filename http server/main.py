from flask import Flask
from math import sqrt

app = Flask(__name__)


template = '''
<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <title>HI TIBCO</title>
    </head>

    <body>
        <h1>well? guess it's working!</h1>
        <p></p>
        <h2>@_@</h2>
    </body>

</html>
'''


@app.route("/")
def index():
    msg = 'go to /sqr/<number> to test it out'
    return template.replace('@_@', msg)


@app.route('/sqr/<int:num1>')
def add_nums(num1):
    return template.replace('@_@', str(sqrt(num1)))


app.run(host='0.0.0.0', port=80)
