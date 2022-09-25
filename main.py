from flask import Flask
from waitress import serve

app = Flask(__name__)
STUDENTID = 10
@app.route('/')
def hello_world1():
    return f"Hello World!!!"

@app.route(f'/api/v1/hello-world{STUDENTID}'.format(STUDENTID))
def hello_world():
    return f"Hello World {STUDENTID}"


if __name__ == 'main':
    app.run(debug=True)

serve(app)