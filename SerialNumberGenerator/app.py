
from flask import Flask, request
import flask
from SerialNumberGenerator import SerialNumberGenerator
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

# Web API routes*
# Default route
@app.route('/')
def newSerialNumber():
    # Uses the global in this scope
    global serialNumberGenerator
    # Assign the return from our getNewSerialNumber method to serialNumber
    serialNumber = serialNumberGenerator.getNewSerialNumber()
    # and then return the serial number
    return str(serialNumber)

# "<range>" represents an integer entered by the user in the URL
# We will return as many serial numbers as the user entered in the URL
#http://localhost:53331/range?range=10
@app.route('/range')
def newSerialNumberRange():
    range = request.args.get('range')
    # Uses the global in this scope
    global serialNumberGenerator
    # We now need to call our getNewSerialNumberRange method from our global object
    serialRange = serialNumberGenerator.getNewSerialNumberRange(range)
    # and then return the range of serial numbers to the client
    return str(serialRange)

# Initialize our SerialNumber class as a global
serialNumberGenerator = SerialNumberGenerator()

#flask server spin up
if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
