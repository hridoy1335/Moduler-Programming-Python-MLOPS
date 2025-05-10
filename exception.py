import sys
from flask import Flask
from src.logging import logging
from src.exception import CustomException


app = Flask(__name__)

@app.route('/',methods =['GET','POST'])
def index():
    try:
        raise('error occured')
    except Exception as e:
        exception = CustomException(e,sys)
        logging.error(exception.error_message)
        
    logging.info('it is my test project')
    return 'hello world'

if __name__ == '__main__':
    app.run(port=5100)  # debug=True for auto-reload