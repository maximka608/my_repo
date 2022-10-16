
from flask import Flask

app = Flask(__name__)
student_id = 2
@app.route('/')
@app.route('/api/v1/hello-world-2')
def hello():
    return "Hello world 2"


