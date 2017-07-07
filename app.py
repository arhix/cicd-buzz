import os
import signal
from flask import Flask, request, render_template
from buzz import generator, fizzbuzz, api

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))


@app.route('/')
def generator_page():
    return render_template('basic.html', content=generator.generate_buzz())


@app.route('/fizzbuzz')
def fizzbuzz_page():
    return render_template(
        'basic.html',
        content=' '.join(map(str, fizzbuzz.fizzbuzz(0, 15))))


@app.route('/gif/<query>', endpoint='gif')
@app.route('/image/<query>', endpoint='image')
def image_search_page(query):
    url = {
        'image': api.image_search(query),
        'gif': api.gif_search(query),
    }[request.endpoint]
    if url:
        return render_template('image.html', url=url, alt=query)
    return render_template('basic.html', content="Couldn't find anything!")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))  # port 5000 is the default
