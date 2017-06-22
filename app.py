import os
import signal
from flask import Flask
from buzz import generator, fizzbuzz

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))


@app.route("/")
def generator_page():
    page = '<html><body><h1>'
    page += generator.generate_buzz()
    page += '</h1></body></html>'
    return page


@app.route("/fizzbuzz")
def fizzbuzz_page():
    page = '<html><body><h1>'
    page += fizzbuzz.fizzbuzz(0, 15)
    page += '</h1></body></html>'
    return page


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT'))  # port 5000 is the default
