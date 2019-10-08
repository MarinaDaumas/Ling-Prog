from flask import Flask
buda = Flask(__name__)

@buda.route('/')
def hello_world():
    return 'Hello, World!'
    
if __name__ == "__main__":
    buda.run()