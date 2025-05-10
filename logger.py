from flask import Flask
from src.logging import logging


app = Flask(__name__)

@app.route('/',methods =['GET','POST'])
def index():
    logging.info('it is my test project')
    return 'hello world'

if __name__ == '__main__':
    app.run(debug=True, port='0.0.0.0')  # debug=True for auto-reload