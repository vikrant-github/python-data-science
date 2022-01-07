
from flask import Flask, request

app = Flask(__name__) # Creating a flask app

@app.route('/api', methods = ['POST']) # Python decorator to create an API route
def say_hello():
    data = request.get_json(force = True)
    name = data['name']
    return "Hello {0}".format(name)
    
if __name__ == '__main__':  # Main block entry point
    app.run(port =10001, debug = True)
