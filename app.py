import os
import signal
from flask import Flask, request
from buzz import generator, fizzbuzz, api

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
    page += ' '.join(map(str, fizzbuzz.fizzbuzz(0, 15)))
    page += '</h1></body></html>'
    return page


@app.route("/gif/<query>", endpoint='gif')
@app.route("/image/<query>", endpoint='image')
def image_search_page(query):
    url = {
        'image': api.image_search(query),
        'gif': api.gif_search(query),
    }[request.endpoint]
    if url is None:
        return "Couldn't find anything!"
    page = '<html><body>'
    page += '<img src="%s" alt="Founded image">' % url
    page += '</body></html>'
    return page


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT'))  # port 5000 is the default
